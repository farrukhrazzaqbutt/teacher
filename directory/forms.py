from django.forms import ModelForm
from django import forms
from .models import register,registerAdmin

class registerForm(ModelForm):
    class Meta:
        model = register
        fields = ['email','first_name','last_name','profile_pic','phone','room_number']

class admin_registerForm(ModelForm):
    class Meta:
        model = registerAdmin
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ['username','password','email']