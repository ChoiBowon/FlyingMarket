from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='home'),
    path('goods/', views.goods, name='goods'),
    path('goods/<int:goods_id>', views.goods_detail, name='goods_detail'),
]