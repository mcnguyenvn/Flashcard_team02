# Create your views here.

from django.contrib.auth.models import User
from django.http import HttpResponse , Http404, HttpResponseRedirect
from django.template import Context
from django.template import RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.signals import user_logged_in , user_logged_out

def register(request):

    state = "Đăng kí"
    username = email = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password1')
        email    = request.POST.get('email1')

        user = User.objects.create_user(username, email, password)

        user.save()

        return HttpResponseRedirect('../regis_success')

    variables=Context({
        'state' : state,
    }
    )

    return render_to_response('regis.html',variables,context_instance=RequestContext(request))

def regis_success(request):

    return render_to_response('regis_succes.html')




