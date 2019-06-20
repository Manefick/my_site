from django.urls import path
from students.views import addStudent, search

urlpatterns = [
    path('add', addStudent),
    path('search', search),
]