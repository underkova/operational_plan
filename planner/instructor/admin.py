from django.contrib import admin
#from .models import student
#from .models import groups
from .models import instructor
from .models import instructor_type
from .models import aircraft_type

#admin.site.register(student)  # чтобы таблица студентов была видна в админке
#admin.site.register(groups)
admin.site.register(instructor)
admin.site.register(instructor_type)
admin.site.register(aircraft_type)
from django.contrib import admin

# Register your models here.