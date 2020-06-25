from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.info(request, f'Your  account has been created! You are now able to log in')
            return redirect('login')
    else:
        form =UserRegistrationForm()
    return render(request, 'user_info/register.html', {'form': form})

@login_required()
def profile(request):
    return render(request, 'user_info/profile.html')

