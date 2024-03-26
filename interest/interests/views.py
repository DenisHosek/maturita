from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CompoundForm, SimpleForm, SignupForm
from .models import CompoundInterest, SimpleInterest
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


def vyp_dnu(a, b,c,d,e,f):
    years = 0
    if c == f:
        days = (e-b) * 30 + (d-a)
    else:
        years = int(f - c)
        days = (12 -b) * 30 + (31-a) + (e-1) * 30 + (d-1)
        if years > 1:
            for i in range(years-1):
                days += 360
    return days

def index(request):
    return render(request, "index.html")

def interest(request):
    result = ""
    rate = ''
    type = ''
    basis = ''
    days = ''
    f_d = ''
    f_m = ''
    f_y = ''
    e_d = ''
    e_m = ''
    e_y = ''

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

            f_d = form.cleaned_data['first_day']
            f_m = form.cleaned_data['first_month']
            f_y = form.cleaned_data['first_year']
            e_d = form.cleaned_data['end_day']
            e_m = form.cleaned_data['end_month']
            e_y = form.cleaned_data['end_year']

            days = vyp_dnu(f_d,f_m,f_y,e_d,e_m,e_y)
            idk = choose[type]
            interest = 0
            result = round(basis*rate/100*days/idk,2)
            if request.user.is_authenticated:
                instance = form.save(commit=False)
                instance.result = result
                instance.interest = interest
                instance.user = request.user
                instance.save()
    else:
        form = SimpleForm()

    return render(request, "interest.html", {'form':form, 'result':result, 'rate':rate, 'type':type, 'base':basis, 'day':days, 'fd':f_d,'fm':f_m,'fy':f_y,'ed':e_d,'em':e_m,'ey':e_y})

def cinterest(request):
    result = ""
    basis = ''
    rate = ''
    period = ''
    fvif = ''
    if request.method == "POST":
        form = CompoundForm(request.POST)
        if form.is_valid():
            basis = form.cleaned_data['basis']
            rate = form.cleaned_data['rate']
            period = form.cleaned_data['period']


            fvif = round((1+(rate/100))**period, 2)
            result = basis * fvif
            if request.user.is_authenticated:
                instance = form.save(commit=False)
                instance.fvif = fvif
                instance.result = result
                instance.user = request.user
                instance.save()
    else:
        form = CompoundForm(request.POST)

    return render(request, "cinterest.html", {'form':form, "result":result, 'base':basis, 'rate':rate, 'fvif':fvif, 'period':period})

def singup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect("home")
    else:
        form = SignupForm()

    return render(request, "signup.html", {"form": form})

def change_pass(request):
    return render(request, "pass_change.html")

@login_required
def history(request):
    sin = SimpleInterest.objects.filter(user=request.user.id).order_by('-date')
    cin = CompoundInterest.objects.filter(user=request.user.id).order_by('-date')
    return render(request, 'history.html', {'sin':sin,'cin':cin})