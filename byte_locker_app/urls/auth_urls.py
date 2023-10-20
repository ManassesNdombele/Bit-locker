from django.urls import path
from byte_locker_app.views import Auth_Platform

auth_views = Auth_Platform()

urlpatterns = [
    path('login/', auth_views.login, name='login'),
    path('register/', auth_views.register, name='register')
]
