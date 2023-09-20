from django.shortcuts import render
from random import choices

def home(request):
    response = {
        'DATA_SENDED': False
    }

    return render(request, 'index.html')

def generate_password(to: list, max_length: int):
    char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!"#$%&/_-@'
    chars = choices(char_list, k=max_length)
    for c in range(0, 5):
        to.append(''.join(chars))
    return to

def password_generator(request):
    response = {
        'DATA_SENDED': True,
        'ERROR': False,
        'ERROR_DESC': '',
        'FIRST_PASSWD': None,
        'SECOND_PASSWD': None,
        'THIRD_PASSWD': None,
        'FOURTH_PASSWD': None,
        'FIFTH_PASSWD': None
    }

    if request.method == 'POST':
        software_name = request.POST.get('software-name-input')
        email_or_user = request.POST.get('email-user-name-input')
        char_length = request.POST.get('char-length-input')
        if software_name == '' or email_or_user == '' or char_length == '':
            response['ERROR'] = True
            response['ERROR_DESC'] = 'Todos os campos são obrigatórios!'
            return render(request, 'index.html', response)

        else:
            response['FIRST_PASSWD'] = generate_password(to=[], max_length=int(char_length))[0]
            response['SECOND_PASSWD'] = generate_password(to=[], max_length=int(char_length))[1]
            response['THIRD_PASSWD'] = generate_password(to=[], max_length=int(char_length))[2]
            response['FOURTH_PASSWD'] = generate_password(to=[], max_length=int(char_length))[3]
            response['FIFTH_PASSWD'] = generate_password(to=[], max_length=int(char_length))[4]
            return render(request, 'index.html', response)
