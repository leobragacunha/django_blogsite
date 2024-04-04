from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse, reverse_lazy

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NewUserForm
from .models import User

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


class UpdateProfileView(LoginRequiredMixin, generic.UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'date_of_birth', 'bio','profile_pic']
    template_name = "accounts/profile.html"

    def form_valid(self, form):
        user = self.get_object()
        form.save()
        return redirect(reverse('blog:blogger-detail', kwargs={'pk':user.pk}))


class DeleteProfileView(LoginRequiredMixin, generic.DeleteView):
    model = User
    template_name = "accounts/profile_confirm_delete.html"
    success_url = reverse_lazy('blog:bloggers')

    def form_valid(self, form):
        logout(self.request)
        return super(DeleteProfileView, self).form_valid(form)
    


