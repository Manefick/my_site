from django.urls import path
from groups.views import test

urlpatterns = [
    path('', test),
]
