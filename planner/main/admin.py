from django.contrib import admin
from .models import students
from .models import groups
from .models import instructors
from .models import instructor_type

admin.site.register(students) #чтобы таблица студентов была видна в админке
admin.site.register(groups)
admin.site.register(instructors)
admin.site.register(instructor_type)
# Register your models here.
