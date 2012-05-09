# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login , logout
from django.template.context import RequestContext


def main_page(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/flashcard")
    return render_to_response('mainpage/index.html')

def login_page(request):
    error = 0
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/flashcard/")
            else:
                error = 1
        else:
            error = 1
    variables = RequestContext(request, {'error': error})
    return render_to_response('mainpage/login.html', variables)

def logout_page(request):
    logout(request)
    return render_to_response('mainpage/logout.html')