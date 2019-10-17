from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import redirect, render

from .forms import UserLookup
from .models import User

# def index(request):
#     user_list = User.objects.all()
#     template = 'userlookup/index.html'
#     context = {
#         'user_list': user_list,
#         'form': UserLookup()
#     }
#     form = UserLookup()
#     return render(request, template, context)

def index(request):
    user_list = []
    template = 'userlookup/index.html'

    if request.method == 'POST':
        form = UserLookup(request.POST)
        if form.is_valid(): 
            name = form.cleaned_data['name']
            user_list = User.objects.filter(name__contains=name)

            context = {
                'user_list': user_list,
                'form': UserLookup()
            }

            return render(request, template, context)
    else:
        if 'show_all' in request.GET:
            user_list = User.objects.all()
            context = {
                'user_list': user_list,
                'form': UserLookup()
            }
            return render(request, template, context)
        else:
            context = {
                'user_list': user_list,
                'form': UserLookup()
            }
            return render(request, template, context)