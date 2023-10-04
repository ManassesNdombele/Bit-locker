from django.shortcuts import render
from random import choices

def home(request):
    return render(request, 'index.html')

def password_generator(request):
    return render(request, 'passwd-gen.html', {'DATA_SENDED': False, 'ERROR': False, 'MESSAGE': ''})

def account_configs(request):
    return render(request, 'account-configs.html')

def authentication(request):
    return render(request, 'authentication.html')

def help_center(request):
    return render(request, 'help-center.html')

def saved_accounts(request):
    return render(request, 'saved-accounts.html')

def saved_passwords(request):
    return render(request, 'saved-passwd.html')

def generate_password(request):
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
            print(password)
            return render(request, 'index.html')
