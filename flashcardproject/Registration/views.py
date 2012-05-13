# Create your views here.
import re
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.validators import email_re
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from Registration.forms import ForgotPasswordForm, RegistrationForm

def is_valid_email(email):
    return True if email_re.match(email) else False

def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/flashcard/')
    notif = 0
    form = RegistrationForm()
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email    = request.POST.get('email')
        if not re.search(r'^\w+$', username):
            notif = 10
            variables = RequestContext(request, {'notif': notif})
            return render_to_response('registration/regis.html', variables)
        if len(username) < 5 or len(password) < 6 or not is_valid_email(email):
            if len(username) < 5:
                notif = 4
            elif len(password) < 6:
                notif = 5
            else: notif = 6
            variables = RequestContext(request, {'notif': notif})
            return render_to_response('registration/regis.html', variables)
        regedUser = User.objects.filter(username__exact = username)
        if regedUser:
            notif = 2
            variables = RequestContext(request, {'notif': notif})
            return render_to_response('registration/regis.html', variables)
        regedEmail = User.objects.filter(email__exact = email)
        if regedEmail:
            notif = 3
            variables = RequestContext(request, {'notif': notif})
            return render_to_response('registration/regis.html', variables)
        if username == '' or password == '' or email == '':
            notif = 1
            variables = RequestContext(request, {'notif': notif})
            return render_to_response('registration/regis.html', variables)
        user = User.objects.create_user(username, email, password)
        user.save()
        send_mail(
            '[Flashcard] Welcome to our website',
            'Thank you for your registration.'
            'Admin,',
            '',
            [email],
            fail_silently=True)
        return HttpResponseRedirect('../regis_success')
    variables = RequestContext(request, {'notif': notif, 'form': form,})
    return render_to_response('registration/regis.html', variables)

def regis_success(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/flashcard/')
    return render_to_response('registration/regis_succes.html')

def reset_password(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/flashcard/')
    form = ForgotPasswordForm()
    notif = 0
    if request.POST:
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(username=username, email=email)

                new_password = User.objects.make_random_password(
                    length=8,
                    allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ0123456789'
                )
                user.set_password(new_password)
                user.save()
                send_mail(
                    '[Flashcard] Reset Password',
                    'Your new password: ' + new_password,
                    '',
                    [email],
                    fail_silently=True)
            except User.DoesNotExist:
                notif = 1
                render_to_response('registration/lostpassword.html', {'form': form, 'notif': notif})
    return render_to_response('registration/lostpassword.html', {'form': form, 'notif': notif})

def reset_success(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/flashcard/')
    return render_to_response('resetsuccess.html')