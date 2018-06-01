from django.urls import path
from . import views

app_name = 'flying'
urlpatterns = [
    path('', views.index, name='flying'),
    path('<int:flying_id>', views.detail, name='flying_detail'),
]