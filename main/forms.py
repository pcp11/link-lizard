from django.core.validators import URLValidator
from django.forms import ModelForm, TextInput, CharField

from main.models import URLMapping


class URLMappingForm(ModelForm):
    original_url = CharField(validators=[URLValidator()], widget=TextInput(
        attrs={"id": "original_url", "class": "form-control", "placeholder": "Enter your link"}))
    generated_hash = CharField(required=False, widget=TextInput(
        attrs={"id": "generated_hash", "class": "form-control", "placeholder": "Custom Alias (Optional)"}))

    class Meta:
        model = URLMapping
        fields = ('original_url', 'generated_hash')
