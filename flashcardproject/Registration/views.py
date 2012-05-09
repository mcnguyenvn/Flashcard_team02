# Create your views here.

from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/flashcard/')
    notif = 0
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email    = request.POST.get('email')
        if username == '' or password == '' or email == '':
            notif = 1
            variables = RequestContext(request, {'notif': notif})
            return render_to_response('registration/regis.html', variables)
        user = User.objects.create_user(username, email, password)
        user.save()
        return HttpResponseRedirect('../regis_success')
    variables = RequestContext(request, {'notif': notif})
    return render_to_response('registration/regis.html', variables)

def regis_success(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/flashcard/')
    return render_to_response('registration/regis_succes.html')

def reset_password(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/flashcard/')
    error = 0
    form = PasswordResetForm()
    if request.POST:
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.clean_email()
            #username = User.objects.get(email = email)
            #password = username.password
            send_mail(
                'Flashcard Reset Password',
                'test',
                ''
                [email],
                fail_silently=True)
            return HttpResponseRedirect('/flashcard/')
        else:
            error = 1
    return render_to_response('registration/lostpassword.html', {'form': form, 'error': error})

def reset_success(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/flashcard/')
    return render_to_response('resetsuccess.html')