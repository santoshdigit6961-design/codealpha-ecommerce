from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Account created successfully! Please log in.')
            return redirect('accounts:login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
