from django.shortcuts import render, redirect
from django.http import HttpResponse
from students.models import Student


def addStudent(request):

    if request.method == 'GET':
        return HttpResponse(render(request, 'add_student.html'))
    elif request.method == 'POST':

        name = request.POST.get('name')
        surname = request.POST.get('surname')
        avg_mark = request.POST.get('avg_mark')
        group_id = request.POST.get('group_id')

        if int(avg_mark) > 9:
            group_id = 2

        student = Student()

        student.name = name
        student.surname = surname
        student.avg_mark = avg_mark
        student.group_id = group_id

        student.save()

    return redirect('/groups/all')