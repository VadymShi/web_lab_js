from django.contrib import admin
from .models import Office, Worker

class OfficeAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')

admin.site.register(Office, OfficeAdmin)

class WorkerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth_date', 'hire_date', 'profession')

admin.site.register(Worker, WorkerAdmin)
