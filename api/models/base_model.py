# abstract base model

from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True
        ordering = ('-created_at', '-last_modified')
        get_latest_by = 'created_at'
    
    def __save__(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)