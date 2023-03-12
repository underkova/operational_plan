from django.contrib import admin

# Register your models here.
from .models import students
from .models import groups
from .models import exercise
from .models import exercise_types

admin.site.register(students)
admin.site.register(groups)
admin.site.register(exercise)
admin.site.register(exercise_types)
