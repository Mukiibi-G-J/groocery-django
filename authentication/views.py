from django.shortcuts import render




def login (request):
    render(request,'account/login.html')




def signin (request):
    render(request,'account/signup.html')
    