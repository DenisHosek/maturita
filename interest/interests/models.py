from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



# Create your models here.

class CompoundInterest(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    basis = models.DecimalField(max_digits=20,decimal_places=2)
    rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    period =models.PositiveIntegerField()
    fvif = models.DecimalField(max_digits=30, decimal_places=2)
    result = models.DecimalField(max_digits=20,decimal_places=2)
    date = models.DateField(auto_now_add=True)

class SimpleInterest(models.Model):
    type_choices = [
        ("p.a.","p.a."),
        ("p.s.","p.s."),
        ("p.q.","p.q."),
        ("p.m.","p.m.")
    ]

    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    basis = models.DecimalField(max_digits=20,decimal_places=2)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    first_day = models.DecimalField(max_digits=2, decimal_places=0)
    first_month = models.DecimalField(max_digits=2, decimal_places=0)
    first_year = models.DecimalField(max_digits=5, decimal_places=0)
    end_day = models.DecimalField(max_digits=2, decimal_places=0)
    end_month = models.DecimalField(max_digits=2, decimal_places=0)
    end_year = models.DecimalField(max_digits=5, decimal_places=0)
    interest = models.DecimalField(max_digits=20,decimal_places=2)
    result = models.DecimalField(max_digits=20,decimal_places=2)
    type = models.CharField(choices=type_choices,max_length=4)
    date = models.DateField(auto_now_add=True)