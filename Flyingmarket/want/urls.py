from django.urls import path
from . import views

app_name = 'want'
urlpatterns = [
    path('', views.index, name='want'),
]