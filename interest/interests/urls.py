from django.urls import path
from django.contrib.auth import views as vie

from . import views as vm

urlpatterns = [
    path("", vm.index, name="home"),
    path("logout/", vie.LogoutView.as_view(template_name='index.html'), name='logout'),
    path('account/', vie.PasswordChangeView.as_view(template_name='account.html'), name='account'),
    path('account/pass/', vm.change_pass, name='password_change_done'),
    path("register/", vm.singup, name="register"),
    path("login/", vie.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path("interest/", vm.interest, name="interest"),
    path("cinterest/", vm.cinterest, name="cinterest"),
    path('history/', vm.history, name="history"),
    #path('account/', vm.PasswordsChangeView.as_view(template_name='account.html'), name='account'),
]