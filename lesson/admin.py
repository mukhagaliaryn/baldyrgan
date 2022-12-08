from django.contrib import admin
from .models import Subject, Lesson, Task
from django.contrib.auth.models import Group


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', )
    search_fields = ('title',)


class TaskTabularInline(admin.TabularInline):
    model = Task
    extra = 1


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'class_room', 'subject', 'view', 'is_public', 'date_created',)
    search_fields = ('title',)

    inlines = [TaskTabularInline, ]


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.unregister(Group)
