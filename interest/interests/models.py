from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CompoundInterest(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    basis = models.FloatField()
    rate = models.DecimalField(max_digits=2, decimal_places=2, default=0)
    period = models.FloatField()
    date = models.DateField()
    result = models.DecimalField(max_digits=20,decimal_places=2)

class SimpleInterest(models.Model):
    type_choices = [
        ("p.a.","p.a."),
        ("p.s.","p.s."),
        ("p.q.","p.q."),
        ("p.m.","p.m.")
    ]

    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    basis = models.FloatField()
    rate = models.DecimalField(max_digits=2, decimal_places=2)
    type = models.CharField(choices=type_choices,max_length=4)
    days = models.FloatField()
    date = models.DateField()
    interest = models.DecimalField(max_digits=20,decimal_places=2)
    result = models.DecimalField(max_digits=20,decimal_places=2)