from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Salon

def index(request):
    posts = Salon.objects.filter(is_public=False).order_by("id").all()
    context = {
        "post": posts
    }
    return render(request, "/index.html", context)