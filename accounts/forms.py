from django import forms

from .models import User
from django.contrib.auth.forms import UserCreationForm

class NewUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','email','password1','password2','first_name','last_name',
                  'date_of_birth','bio', 'profile_pic')