from django.contrib import admin

from .models import SimpleInterest, CompoundInterest
# Register your models here.

@admin.register(SimpleInterest)
class InterestAdmin(admin.ModelAdmin):
    pass




@admin.register(CompoundInterest)
class CinterestAdmin(admin.ModelAdmin):
    pass