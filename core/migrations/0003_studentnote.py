# Generated by Django 3.2.9 on 2021-12-05 23:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_activationcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=500)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_students_notes', to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students_notes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('student', 'teacher')},
                'index_together': {('student', 'teacher')},
            },
        ),
    ]
