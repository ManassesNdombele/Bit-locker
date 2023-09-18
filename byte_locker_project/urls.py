from django.contrib import admin
from django.urls import path
from byte_locker_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home_view')
]
