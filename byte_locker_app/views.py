from django.shortcuts import render

def home(request):
    response = {
        'DATA_SENDED': False
    }

    return render(request, 'index.html')

def password_generator(request):
    return render(request, 'passwd_gen.html')

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
