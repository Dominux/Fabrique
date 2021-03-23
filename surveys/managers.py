from django.db.models.expressions import F
from django.utils import timezone
from .models import Survey
from django.db import models


class SurveyManager(models.Manager):
    def active(self):
        now = timezone.now()
        return self.filter(
            start_date__gt=now,
            end_date__lt=now
        )

