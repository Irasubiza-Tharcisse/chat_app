from django.contrib import admin
from django.urls import path
from .views import index_view,login_view,logout_view, profile_view

urlpatterns =[
  
  path('', index_view, name="home"),
  path('login/',login_view, name="login"),
  path('profile/', profile_view, name="profile"),
  path('logout/', logout_view, name="logout")
]