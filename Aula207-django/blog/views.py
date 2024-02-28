from django.shortcuts import render


def blogView(request):
    print('Blog')
    return render(
        request,
        'blog/index.html'
    )


def exemplo(request):
    print('Exemplo')
    return render(
        request,
        'blog/exemplo.html'
    )
