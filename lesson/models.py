from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


class Subject(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    slug = models.SlugField(verbose_name=_('Subject slug'), max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Subject')
        verbose_name_plural = _('Subjects')


class Lesson(models.Model):
    CLASS = (
        ('NOT', _('Not defined')),
        ('FIRST_C', _('1')),
        ('SECOND_C', _('2')),
        ('THIRD_C', _('3')),
        ('FOURTH_C', _('4')),
    )

    title = models.CharField(verbose_name=_('Title'), max_length=255)
    slug = models.SlugField(verbose_name=_('Lesson slug'), max_length=255)
    class_room = models.CharField(verbose_name=_('Class'), choices=CLASS, default=CLASS[0][1], max_length=255)
    content = RichTextField(verbose_name=_('Content'), blank=True, null=True)
    subject = models.ForeignKey(Subject, verbose_name=_('Subject'), on_delete=models.CASCADE)
    view = models.PositiveIntegerField(verbose_name=_('View'), default=0)
    date_created = models.DateField(verbose_name=_('Date created'), auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Lesson')
        verbose_name_plural = _('Lessons')
        ordering = ('-date_created',)


class Task(models.Model):
    title = models.CharField(verbose_name=_('Document title'), max_length=255)
    file = models.FileField(verbose_name=_('File'), upload_to='lesson/docs/', blank=True, null=True)
    lesson = models.ForeignKey(Lesson, verbose_name=_('Lesson'), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')
