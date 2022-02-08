from django import forms

class SubmitDrill(forms.Form):
    submit = forms.CharField(label='submit', max_length=50)
