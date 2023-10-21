from django.urls import path
from byte_locker_app.views import (
    saved_passwords,
    new_password_datas,
    save_password_datas
)

urlpatterns = [
    path('list/', saved_passwords, name='passwords_list'),
    path('new-password-datas/', new_password_datas, name='new_passwd_datas'),
    path('save-password-datas/', save_password_datas, name='save_password_datas')
]
