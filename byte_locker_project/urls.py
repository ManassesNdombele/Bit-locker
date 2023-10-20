from django.urls import path, include
from django.contrib import admin 
from byte_locker_app.views import (
    home,
    account_configs,
    authentication,
    help_center,
    saved_accounts,
    saved_passwords
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('auth/', include('byte_locker_app.urls.auth_urls')),
    path('password-generator/', include('byte_locker_app.urls.password_generator')),
    path('account-configs/', account_configs, name='account_configs'),
    path('authentication/', authentication, name='authentication'),
    path('help-center/', help_center, name='help_center'),
    path('saved-accounts/', saved_accounts, name='saved_accounts'),
    path('saved-passwords/', saved_passwords, name='saved_passwords')
]
