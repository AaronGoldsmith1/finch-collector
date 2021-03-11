from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

from .models import Finch, Toy
from .forms import FeedingForm, FinchForm


# Create your views here.

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('finches_index')
        else:
            error_message = 'Invalid sign up - try again'
    # A GET or a bad POST request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


@ login_required
def finches_index(request):
    finches = Finch.objects.filter(user=request.user)
    return render(request, 'finches/index.html', {'finches': finches})


@ login_required
def finches_new(request):
    finch_form = FinchForm(request.POST or None)
    if request.POST and finch_form.is_valid():
        new_finch = finch_form.save(commit=False)
        new_finch.user = request.user
        new_finch.save()
        return redirect('finches')
    else:
        return render(request, 'finches/new.html', {'finch_form': finch_form})


@ login_required
def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    toys_finch_doesnt_have = Toy.objects.exclude(id__in=finch.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {
        'finch': finch,
        'feeding_form': feeding_form,
        'toys': toys_finch_doesnt_have
    })


@ login_required
def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)


@ login_required
def assoc_toy(request, finch_id, toy_id):
    # Note that you can pass a toy's id instead of the whole object
    Finch.objects.get(id=finch_id).toys.add(toy_id)
    return redirect('detail', finch_id=finch_id)
