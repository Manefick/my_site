from django.urls import path
from students.views import addStudent

urlpatterns = [
    path('add', addStudent),
]