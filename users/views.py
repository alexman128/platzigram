"""Users views"""

# Django
from django.contrib.auth import authenticate, login
from django.shortcuts import render

# Create your views here.

def login_view(request):
    """Login view"""
    return render(request, 'users/login.html')
