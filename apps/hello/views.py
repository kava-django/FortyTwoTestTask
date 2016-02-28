from django.shortcuts import render
from django.template import RequestContext
from apps.hello.models import MyContacts


def index(request):
    return render(request, 'index.html', {'contact': MyContacts.objects.get(id=1)})

