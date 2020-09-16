from django.shortcuts import render


def index(require):
    return render(require, 'contatos/index.html')
