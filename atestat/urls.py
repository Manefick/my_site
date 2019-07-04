from django.urls import path
from atestat.views import addAtestat, sortSudents

urlpatterns = [
    path('add', addAtestat),
    path('sort', sortSudents)
]