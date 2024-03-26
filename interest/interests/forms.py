from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import CompoundInterest, SimpleInterest
from django.contrib.auth.models import User


class DateInput(forms.DateInput):
    input_type = "date"

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=30, required=False)

class SimpleForm(forms.ModelForm):
    class Meta:
        type_choices = [
            ("p.a.","p.a."),
            ("p.s.","p.s."),
            ("p.q.","p.q."),
            ("p.m.","p.m.")
        ]
        model = SimpleInterest
        labels = {
            "basis": "Počáteční jistina",
            "rate":"Úroková sazba",
            'type':"Úrokovací období",
        }
        exclude = ["user", 'interest', 'result']
        field = '__all__'
        widgets = {
            "basis" : forms.TextInput(attrs={"class":"form-control", 'placeholder':'Počáteční jistina'}),
            "rate" : forms.TextInput(attrs={"class":"form-control", 'placeholder':'Úroková sazba'}),
            'first_day':forms.TextInput(attrs={"class":"form-control", 'placeholder':'dd'}),
            'first_month':forms.TextInput(attrs={"class":"form-control", 'placeholder':'mm'}) ,
            'first_year':forms.TextInput(attrs={"class":"form-control", 'placeholder':'yyyy'}),
            'end_day':forms.TextInput(attrs={"class":"form-control", 'placeholder':'dd'}),
            'end_month':forms.TextInput(attrs={"class":"form-control", 'placeholder':'mm'}),
            'end_year':forms.TextInput(attrs={"class":"form-control ", 'placeholder':'yyyy'}),
            'type': forms.Select(attrs={'class': "form-select"})
        }

class CompoundForm(forms.ModelForm):
    class Meta:
        model = CompoundInterest
        exclude = ["user", 'fvif', 'result']
        labels = {
            "basis": "Počáteční jistina",
            "rate":"Úroková sazba",
            "period":"Počet období"
        }
        widgets = {
            "basis" : forms.TextInput(attrs={"class":"form-control", 'placeholder':'Počáteční jistina'}),
            "rate" : forms.TextInput(attrs={"class":"form-control", 'placeholder':'Úroková sazba'}),
            "period" : forms.TextInput(attrs={"class":"form-control", 'placeholder':'Počet období'}),
        }

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'Uživatelské jméno'
        self.fields['username'].widget.attrs['class']="form-control"
        self.fields['password1'].widget.attrs['placeholder'] = 'Heslo'
        self.fields['password1'].widget.attrs['class']="form-control"
        self.fields['password2'].widget.attrs['placeholder'] = 'Potvrzení hesla'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

