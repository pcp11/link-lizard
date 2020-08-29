from django.core.validators import URLValidator
from django.db import models
from django.utils import timezone


class URLMapping(models.Model):
    original_url = models.TextField(blank=False, validators=[URLValidator()])
    generated_hash = models.TextField(blank=False, unique=True, db_index=True)
    created = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created = timezone.now()
        return super(URLMapping, self).save(*args, **kwargs)
