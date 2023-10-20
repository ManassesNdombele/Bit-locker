from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from random import choices
from byte_locker_app.models import Accounts

class Auth_Platform():
    def register(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        
        else:
            if request.method == 'GET':
                return render(request, 'register.html', {'DATA_SENDED': False, 'ERROR': False, 'MESSAGE': None})
            
            elif request.method == 'POST':
                username = request.POST.get('username-name')
                email = request.POST.get('email-name')
                password = request.POST.get('password-name')
                password_confirmation = request.POST.get('password-confirm-name')
                username_datas = User.objects.filter(username=username).first()
                email_datas = User.objects.filter(email=email).first()
                if username_datas:
                    return render(request, 'register.html', {'DATA_SENDED': True, 'ERROR': True, 'MESSAGE': 'Use outro nome de usuário porque esse nome já foi cadastrado no sistema.', 'USERNAME': username, 'EMAIL': email, 'PASSWORD': password, 'PASSWORD_CONFIRMATION': password_confirmation})

                elif email_datas:
                    return render(request, 'register.html', {'DATA_SENDED': True, 'ERROR': True, 'MESSAGE': 'Este email já foi cadastrado no sistema tente outro email.', 'USERNAME': username, 'EMAIL': email, 'PASSWORD': password, 'PASSWORD_CONFIRMATION': password_confirmation})
            
                elif password != password_confirmation:
                    return render(request, 'register.html', {'DATA_SENDED': True, 'ERROR': False, 'MESSAGE': 'A sua senha deve ser igual ao campo de confirmação de senha.', 'USERNAME': username, 'EMAIL': email, 'PASSWORD': password, 'PASSWORD_CONFIRMATION': password_confirmation})

                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    return redirect('login')

    def login(self, request):
        if request.user.is_authenticated:
            return redirect('home')

        else:
            if request.method == 'GET':
                return render(request, 'login.html', {'DATA_SENDED': False, 'ERROR': False, 'MESSAGE': None})

            elif request.method == 'POST':
                username = request.POST.get('username-name')
                password = request.POST.get('password-name')
                user = authenticate(username=username, password=password)
                if user:
                    auth_login(request, user)
                    return redirect('home')

                else:
                    return render(request, 'login.html', {'DATA_SENDED': True, 'ERROR': True, 'MESSAGE': 'Nome de usuário ou senha inválidos, tente novamente', 'Senha': password, 'PASSWORD': password})

@login_required(login_url='/auth/login/')
def password_generator(request):
    return render(request, 'passwd-gen.html', {'DATA_SENDED': False, 'ERROR': False, 'MESSAGE': None})

@login_required(login_url='/auth/login/')
def generate_password(request):
    if request.method == 'GET':
        return render(request, 'permission-error.html')

    if request.method == 'POST':
        program_name = request.POST.get('software-name-input')
        email = request.POST.get('email-input')
        user_name = request.POST.get('user-name-input')
        char_length = request.POST.get('char-length-input')
        upper_letters_check = request.POST.get('upper-letters-checkbox')
        lower_letters_check = request.POST.get('lower-letters-checkbox')
        numbers_check = request.POST.get('numbers-checkbox')
        account_description = request.POST.get('account-description-textbox')
        if str(email) == '' and str(user_name) == '':
            return render(request, 'passwd-gen.html', {'DATA_SENDED': False, 'ERROR': True, 'MESSAGE': 'Tens de preencher o campo de email ou o campo de nome de usuário ou os dois campos!'})

        else:
            upper_letters = ''
            lower_letters = ''
            numbers_chars = ''
            if str(upper_letters_check) == 'on':
                upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

            if str(lower_letters_check) == 'on':
                lower_letters = 'abcdefghijklmnopqrstuvwxyz'

            if str(numbers_check) == 'on':
                numbers_chars = '0123456789'

            base_chars = f'{upper_letters}{lower_letters}{numbers_chars}!@#$%&*-'
            passwd_char_list = choices(base_chars, k=int(char_length))
            password = ''.join(passwd_char_list)
            return render(request, 'passwd-gen.html', {'DATA_SENDED': True, 'ERROR': False, 'MESSAGE': None, 'PROGRAM_NAME': program_name, 'EMAIL': email, 'USER_NAME': user_name, 'DESCRIPTION': account_description, 'PASSWORD': password})

@login_required(login_url='/auth/login/')
def save_account_datas(request):
    if request.method == 'GET':
        return render(request, 'permission-error.html')

    if request.method == 'POST':
        program_name = request.POST.get('software-name-input')
        email = request.POST.get('email-input')
        user_name = request.POST.get('user-name-input')
        account_description = request.POST.get('account-description-textbox')
        account_password = request.POST.get('generated-passwd-input')
        user_id = request.user
        new_account = Accounts(program_name=program_name, email=email, username=user_name, description=account_description, password=account_password, user=user_id)
        new_account.save()
        return redirect('generation_sucess')

@login_required(login_url='/auth/login/')
def regenerate_password(request):
    return redirect('gen_passwd')

@login_required(login_url='/auth/login/')
def cancel_generation(request):
    return redirect('passwd_gen')

@login_required(login_url='/auth/login/')
def generation_sucess(request):
    return render(request, 'generation-sucess.html')

@login_required(login_url='/auth/login/')
def home(request):
    return render(request, 'index.html')

@login_required(login_url='/auth/login/')
def account_configs(request):
    return render(request, 'account-configs.html')

@login_required(login_url='/auth/login/')
def authentication(request):
    return render(request, 'authentication.html')

@login_required(login_url='/auth/login/')
def help_center(request):
    return render(request, 'help-center.html')

@login_required(login_url='/auth/login/')
def saved_accounts(request):
    return render(request, 'saved-accounts.html')

@login_required(login_url='/auth/login/')
def saved_passwords(request):
    return render(request, 'saved-passwd.html')
