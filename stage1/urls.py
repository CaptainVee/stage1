from django.urls import path, include
from .views import PersonView


urlpatterns = [
   path("api/", PersonView.as_view(), name="api"),
]