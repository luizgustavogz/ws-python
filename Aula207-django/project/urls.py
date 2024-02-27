"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# HTTP Request <-> HTTP Response:
# É um protocolo de comunicação entre Cliente e Servidor
# Cliente faz a Request (Requisição) <-> Servidor devolve a Response (Resposta)
# Django funciona no MVT (Model View Template), variação do MVC (Model View Controller)


def home(request):
    print('HOME')
    return HttpResponse('HOME')


def blog(request):
    print('BLOG')
    return HttpResponse('BLOG')


urlpatterns = [
    path('', home),  # Nenhuma URL começa com "/"
    path('blog/', blog),
    path('admin/', admin.site.urls),
]
