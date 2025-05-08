from django.contrib import admin
from task.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'start_date', 'updated_at', 'end_date', 'status')
    list_filter = ('status',)
    search_fields = ('name', 'description')
    ordering = ('-start_date',)
    date_hierarchy = 'start_date'
    list_per_page = 10
    list_editable = ('status',)

admin.site.register(Task, TaskAdmin)