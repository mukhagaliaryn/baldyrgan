# Generated by Django 4.1.1 on 2022-09-25 08:47

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0004_lesson_date_created_lesson_view'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ('date_created',), 'verbose_name': 'Lesson', 'verbose_name_plural': 'Lessons'},
        ),
        migrations.AddField(
            model_name='lesson',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='class_room',
            field=models.CharField(choices=[('NOT', 'Not defined'), ('FIRST_C', '1'), ('SECOND_C', '2'), ('THIRD_C', '3'), ('FOURTH_C', '4')], default='Not defined', max_length=255, verbose_name='Class'),
        ),
    ]