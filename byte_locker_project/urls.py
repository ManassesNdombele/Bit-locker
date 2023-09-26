from django.contrib import admin
from django.urls import path
from byte_locker_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home_view'),
    path('password-generator/', password_generator, name='passwd_gen'),
    path('account-configs/', account_configs, name='account_configs'),
    path('authentication/', authentication, name='authentication'),
    path('help-center', help_center, name='help_center'),
    path('saved-accounts/', saved_accounts, name='saved_accounts'),
    path('saved-passwords/', saved_passwords, name='saved_passwords')
]
