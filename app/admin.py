from django.contrib import admin
from .models import Management, Students, Lecturers

# Register your models here.

class ManagemantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'profession', 'date_of_employment')

class LecturersAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subjects_taught', 'salary', 'level_of_expertise', 'years_of_experience')

class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'year_level', 'academic_level', 'description')

admin.site.register(Management, ManagemantAdmin)
admin.site.register(Students, StudentsAdmin)
admin.site.register(Lecturers, LecturersAdmin)