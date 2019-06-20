from django.shortcuts import render, redirect
from django.http import HttpResponse
from groups.models import Group
from students.models import Student

def showGroups(request):
    return HttpResponse(render(request, 'all_group.html', {'groups': Group.objects.all(), 'students': Student.objects.values()}))

def addGroup(request):

    if request.method == 'GET':
        return HttpResponse(render(request, 'add_group.html'))
    elif request.method == 'POST':

        name = request.POST.get('name')
        start_date = request.POST.get('startDate')
        max_students = request.POST.get('maxStudents')

        group = Group()

        group.name = name
        group.start_date = start_date
        group.max_students = max_students

        group.save()

    return redirect('/groups/all')
