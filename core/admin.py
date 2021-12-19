from django.contrib import admin
from core.models import User, ActivationCode, StudentNote

admin.site.register(User)
admin.site.register(ActivationCode)
admin.site.register(StudentNote)
