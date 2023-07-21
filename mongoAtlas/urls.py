from django.contrib import admin
from django.urls import path
from mongoapp.views import Student
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Student.as_view()),
]

urlpatterns += staticfiles_urlpatterns()