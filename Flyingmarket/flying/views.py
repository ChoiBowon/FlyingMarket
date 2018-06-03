from django.shortcuts import render, get_object_or_404, redirect
from .models import Flying
from main.models import Country
from .forms import FlyingUploadForm


def index(request):
    flying_list = Flying.objects.filter(is_matched=False)
    context = {
        'flying_list': flying_list,
    }
    return render(request, 'flying/flying.html', context)


def detail(request, flying_id):
    flying = get_object_or_404(Flying, pk=flying_id)
    country = get_object_or_404(Country, pk=flying.country_id)
    context = {
        'Flying': flying,
        'Country': country,
    }
    return render(request, 'flying/flying_detail.html', context)


def regist(request):
    if request.method == 'POST':
        form = FlyingUploadForm(request.POST, request.FILES)
        #title = request.POST['title']
        #content = request.POST['content']
        # thumbnail = request.FILES['thumbnail']
        #choice = request.POST['publish']
        if form.is_valid():
            temp = form.save(commit=False)
            temp.user = request.user
            temp.save()
            #title = form.cleaned_data['title']
            #content = form.cleaned_data['content']

            #if choice == 'yes':
            #    publish = True
            #else:
            #    publish = False
            #blog = Blog.objects.create(
            #    title=title,
            #    content=content,
            #    # thumbnail=thumbnail,
             #   is_published = publish,
            #)
            return redirect('/')
        else:
            여기아닌데

    else:
        form = FlyingUploadForm()
        return render(request, 'flying/flying_regist.html', {
            'form': form
        })

