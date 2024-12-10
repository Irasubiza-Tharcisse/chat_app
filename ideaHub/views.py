from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from userinfo.models import user_profile
# Create your views here.


def index_view(request):
  return render(request, 'index.html')


def login_view(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    print(user)
    if user is not None:
      login(request, user)
      request.session['username'] = user.username
      return redirect('profile')
    else:
      return HttpResponse(f'Invalid credentials')

  else:
    return render(request, 'index.html')


@login_required
def profile_view(request):
  if 'username' not in request.session:
    return redirect('login')

  else:
    username = request.session['username']
    info = User.objects.get(username=username)
    context = {'info': info}
    return render(request, 'profile/profile.html', context)


def logout_view(request):
  logout(request)
  return redirect('login')
