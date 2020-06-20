from django.forms import ModelForm
from .models import register

class registerForm(ModelForm):
    class Meta:
        model = register
        fields = ['email','first_name','last_name','profile_pic','phone','room_number']