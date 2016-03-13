from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('eid', 'title', 'event_start_date', 'event_end_date',
                  'link', 'description', 'venue', 'registration_form_link',
                  'event_image_link')

