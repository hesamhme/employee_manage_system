from django.contrib import admin
from .models import Employee, Penalty

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'position', 'salary']
    list_filter = ['manager']
    search_fields = ['name', 'position']


@admin.register(Penalty)
class PenaltyAdmin(admin.ModelAdmin):
    list_display = ['fee', ]

    

