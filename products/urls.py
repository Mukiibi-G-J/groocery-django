from base64 import urlsafe_b64decode
from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
]
