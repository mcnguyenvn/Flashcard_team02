# Create your views here.
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import check_password, User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from flashcardapp.models import FlashCard

@login_required
def user_flashcard(request, username):
    viewUser = get_object_or_404(User, username__exact = username)
    flashcards = FlashCard.objects.filter(user__exact = viewUser)
    return render_to_response('account/myflashcard.html', {'flashcards': flashcards,
                                                           'viewUser': viewUser,
                                                           'user':request.user})

@login_required
def edit_profile(request, username):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        request.user.first_name = first_name
        request.user.last_name = last_name
        request.user.email = email
        request.user.save()
        return HttpResponseRedirect('/flashcard/')
    viewUser=get_object_or_404(User, username__exact=username)
    isOwner=False
    if viewUser == request.user:
        isOwner=True
    variables=RequestContext(request, {})
    if isOwner:
        return render_to_response('account/userprofile.html', variables)
    else:
        return render_to_response('404.html')

@login_required
def view_profile(request, username):
    viewUser=get_object_or_404(User, username__exact=username)
    isOwner=False
    if viewUser == request.user:
        isOwner=True
    flist = FlashCard.objects.filter(user__exact = viewUser)
    numberFlashcard = flist.count()
    variables=RequestContext(request, {'viewUser': viewUser, 'isOwner': isOwner, 'numberFlashcard': numberFlashcard})
    return render_to_response('account/viewprofile.html', variables)

@login_required
def change_password(request, username):
    viewUser=get_object_or_404(User, username__exact=username)
    if viewUser != request.user:
        return HttpResponseRedirect('/flashcard/')

    error = 0
    changed = False

    if request.method == "POST":
        oldpass = request.POST.get('oldpass')
        newpass1 = request.POST.get('newpass1')
        newpass2 = request.POST.get('newpass2')

        if check_password(oldpass, request.user.password):
            if newpass1 == newpass2:
                request.user.set_password(newpass1)
                request.user.save()
                changed = True
            else:
                error = 2
        else:
            error = 1

    oldpass = newpass1 = newpass2 = ''
    variables=RequestContext(request, {
        'oldpass': oldpass,
        'newpass1': newpass1,
        'newpass2': newpass2,
        'changed': changed,
        'error': error,})
    return render_to_response('account/changepassword.html', variables)