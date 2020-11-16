from django.contrib import auth


def check_request_method_is_post(request_method):
    if request_method == 'POST':
        return True
    return False


def check_user_exists(request):
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if user:
        return True, auth.login(request, user)
    else:
        return False
