from django.urls import path

from . import views

app_name = 'gv250'
urlpatterns = [
    path('', views.index, name='index'),
]
