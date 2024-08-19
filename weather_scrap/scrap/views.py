from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm
from .scrap import *
from .weather import *


def input(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            data = form.cleaned_data
            data = country(data['city'])
            wea = description(data)
            
            return render(request, 'show.html', {'form': form,'data':wea})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'home.html', {'form': form})

def home(request):
    return HttpResponseRedirect('/')
    