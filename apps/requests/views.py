from django.shortcuts import render
from django.template import RequestContext
import json
from .models import Request


def requests(request):
    all_requests = Request.objects.all()
    if all_requests.count() > 10:
        q = all_requests.order_by('-date')[0:10]
        l = [i.id for i in q]
        for x in all_requests:
            if x.id not in l:
                Request.objects.filter(id=x.id).delete()
        ten_request = all_requests.order_by('-date')
    else:
        ten_request = all_requests.order_by('-date')

    return render(request, 'requests/requests.html', {'ten_request': ten_request})

