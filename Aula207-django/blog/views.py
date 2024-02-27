from django.http import HttpResponse

# from django.shortcuts import render


def blogView(request):
    print('Blog')
    return HttpResponse('Blog do app 1')


def exemplo(request):
    print('Exemplo')
    return HttpResponse('Exemplo do app')
