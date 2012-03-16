# Create your views here.
from flashcardapp.forms import FlashCardForm
from flashcardapp.models import FlashCard, Question
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
import settings

def index(request):
    login = 0
    if request.user.is_authenticated():
        login = 1
    objects = FlashCard.objects.all()
    return render_to_response('flashcard/index.html', {'objects': objects, 'login': login})
    
@login_required
def create(request):
    login = 0
    if request.user.is_authenticated():
        login = 1
    if request.method == "POST":
        form = FlashCardForm(request.POST)
        if form.is_valid():
            new_flashcard = form.save()
            new_flashcard.save()

        for i in xrange(settings.QuestNumber):
            if request.POST['Prompt_%d' % (i+1)] != '':
                prompt = request.POST['Prompt_%d' % (i+1)]
                answer = request.POST['Answer_%d' % (i+1)]
                quest = Question.objects.create(prompt=prompt,answer=answer,vote=0,flashcardID = new_flashcard)
                quest.save()

        return HttpResponseRedirect('success/')
    else:
        form = FlashCardForm()
    return render_to_response('flashcard/create.html', {
            'form': form,
            'login': login
    },context_instance=RequestContext(request))

@login_required
def creatingsuccess(request):
    login = 0
    if request.user.is_authenticated():
        login = 1
    return render_to_response('flashcard/creatingsuccess.html', {'login': login})

@login_required
def edit(request, flashcard_id):
    login = 0
    if request.user.is_authenticated():
        login = 1
    flashcard = FlashCard.objects.get(pk = flashcard_id)
    return render_to_response('flashcard/edit.html', {'flashcard_id': flashcard_id, 'login': login})

@login_required
def view_flashcard(request, flashcard_id):
    login = 0
    if request.user.is_authenticated():
        login = 1
    fc = get_object_or_404(FlashCard, pk = flashcard_id)
    quests = Question.objects.filter(flashcardID__exact = fc)
    return render_to_response('flashcard/view.html', {
            'fc': fc,
            'quests': quests,
            'flashcard_id': flashcard_id,
            'login': login
    })