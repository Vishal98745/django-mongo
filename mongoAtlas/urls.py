from django.contrib import admin
from django.urls import path
from mongoapp.views import Student
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Student.as_view()),
]