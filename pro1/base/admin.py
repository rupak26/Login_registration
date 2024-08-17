from django.contrib import admin
from .models import login , registration , Todo
# Register your models here.
admin.site.register(login)
admin.site.register(registration)
admin.site.register(Todo)