# Create your views here.

from django.contrib.auth.models import User
from django.http import HttpResponse , Http404, HttpResponseRedirect
from django.template import Context
from django.template import RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.signals import user_logged_in , user_logged_out

def main_page(request):

 username = password = ''

 state = 1
 if request.POST:
  username = request.POST.get('username')
  password = request.POST.get('password')
        
  user = authenticate(username=username, password=password)
  if user is not None:
   if user.is_active:
    login(request, user)
    return HttpResponseRedirect("../flashcard")
   else:
    state = 0
  else:
   state = -1

 variables = Context({
  'state': state,
 })
 
 return render_to_response('mainpage/index.html',variables,context_instance=RequestContext(request))

def logout_page(request):
    logout(request)
    return render_to_response('mainpage/logout.html')