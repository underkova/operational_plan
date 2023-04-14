from django.contrib import admin

# Register your models here.
from .models import student, group, exercise, exercise_type, briefing

class ExerciseAdmin(admin.ModelAdmin):
    class Meta:
        model = exercise
    list_display = ('exercise_code', 'total_time', 'instrument_time', 'approaches', 'landings', 'solo_time', 'night_time', 'PIC_time', 'copilot_time',
                    'PIC_night_time', 'equivalent')
    list_editable = ('total_time', 'instrument_time', 'approaches', 'landings', 'equivalent', 'night_time', 'copilot_time', 'solo_time', 'PIC_time'
                    ,'PIC_night_time',)

admin.site.register(student)
admin.site.register(group)
admin.site.register(exercise, ExerciseAdmin)
admin.site.register(exercise_type)
admin.site.register(briefing)
