from django.shortcuts import render


def homeView(request):
    print('Home')
    return render(
        request,
        'home/index.html'
    )
