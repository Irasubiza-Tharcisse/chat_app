from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Friend
from django.contrib.auth.models import User

@login_required
def add_friends_view(request):
   
    users = User.objects.all()
    username = request.session['username']
    info = User.objects.get(username=username)
    context = {
        'users':users,
        'info':info
    }
    return render(request, 'friends/add_friends.html', context)
  
def add_friend(request, user_id):
    try:
        friend = User.objects.get(id=user_id)
        if friend != request.user:  # Prevent adding oneself as a friend
            Friend.objects.get_or_create(user=request.user, friend=friend)
            messages.success(request, f'You are now friends with {friend.username}!')
        else:
            messages.error(request, 'You cannot add yourself as a friend.')
    except User.DoesNotExist:
        messages.error(request, 'User does not exist.')

    return redirect('add_friends')  # Redirect to the chat room or appropriate page

@login_required
def my_friends_view(request):
    username = request.session['username']
    info = User.objects.get(username=username)
    friends = request.user.friends.all()
    context={
        'info':info,
        'friends':friends,
    }
    return render(request, 'friends/my_friends.html', context)