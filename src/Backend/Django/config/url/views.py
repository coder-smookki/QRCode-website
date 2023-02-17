from django.http import HttpResponse
from django.shortcuts import render
import json
from . import check_url
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def processing_url(request):
    global res
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        if isinstance(data, dict):
            url = data.get('url', None)
            if url is not None:
                res = check_url.check_link(url)
        else:
            return f'Link verification error'

    return HttpResponse(res)
