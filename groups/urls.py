from django.urls import path
from groups.views import showGroups, addGroup

urlpatterns = [
    path('add', addGroup),
    path('all', showGroups),
]
