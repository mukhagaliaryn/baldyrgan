from django.shortcuts import render, get_object_or_404
from .models import Lesson, Subject, Task


def index(request):
    print(request.path)

    return render(request, 'index.html', {})


def home(request):
    lessons = Lesson.objects.filter(is_public=True)
    subjects = Subject.objects.all()

    if 'search' in request.GET:
        search = request.GET.get('search')
        lessons = Lesson.objects.filter(is_public=True, title__icontains=search)

        context = {
            'lessons': lessons,
            'subjects': subjects
        }

    if 'class-1' in request.GET:
        lessons = Lesson.objects.filter(is_public=True, class_room='FIRST_C')

        context = {
            'lessons': lessons,
            'subjects': subjects
        }
    if 'class-2' in request.GET:
        lessons = Lesson.objects.filter(is_public=True, class_room='SECOND_C')

        context = {
            'lessons': lessons,
            'subjects': subjects
        }
    if 'class-3' in request.GET:
        lessons = Lesson.objects.filter(is_public=True, class_room='THIRD_C')

        context = {
            'lessons': lessons,
            'subjects': subjects
        }
    if 'class-4' in request.GET:
        lessons = Lesson.objects.filter(is_public=True, class_room='FOURTH_C')

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


# ======================================================================
def subject_detail(request, slug):
    subject = get_object_or_404(Subject, slug=slug)
    lessons = Lesson.objects.filter(subject=subject, is_public=True)
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


# ======================================================================
def lesson_detail(request, slug):
    lesson = get_object_or_404(Lesson, slug=slug)
    lessons = Lesson.objects.filter(subject=lesson.subject, class_room=lesson.class_room)
    lesson.view = lesson.view + 1
    lesson.save()
    task_list = Task.objects.filter(lesson=lesson)

    context = {
        'lesson': lesson,
        'lessons': lessons,
        'tasks': task_list
    }

    return render(request, 'lesson/lesson_detail.html', context)


# ========================================================================
def tasks(request, slug):
    lesson = get_object_or_404(Lesson, slug=slug)
    task_list = Task.objects.filter(lesson=lesson)
    lessons = Lesson.objects.filter(subject=lesson.subject, class_room=lesson.class_room)

    context = {
        'lesson': lesson,
        'lessons': lessons,
        'tasks': task_list
    }
    return render(request, 'lesson/tasks.html', context)
