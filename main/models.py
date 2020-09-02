from django.core.validators import URLValidator, RegexValidator
from django.db import models
from django.utils import timezone


class URLMapping(models.Model):
    original_url = models.TextField(blank=False, validators=[URLValidator()])
    generated_hash = models.TextField(
        blank=False, unique=True, db_index=True,
        validators=[RegexValidator(regex='^[a-zA-Z0-9_]+$',
                                   message="Hash should be a combination of letters and numbers.")])
    created = models.DateTimeField(editable=False)

    # pylint: disable=signature-differs
    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created = timezone.now()
        super().save(*args, **kwargs)
