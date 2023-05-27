from django.contrib import admin
from .models import instructor
from .models import instructor_type
from .models import aircraft_type

class InstructorAdmin(admin.ModelAdmin):
    class Meta:
        model = instructor
    list_display = ('instructor_name', 'formatted_flight_time', 'aircraft_type', 'instructor_type')
    list_editable = ()
    def formatted_flight_time(self, obj):
        total_minutes = obj.instructor_flight_time.total_seconds() // 60
        hours = int(total_minutes // 60)
        minutes = int(total_minutes % 60)
        return f"{hours}:{minutes:}"

    formatted_flight_time.short_description = 'Общий налёт'

admin.site.register(instructor, InstructorAdmin)
admin.site.register(instructor_type)
admin.site.register(aircraft_type)
from django.contrib import admin

# Register your models here.
