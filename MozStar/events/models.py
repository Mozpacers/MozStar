from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db import models

# Custom validators
def validate_future_events(value):
    '''
    Ensures event_start_date and event_end_date are in future
    '''
    if value < timezone.now():
        raise ValidationError(u'%s is not a future date!' % value)

# Create your models here.
class Event(models.Model):
    '''
    Denotes event to be displayed on mozpacers.org
    '''
    eid = models.AutoField(primary_key=True, blank=True, editable=False)
    title = models.CharField(max_length=100)
    event_start_date = models.DateTimeField(validators=[validate_future_events])
    event_end_date = models.DateTimeField(validators=[validate_future_events])
    link = models.URLField()
    description = models.TextField(max_length=1000)
    venue = models.CharField(max_length=500)
    registration_form_link = models.URLField()
    event_image_link = models.URLField()
    is_published = models.BooleanField(default=False)

    def clean(self):
        if self.event_start_date > self.event_end_date:
            raise ValidationError('Start date cannot precede end date')
