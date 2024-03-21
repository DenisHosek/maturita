from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from .forms import CompoundForm, SimpleForm

def index(request):
    return render(request, "index.html")

def interest(request):
    if request.method == "POST":
        form = SimpleForm(request.POST)
        choose = {"p.a.":360,
                  "p.s.":180,
                  "p.q.":90,
                  "p.m.":30}
        if form.is_valid():
            basis = form.cleaned_data['basis']
            rate = form.cleaned_data['rate']
            type = form.cleaned_data['type']
            days = form.cleaned_data['days']
            idk = choose[type]
            result = basis*rate/100*days/idk
            #if request.user.is_authenticated:
    else:
        form = SimpleForm(request.POST)

    return render(request, "interest.html", {'form':form, 'result':result})

def cinterest(request):
    if request.method == "POST":
        form = CompoundForm(request.POST)
        if form.is_valid():
            basis = form.cleaned_data['basis']
            rate = form.cleaned_data['rate']
            period = form.cleaned_data['period']

            fvif = (1+(rate/100))**period
            result = basis * fvif
            #if request.user.is_authenticated:
            return redirect (request, "result.html", {'result':result})
    else:
        form = CompoundForm(request.POST)

    return render(request, "interest.html", {'form':form})

def singup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect("home")
    else:
        form = UserCreationForm()

    return render(request, "signup.html", {"form": form})

def change_pass(request):
    return render(request, "pass_change.html")

