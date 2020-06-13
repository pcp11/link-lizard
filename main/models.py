from django.utils import timezone
from django.db import models

from main.base64 import encode


class URLMapping(models.Model):
    original_url = models.URLField()
    created = models.DateTimeField(editable=False)

    @property
    def generated_hash(self):
        id_str = str(self.id)
        return encode(id_str)

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created = timezone.now()
        return super(URLMapping, self).save(*args, **kwargs)
