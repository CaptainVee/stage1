from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
import subprocess
import whisper

class VideoUploadView(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        video_file = request.FILES.get('video')

        if not video_file:
            return Response({'message': 'No video file provided'}, status=status.HTTP_400_BAD_REQUEST)

        # Save the video to disk
        fs = FileSystemStorage()
        video_filename = fs.save(video_file.name, video_file)

        # Construct the URL of the uploaded video file
        video_url = os.path.join(settings.MEDIA_URL, video_filename)

        # Define the output audio file path
        audio_filename = os.path.splitext(video_filename)[0] + '.mp3'
        audio_file_path = os.path.join(settings.MEDIA_ROOT, audio_filename)

        # Use ffmpeg to extract audio from the video
        ffmpeg_cmd = [
            'ffmpeg',
            '-i', os.path.join(settings.MEDIA_ROOT, video_filename),
            '-vn', '-acodec', 'libmp3lame',
            audio_file_path,
        ]

        try:
            subprocess.run(ffmpeg_cmd, check=True)
        except subprocess.CalledProcessError as e:
            return Response({'message': f'Error extracting audio: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Load the Whisper ASR model
        whisper_model = whisper.load_model('base')

        # Transcribe the audio
        try:
            result = whisper_model.transcribe(audio_file_path)
            transcribed_text = result['text']
        except Exception as e:
            return Response({'message': f'Error transcribing audio: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Return the response with message, video URL, and transcribed text
        response_data = {
            'message': 'Video processed successfully',
            'video_url': video_url,
            'transcribed_text': transcribed_text,
        }

        return Response(response_data, status=status.HTTP_201_CREATED)

