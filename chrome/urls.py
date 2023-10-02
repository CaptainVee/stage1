from django.urls import path
from .views import VideoUploadView

urlpatterns = [
    path('upload/', VideoUploadView.as_view(), name='video-upload'),
    # Add more views/URLs as needed for rendering the video page
]
