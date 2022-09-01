from nturl2path import url2pathname
from django.urls import path
from . import views
app_name = 'authentication'

urlpatterns = [
    path('login/', views.login, name="login"),
    path('signin/', views.signin, name="signin")
]