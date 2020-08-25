from django.shortcuts import render
from . import forms
from testapp.models import input_movie
# Create your views here.

def home(request):
    return render(request, 'testapp/home.html')

def movies_view(request):
    return render(request, 'testapp/movies.html')

def inputmovie_view(request):
    form = forms.Input_Form()
    if request.method == 'POST':
        form = forms.Input_Form(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request, 'testapp/inputmovie.html', {'form':form})

def listmovie_view(request):
    moviedata = input_movie.objects.all()
    return render(request, 'testapp/list.html',{'data': moviedata})

def register_view(request):
    return render(request, 'testapp/register.html')