# Create your views here.
from flashcardapp.forms import FlashCardForm
from django.db.models import Q
from flashcardapp.models import FlashCard, Question
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
    
    if request.method == "POST":
        form = FlashCardForm(request.POST)
        if form.is_valid():
            new_flashcard = form.save()
            new_flashcard.user = request.user
            new_flashcard.save()

        for i in xrange(settings.QuestNumber):
            if request.POST['Prompt_%d' % (i+1)] != '':
                prompt = request.POST['Prompt_%d' % (i+1)]
                answer = request.POST['Answer_%d' % (i+1)]
                quest = Question.objects.create(prompt=prompt,answer=answer,vote=0,flashcardID = new_flashcard)
                quest.save()

        return HttpResponseRedirect('/flashcard/create/success')
    else:
        form = FlashCardForm()
    return render_to_response('flashcard/create.html', {
            'form': form,
            'user':request.user,
    },context_instance=RequestContext(request))

@login_required
def creatingsuccess(request):
    return render_to_response('flashcard/creatingsuccess.html')

@login_required
def delete(request, flashcard_id):
    card = get_object_or_404(FlashCard, pk = flashcard_id)
    quests = Question.objects.filter(flashcardID__exact = card)

    for q in quests:
        q.delete()

    card.delete()

    return render_to_response('flashcard/delsuccess.html')

@login_required
def editsuccess(request):
    return render_to_response('flashcard/editsuccess.html')

@login_required
def edit(request, flashcard_id):
    if request.method == "POST":
        form = FlashCardForm(request.POST)
        if form.is_valid():
            new_flashcard = form.save()
            card = get_object_or_404(FlashCard, pk = flashcard_id)
            quests = Question.objects.filter(flashcardID__exact = card)
            card.copy(new_flashcard)
            card.save()

            # delete all old questions
            for q in quests:
                q.delete()

            # add new questions
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
def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(prompt__icontains=query) |
            Q(answer__icontains=query)
            )
        results = Question.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("flashcard/search.html", {
        "results": results,
        "query": query
    })

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

    owner = 0
    if fc.user == request.user:
        owner = 1

    var = RequestContext(request, {
        'fc': fc,
        'quests': quests,
        'flashcard_id': flashcard_id,
        'p':p,
        'a':a,
        'owner': owner,
        })

    return render_to_response('flashcard/viewquest.html',var)