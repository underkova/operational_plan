from django.contrib import admin

# Register your models here.
from .models import student
from .models import group
from .models import exercise
from .models import exercise_type
from .models import briefing

admin.site.register(student)
admin.site.register(group)
admin.site.register(exercise)
admin.site.register(exercise_type)
admin.site.register(briefing)
