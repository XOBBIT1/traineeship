from django.shortcuts import render, redirect

def index(request):
    return render(request, 'salon_app/main.html')