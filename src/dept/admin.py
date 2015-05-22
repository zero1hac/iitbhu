from django.contrib import admin

# Register your models here.
from .models import department,faculty,student,staff,notification,course,gallery,image


class deptAdmin(admin.ModelAdmin):
    class Meta:
        model = department
        model = faculty
        model = student
        model = staff
        model = notification
        model = course
        model = gallery
        model = image
        
admin.site.register(department, deptAdmin)
admin.site.register(faculty, deptAdmin)
admin.site.register(student, deptAdmin)
admin.site.register(staff, deptAdmin)
admin.site.register(notification, deptAdmin)
admin.site.register(course, deptAdmin)
admin.site.register(gallery, deptAdmin)
admin.site.register(image, deptAdmin)