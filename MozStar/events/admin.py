from django.contrib import admin
from .models import Event

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('eid', 'title', 'event_start_date', 'event_end_date',
                    'link', 'venue', 'registration_form_link', 'is_published')

admin.site.register(Event, EventAdmin)
