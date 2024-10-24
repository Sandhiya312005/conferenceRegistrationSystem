from django.shortcuts import render, redirect
from .models import Registration
from .forms import RegistrationForm, ContactForm

def home(request):
    return render(request, 'registration/home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def profile(request):
    registrations = Registration.objects.all()
    return render(request, 'registration/profile.html', {'registrations': registrations})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save or process the contact form data here
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'registration/contact.html', {'form': form})
