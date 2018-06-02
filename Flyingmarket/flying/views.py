from django.shortcuts import render, get_object_or_404, redirect
from .models import Flying



def index(request):
    flying_list = Flying.objects.filter(is_matched=False)
    context = {
        'flying_list': flying_list,
    }
    return render(request, 'flying/flying.html', context)


def detail(request, flying_id):
    flying = get_object_or_404(Flying, pk=flying_id)
    context = {
        'Flying': flying,
    }
    return render(request, 'flying/flying_detail.html', context)
