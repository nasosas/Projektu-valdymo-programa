from django.contrib import admin
from .models import Task, Invoice, Employee, Client, Project

class ClientAdmin(admin.ModelAdmin):
    list_display = ('f_name', 'l_name', 'company', 'contacts')
    search_fields = ('f_name', 'l_name', 'company')

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'info')

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('date', 'sum')
    search_fields = ('date', 'sum')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('f_name', 'l_name', 'job')
    search_fields = ('f_name', 'l_name', 'job')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'client')
    list_filter = ('name', 'client')
    search_fields = ('user', 'name')

admin.site.register(Task, TaskAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Project, ProjectAdmin)
