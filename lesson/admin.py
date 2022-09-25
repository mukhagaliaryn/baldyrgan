from django.contrib import admin
from .models import Subject, Lesson
from django.contrib.auth.models import Group


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', )
    search_fields = ('title',)


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'class_room', 'subject', 'view', 'date_created',)
    search_fields = ('title',)


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.unregister(Group)
