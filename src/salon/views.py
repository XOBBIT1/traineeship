from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Salon

def index(request):
    return render(request, 'salon/main.html')