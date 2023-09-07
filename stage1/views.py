from django.views import View
from django.http import JsonResponse
from django.utils import timezone

class EndpointView(View):
    def get(self, request):
        slack_name = request.GET.get('slack_name', '')
        track = request.GET.get('track', '')
        current_time = timezone.now()
        
        data = {
            "slack_name": slack_name,
            "current_day": current_time.strftime('%A'),
            "utc_time": current_time.strftime('%Y-%m-%dT%H:%M:%SZ'),
            "track": track,
            "github_file_url": "https://github.com/CaptainVee/stage1/blob/main/stage1/views.py",
            "github_repo_url": "https://github.com/CaptainVee/stage1",
            "status_code": 200,
        }


        return JsonResponse(data)