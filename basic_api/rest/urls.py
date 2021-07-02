from django.urls import path
from django.contrib import admin

from restapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu/', views.studentapi),
]
