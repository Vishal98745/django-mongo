from django.contrib import admin
from .models import student
# Register your models here.


class studentAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','password','phone','is_created']

admin.site.register(student,studentAdmin)