# Create your views here.
from flashcardapp.forms import FlashCardForm, PromptForm
from django.db.models import Q
from flashcardapp.models import FlashCard, Question
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
import settings

def index(request):
    Art = FlashCard.objects.filter(Q(subject='art')).order_by('-id')[:5]
    Bae = FlashCard.objects.filter(Q(subject='bae')).order_by('-id')[:5]
    Cos = FlashCard.objects.filter(Q(subject='cos')).order_by('-id')[:5]
    Geo = FlashCard.objects.filter(Q(subject='geo')).order_by('-id')[:5]
    Gov = FlashCard.objects.filter(Q(subject='gov')).order_by('-id')[:5]
    His = FlashCard.objects.filter(Q(subject='his')).order_by('-id')[:5]
    Mat = FlashCard.objects.filter(Q(subject='mat')).order_by('-id')[:5]
    Mus = FlashCard.objects.filter(Q(subject='mus')).order_by('-id')[:5]
    Fol = FlashCard.objects.filter(Q(subject='fol')).order_by('-id')[:5]
    Sci = FlashCard.objects.filter(Q(subject='sci')).order_by('-id')[:5]
    Peh = FlashCard.objects.filter(Q(subject='peh')).order_by('-id')[:5]
    Rel = FlashCard.objects.filter(Q(subject='rel')).order_by('-id')[:5]

    qfc = FlashCard.objects.all()
    a = []
    for fc in qfc:
        a.append(fc.title)

    variables = Context({
	  'user': request.user,
      'Art': Art,
      'Bae': Bae,
      'Cos': Cos,
      'Geo': Geo,
      'Gov': Gov,
      'His': His,
      'Mat': Mat,
      'Mus': Mus,
      'Fol': Fol,
      'Sci': Sci,
      'Peh': Peh,
      'Rel': Rel,
      'a': a,
	})

    return render_to_response('flashcard/main.html',variables,context_instance=RequestContext(request))

@login_required
def create(request):
    if request.method == "POST":
        form = FlashCardForm(request.POST)
        promptForm = PromptForm(request.POST)
        if form.is_valid() and promptForm.is_valid():
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
        promptForm = PromptForm()
    return render_to_response('flashcard/create.html', {
            'form': form,
            'promptForm': promptForm,
            'user':request.user,
    },context_instance=RequestContext(request))

@login_required
def creatingsuccess(request):
    return render_to_response('flashcard/creatingsuccess.html' , {
		'user':request.user,
    },context_instance=RequestContext(request))

@login_required
def delete(request, flashcard_id):
    card = get_object_or_404(FlashCard, pk = flashcard_id)
    quests = Question.objects.filter(flashcardID__exact = card)

    for q in quests:
        q.delete()

    card.delete()

    return render_to_response('flashcard/delsuccess.html' , {
		'user':request.user,
    },context_instance=RequestContext(request))

@login_required
def editsuccess(request):
    return render_to_response('flashcard/editsuccess.html' , {
		'user':request.user,
    },context_instance=RequestContext(request))

@login_required
def edit(request, flashcard_id):
    if request.method == "POST":
        form = FlashCardForm(request.POST)
        promptForm = PromptForm(request.POST)
        if form.is_valid() and promptForm.is_valid():
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
        pList = dict([])
        for q in quests.all():
            i += 1
            pList['Prompt_%s' % i] = q.prompt
            pList['Answer_%s' % i] = q.answer

        form = FlashCardForm(list)
        promptForm = PromptForm(pList)
    return render_to_response('flashcard/create.html', {
        'form': form,
        'promptForm': promptForm,
        'user':request.user,
        },context_instance=RequestContext(request))

def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(title__icontains=query)
        )
        results = FlashCard.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("flashcard/search.html", {
        "results": results,
        "query": query ,
		'user':request.user,
    }, context_instance=RequestContext(request))
	

def view_title(request,sub):
    objects = FlashCard.objects.filter(subject=sub)
    return render_to_response('flashcard/viewtitle.html',{
		'objects':objects,
		'user':request.user,
    },context_instance=RequestContext(request))

def view_flashcard(request, flashcard_id):

    fc = get_object_or_404(FlashCard, pk = flashcard_id)
    quests = Question.objects.filter(flashcardID__exact = fc)
    moreFc = FlashCard.objects.filter(Q(user=fc.user)).order_by('-id')[:5]
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
        'moreFc': moreFc,
        'viewUser': fc.user,
        })

    return render_to_response('flashcard/viewquest.html',var)