from django.shortcuts import render, render_to_response
from django.template import RequestContext
from apps.hello.models import MyContacts
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'index.html', {'contact': MyContacts.objects.get(id=1)})

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
    if request.GET:
       return HttpResponseRedirect('/')
    return render_to_response('login.html', context_instance=RequestContext(request))

