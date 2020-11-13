from django.contrib import auth


def check_request_method_is_post(request_method):
    if request_method == 'POST':
        return True
    return False


def creates_user(request, username, password):
    user = auth.authenticate(request, username=username, password=password)
