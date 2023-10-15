from django.urls import path
from byte_locker_app.views import *

urlpatterns = [
    path('form/', password_generator, name='passwd_gen_form'),
    path('generate-password/', generate_password, name='gen_passwd'),
    path('save-account-datas/', save_account_datas, name='save_account_datas')
]
