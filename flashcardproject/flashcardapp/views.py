# Create your views here.
from flashcardapp.forms import FlashCardForm
from flashcardapp.models import FlashCard, Question
<<<<<<< HEAD
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
import settings

@login_required
def index(request):
    variables = Context({
	  'user': request.user,
	})

    return render_to_response('flashcard/main.html',variables,context_instance=RequestContext(request))

@login_required
def create(request):
    
=======
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
>>>>>>> c64d101212f1ab4060c9ca4390c56bdd4c0432b3
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

<<<<<<< HEAD
        return HttpResponseRedirect('/flashcard/create/success')
=======
        return HttpResponseRedirect('success/')
>>>>>>> c64d101212f1ab4060c9ca4390c56bdd4c0432b3
    else:
        form = FlashCardForm()
    return render_to_response('flashcard/create.html', {
            'form': form,
<<<<<<< HEAD
            'user':request.user,
=======
            'login': login
>>>>>>> c64d101212f1ab4060c9ca4390c56bdd4c0432b3
    },context_instance=RequestContext(request))

@login_required
def creatingsuccess(request):
<<<<<<< HEAD
    return render_to_response('flashcard/creatingsuccess.html')

@login_required
def editsuccess(request):
    return render_to_response('flashcard/editsuccess.html')

@login_required
def edit(request, flashcard_id):
    if request.method == "POST":
        form = FlashCardForm(request.POST)
        if form.is_valid():
            card = get_object_or_404(FlashCard, pk = flashcard_id)
            quests = Question.objects.filter(flashcardID__exact = card)

            for q in quests:
                q.delete()


            for i in xrange(settings.QuestNumber):
                if request.POST['Prompt_%d' % (i+1)] != '':
                    prompt = request.POST['Prompt_%d' % (i+1)]
                    answer = request.POST['Answer_%d' % (i+1)]
                    quest = Question.objects.create(prompt=prompt,answer=answer,vote=0,flashcardID = card)
                    quest.save()

            return HttpResponseRedirect('/flashcard/edit/success')
    else:
        fc = get_object_or_404(FlashCard, pk = flashcard_id)
        list = dict([])
        list['title'] = fc.title
        list['description']=fc.description
        list['grade']=fc.grade
        list['subject']=fc.subject

        quests = Question.objects.filter(flashcardID__exact = fc)
        i = 0
        for q in quests.all():
            i += 1
            list['Prompt_%s' % i] = q.prompt
            list['Answer_%s' % i] = q.answer

        form = FlashCardForm(list)
    return render_to_response('flashcard/create.html', {
        'form': form,
        'user':request.user,
        },context_instance=RequestContext(request))

@login_required
def view_title(request,sub):
    objects = FlashCard.objects.filter(subject=sub)
    return render_to_response('flashcard/viewtitle.html',{'objects':objects})

@login_required
def view_flashcard(request, flashcard_id):

    fc = get_object_or_404(FlashCard, pk = flashcard_id)
    quests = Question.objects.filter(flashcardID__exact = fc)

    p = ''
    a = ''
    for q in quests:
        p += q.prompt + '***'
        a += q.answer + '***'
    p = p[:-3]
    a = a[:-3]

    var = RequestContext(request, {
        'fc': fc,
        'quests': quests,
        'flashcard_id': flashcard_id,
        'p':p,
        'a':a,
        })

    return render_to_response('flashcard/viewquest.html',var)
=======
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
>>>>>>> c64d101212f1ab4060c9ca4390c56bdd4c0432b3
