from django.shortcuts import render
from .models import Want



def index(request):
    want_list = Want.objects.filter(is_matched=False)
    context = {
        'want_list': want_list,
    }
    return render(request, 'want/want.html', context)