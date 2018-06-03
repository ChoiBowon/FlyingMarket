from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from .models import Goods
# from django.contrib.auth import login
# from .forms import SignupForm
# from .forms import UserForm
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


def index(request):
    # form = UserForm()
    form = UserCreationForm()
    return render(request, 'main/index.html', {
        'form': form,
    })


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



# def signup(request):
#     if request.method == 'POST':
#         signup_form = SignupForm(request.POST)
#         if signup_form.is_valid():
#             signup_form.signup()
#             return redirect('post:post_list')
#     else:
#         signup_form = SignupForm()
#
#     context = {
#         'signup_form' : signup_form,
#     }
#     return render(request, 'registration/signup.html', context)


def signup(request):
    # if request.method == "POST":
    #     form = SignupForm(request.POST)
    #     if form.is_valid():
    #         new_user = User.objects.create_user(**form.cleaned_data)
    #         login(request, new_user)
    #         return render(request, '/', {})
    # else:
    #     form = SignupForm()
    #     return render(request, 'registration/signup.html', {'form': form})

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return render(request, 'registration/signup_ok.html', {})
    else:
        form = UserCreationForm()
    return render(request, 'main/index.html', {'form': form})
