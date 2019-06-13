from django.urls import path
from groups.views import test, addGroup

urlpatterns = [
    path('add', addGroup),
]
