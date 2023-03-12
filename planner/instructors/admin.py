from django.contrib import admin
#from .models import students
#from .models import groups
from .models import instructors
from .models import instructor_type
from .models import aircraft_types

#admin.site.register(students)  # чтобы таблица студентов была видна в админке
#admin.site.register(groups)
admin.site.register(instructors)
admin.site.register(instructor_type)
admin.site.register(aircraft_types)
from django.contrib import admin

# Register your models here.
