import json
from datetime import datetime,timedelta
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
            {"hour":"2012-06-21-14", "avg_resp_time":"127.5", "hits":"5809"},
            {"hour":"2012-06-21-15", "avg_resp_time":"0.5", "hits":"2"},
            {"hour":"2012-06-21-8", "avg_resp_time":"60", "hits":"1000"}
            ]
    }"""

    page = {'page': []}

    for offset in range(30,-1,-1):
        this_date = datetime.today() - timedelta(days=offset)

        for newhour in range(24):
            container = {}
	    this_date = this_date.replace(hour=newhour, minute=0, second=0)
            container['hour'] = this_date.isoformat()# + '-' + str(hour)
            container['avg_resp_time'] = '%.2f' % (random()*100)
            container['hits'] = str(randint(1,1000))
            page['page'].append(container)

    return HttpResponse(json.dumps(page))
