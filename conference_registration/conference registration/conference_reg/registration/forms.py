from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['first_name', 'last_name', 'date_of_birth', 'nationality', 
                  'institution', 'department', 'address', 'country', 'email', 
                  'mobile_number', 'paper_type', 'paper_id']

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
