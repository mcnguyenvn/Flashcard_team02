# Create your views here.
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import check_password
from django.shortcuts import render_to_response
from flashcardapp.models import FlashCard

@login_required
def user_flashcard(request):
    flashcards = FlashCard.objects.filter(user__exact = request.user)
    return render_to_response('account/myflashcard.html', {'flashcards': flashcards})

@login_required
def user_profile(request):
    user = request.user

    return render_to_response('account/userprofile.html')

def change_password(request):
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
    return render_to_response('account/changepassword.html', {
        'oldpass': oldpass,
        'newpass1': newpass1,
        'newpass2': newpass2,
        'changed': changed,
        'error': error,
    })