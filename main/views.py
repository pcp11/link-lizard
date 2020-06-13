from django.http import HttpResponseRedirect
from django.shortcuts import render

from main.base64 import decode
from main.models import URLMapping


def index(request):
    return render(request, 'home.html')


def success(request):
    if request.method != 'POST':
        return render(request, 'home.html')
    url_param = request.POST.get("url")
    mapping = URLMapping(original_url=url_param)
    mapping.save()
    generated_url = 'http://127.0.0.1:8000/' + mapping.generated_hash
    return render(request, 'success.html', {'original_url': url_param, 'generated_url': generated_url})


def redirect(_, generated_hash):
    mapping_id = int(decode(generated_hash))
    mapping = URLMapping.objects.get(pk=mapping_id)

    return HttpResponseRedirect(mapping.original_url)
