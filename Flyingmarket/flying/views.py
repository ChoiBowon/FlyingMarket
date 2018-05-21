from django.shortcuts import render
from .models import Flying

def index(request):
    flying_list = Flying.objects.filter(is_matched=False)
    context = {
        'flying_list': flying_list,
    }
    return render(request, 'flying/flying.html', context)