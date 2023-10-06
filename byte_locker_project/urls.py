from django.urls import path, include
from byte_locker_app.views import *

urlpatterns = [
    path('', home, name='home_view'),
    path('password-generator/', include('byte_locker_app.urls')),
    path('account-configs/', account_configs, name='account_configs'),
    path('authentication/', authentication, name='authentication'),
    path('help-center/', help_center, name='help_center'),
    path('saved-accounts/', saved_accounts, name='saved_accounts'),
    path('saved-passwords/', saved_passwords, name='saved_passwords'),
    path('generate-passwd/', generate_password, name='generate_password')
]
