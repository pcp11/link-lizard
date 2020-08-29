import json

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from nanoid import generate

from main.forms import URLMappingForm
from main.models import URLMapping


def index(request):
    if request.method == 'POST':
        form = URLMappingForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            generated_hash = form.cleaned_data['generated_hash'] \
                if form.cleaned_data['generated_hash'] \
                else generate(size=5)

            mapping = URLMapping(original_url=original_url, generated_hash=generated_hash)
            mapping.save()

            base_url = request.META['HTTP_ORIGIN'] + "/"
            generated_url = base_url + mapping.generated_hash

            return HttpResponse(json.dumps({"original_url": original_url, "generated_url": generated_url}))
        else:
            return HttpResponse(json.dumps({"errors": form.errors}))
    else:
        form = URLMappingForm()
    return render(request, 'home.html', {"form": form})


def redirect(_, generated_hash):
    mapping = get_object_or_404(URLMapping, generated_hash=generated_hash)
    return HttpResponseRedirect(mapping.original_url)
