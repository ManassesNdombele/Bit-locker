from django.urls import path
from byte_locker_app.views import (password_generator, generate_password, save_account_datas, regenerate_password, cancel_generation, generation_sucess)

urlpatterns = [
    path('form/', password_generator, name='passwd_gen'),
    path('generate-password/', generate_password, name='gen_passwd'),
    path('save-account-datas/', save_account_datas, name='save_account_datas'),
    path('regenerate-password/', regenerate_password, name='regen_passwd'),
    path('cancel-generation/', cancel_generation, name='cancel_generation'),
    path('sucess/', generation_sucess, name='generation_sucess')
]
