from django.contrib import admin

from mainapp.models import Applicant, Feedback, Question


# Register your models here.
@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'telegram', 'phone_number', 'course', 'date']
    list_display_links = ['__str__', 'telegram', 'phone_number']
    search_fields = ['telegram', 'email', 'phone_number']
    save_on_top = True


@admin.register(Feedback)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'telegram', 'phone_number', 'date']
    list_display_links = ['first_name', 'telegram', 'phone_number']
    search_fields = ['telegram', 'first_name', 'phone_number']
    save_on_top = True


@admin.register(Question)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    list_display_links = ['__str__']
    search_fields = ['__str__', 'answer']
    save_on_top = True
