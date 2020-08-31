from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from nanoid import generate

from main.forms import URLMappingForm
from main.models import URLMapping


def index(request):
    """
    Index view for handling form data and generating shortened URLs
    """
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

            return JsonResponse({"original_url": original_url, "generated_url": generated_url})

        return JsonResponse({"errors": form.errors})

    form = URLMappingForm()
    return render(request, 'home.html', {"form": form})


def redirect(_, generated_hash):
    """
    Redirect to the original URL which belongs to the hash
    """
    mapping = get_object_or_404(URLMapping, generated_hash=generated_hash)
    return HttpResponseRedirect(mapping.original_url)
