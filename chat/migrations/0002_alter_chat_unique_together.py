# Generated by Django 3.2.9 on 2021-11-21 22:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='chat',
            unique_together={('student', 'teacher')},
        ),
    ]
