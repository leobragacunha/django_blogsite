from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth import login, authenticate

from .forms import NewUserForm

# Create your views here.

def signUpView(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(request, username=username, password=password)
            login(request, user)

            return redirect('home')
    
    else:
        form = NewUserForm()

    return render(request, "accounts/signup.html", {'form':form})


