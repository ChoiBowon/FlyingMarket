from django.shortcuts import render, get_object_or_404
from .models import Want



def index(request):
    want_list = Want.objects.filter(is_matched=False)
    context = {
        'want_list': want_list,
    }
    return render(request, 'want/want.html', context)


def detail(request, want_id):
    want = get_object_or_404(Want, pk=want_id)
    context = {
        'Want': want,
    }
    return render(request, 'want/want_detail.html', context)
