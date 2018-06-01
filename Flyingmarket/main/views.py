from django.shortcuts import render, get_object_or_404
from .models import Goods


def index(request):
    return render(request, 'main/index.html', {})


def goods(request):
    goods_list = Goods.objects.all
    context = {
        'goods_list' : goods_list
    }
    return render(request, 'main/goods.html', context)


def goods_detail(request, goods_id):
    goods = get_object_or_404(Goods, pk=goods_id)
    context = {
        'Goods': goods,
    }
    return render(request, 'main/goods_detail.html', context)
