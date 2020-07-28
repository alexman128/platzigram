"""Users views"""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Models

from django.contrib.auth.models import User
from users.models import Profile

# Create your views here.

def login_view(request):
    """Login view"""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if (user):
            login(request, user)
            return redirect('feed')
        else:
            return(render(request, 'users/login.html', {'error': 'Invalid username and password'}))
    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    """ Logout view """
    logout(request)
    return redirect('login')

def signup_view(request):
    """ Sign up view """
    if request.method == "POST":
        username = request.POST.get('username', True)
        passwd = request.POST.get('passwd', True)
        passwd_confirmation = request.POST.get('passwd_confirmation', True)

        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html', {'error': f'Password confirmation doest not match {passwd}, {passwd_confirmation}'})
        
        try:
            user = User.objects.create_user(username=username, password=passwd)
        except Exception as e:
            return render(request, 'users/signup.html', {'error': f'Error al crear el usuario: {e}'})

        user.first_name = request.POST.get('first_name', True)
        user.last_name = request.POST.get('last_name', True)
        user.email = request.POST.get('email', True)
        import pdb; pdb.set_trace()
        user.save()

        profile = Profile(user=user)
        profile.save()
        redirect('login')

    return render(request, 'users/signup.html')