# urls.py
from django.urls import path
from . import views 

urlpatterns = [
    path('add_friends/',views.add_friends_view,name='add_friends'),
    path('add-friend/<int:user_id>/',views.add_friend, name='add_friend'),
    path('my_friends/',views.my_friends_view, name='my_friends'),
]