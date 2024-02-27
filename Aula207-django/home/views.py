from django.http import HttpResponse

# from django.shortcuts import render


def homeView(request):
    print('Home')
    return HttpResponse('Home do app')
