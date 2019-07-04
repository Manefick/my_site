from django.shortcuts import render, redirect
from django.http import HttpResponse
from atestat.models import Atestat
from students.models import Student


def addAtestat(request):

    if request.method == 'GET':
        return HttpResponse(render(request, 'atestat.html', {'values': Student.objects.values() }))
    elif request.method == 'POST':

        name_subject = request.POST.get('name')
        mark = request.POST.get('mark')
        date = request.POST.get('date')
        student_id = request.POST.get('student_id')

        print(name_subject)

        atestat = Atestat()

        atestat.name_subject = name_subject
        atestat.mark = mark
        atestat.date = date
        atestat.student_id = student_id

        atestat.save()

        # a = sorted(Atestat.objects.all(), key=lambda atestat: atestat.mark)

    return redirect('/groups/all')

def sortSudents(request):

    return HttpResponse(render(request, 'sort_mark.html',
                               {'atestats': sorted(Atestat.objects.all(), key=lambda atestat: atestat.mark) }))