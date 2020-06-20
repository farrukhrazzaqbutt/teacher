from django.contrib import admin

# Register your models here.
from .models import register,subject_detail,registerAdmin

admin.site.register(register)
admin.site.register(subject_detail)
admin.site.register(registerAdmin)