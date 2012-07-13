import json
from random import random,randint
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def index(request):
    return render_to_response("index.html", 
                              {},
                              context_instance=RequestContext(request))

def index_ajax(request):
    """Return random AJAX data in the format:
    {
        "page":[
            {"hour":"14", "avg_resp_time":"127.5", "hits":"5809"},
            {"hour":"1", "avg_resp_time":"0.5", "hits":"2"},
            {"hour":"8", "avg_resp_time":"60", "hits":"1000"}
            ]
    }"""

    page = {'page': []}

    for i in range(24):
        container = {}
        container['hour'] = str(i)
        container['avg_resp_time'] = '%.2f' % (random()*100)
        container['hits'] = str(randint(1,1000))
        page['page'].append(container)

    return HttpResponse(json.dumps(page))
