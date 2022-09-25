from django.shortcuts import render, get_object_or_404
from .models import Lesson, Subject
from django.db.models import Q


def home(request):
    lessons = Lesson.objects.all()
    subjects = Subject.objects.all()

    if 'search' in request.GET:
        search = request.GET.get('search')
        lessons = Lesson.objects.filter(title__icontains=search)

        context = {
            'lessons': lessons,
            'subjects': subjects
        }

    if 'class-1' in request.GET:
        lessons = Lesson.objects.filter(class_room='FIRST_C')

        context = {
            'lessons': lessons,
            'subjects': subjects
        }
    if 'class-2' in request.GET:
        lessons = Lesson.objects.filter(class_room='SECOND_C')

        context = {
            'lessons': lessons,
            'subjects': subjects
        }
    if 'class-3' in request.GET:
        lessons = Lesson.objects.filter(class_room='THIRD_C')

        context = {
            'lessons': lessons,
            'subjects': subjects
        }
    if 'class-4' in request.GET:
        lessons = Lesson.objects.filter(class_room='FOURTH_C')

        context = {
            'lessons': lessons,
            'subjects': subjects
        }
    else:
        context = {
            'lessons': lessons,
            'subjects': subjects
        }
    return render(request, 'lesson/index.html', context)


def subject_detail(request, slug):
    subject = get_object_or_404(Subject, slug=slug)
    lessons = Lesson.objects.filter(subject=subject)
    subjects = Subject.objects.all()

    if 'search' in request.GET:
        search = request.GET.get('search')
        lessons = lessons.filter(title__icontains=search)

        context = {
            'subject': subject,
            'lessons': lessons,
            'subjects': subjects
        }

    if 'class-1' in request.GET:
        lessons = lessons.filter(class_room='FIRST_C')

        context = {
            'subject': subject,
            'lessons': lessons,
            'subjects': subjects
        }
    if 'class-2' in request.GET:
        lessons = lessons.filter(class_room='SECOND_C')

        context = {
            'subject': subject,
            'lessons': lessons,
            'subjects': subjects
        }
    if 'class-3' in request.GET:
        lessons = lessons.filter(class_room='THIRD_C')

        context = {
            'subject': subject,
            'lessons': lessons,
            'subjects': subjects
        }
    if 'class-4' in request.GET:
        lessons = lessons.filter(class_room='FOURTH_C')

        context = {
            'subject': subject,
            'lessons': lessons,
            'subjects': subjects
        }
    else:
        context = {
            'subject': subject,
            'lessons': lessons,
            'subjects': subjects
        }

    return render(request, 'lesson/subject_detail.html', context)
