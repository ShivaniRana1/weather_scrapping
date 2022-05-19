from django import forms

class NameForm(forms.Form):
    city = forms.CharField(label='city_name', max_length=100,required=True)
