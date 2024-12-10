# chat_messages/views.py
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Message


def recieved_messages_view(request):
    username = request.session['username']
    info = User.objects.get(username=username)
    
    messages = Message.objects.filter(recipient=request.user)
    context = {
        'messages':messages,
        'info':info,
    }
    return render(request, 'messages/recieved_messages.html',context)



def chat_messages_view(request):
    username = request.session['username']
    info = User.objects.get(username=username)
    context ={
        'info':info,
    }
    if request.method == 'POST':
        content = request.POST.get('content')
        try:
            recipient = User.objects.first()
            if recipient and content:
                sent_message = Message.objects.create(sender=request.user, recipient=recipient, content=content)
                context={
                    'sent_message':sent_message,
                    
                }
                messages.success(request, 'Message sent successfully!')
            else:
                messages.error(request, 'Invalid data.')
        except Exception as e:
             messages.error(request, f'Error: {str(e)}')
             return render(request, 'messages/chat_messages.html',context)
    return render (request,'messages/chat.html',context)