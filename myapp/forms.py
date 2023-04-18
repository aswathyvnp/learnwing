from django import forms
from .models import OtherModel

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):       
        model=User
        fields=['username','email','password1','password2']



class OtherModelForm(forms.ModelForm):
    class Meta:
        model = OtherModel
        fields = ['image','dateOfBirth']
