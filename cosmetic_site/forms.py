from django import forms
from .models import Payment
from django.contrib.auth.models import User

class CardForm(forms.ModelForm):
 
    class Meta:
        model = User
        fields = ["full_name", "card_number", "expiry_date", "cvv", "zip_code"]

    def __init__(self, *args, **kwargs):
        super(CardForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['full_name'].widget.attrs['placeholder'] = "Cardholder's Name"
        self.fields['card_number'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['card_number'].widget.attrs['placeholder'] = '1234 5678 9012 3457'
        self.fields['expiry_date'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['expiry_date'].widget.attrs['placeholder'] ="MM/YYYY"
        self.fields['cvv'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['cvv'].widget.attrs['placeholder'] = '234'
        self.fields['zip_code'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['zip_code'].widget.attrs['placeholder'] = '10004'
        

    def save(self, commit=True):
        user = super(Card, self).save(commit=False)
        if commit:
            user.save()
        return user