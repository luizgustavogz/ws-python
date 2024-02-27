from django.urls import path

from . import views

# blog/
urlpatterns = [
    path('', views.blogView),
    path('exemplo/', views.exemplo),
]
