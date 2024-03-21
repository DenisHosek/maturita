from django import forms


from .models import CompoundInterest, SimpleInterest

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=30, required=False)

class SimpleForm(forms.ModelForm):
    class Meta:
        model = SimpleInterest
        exclude = ["user", 'date', 'interest', 'result']

class CompoundForm(forms.ModelForm):
    class Meta:
        model = CompoundInterest
        exclude = ["user", 'date', 'interest', 'result']