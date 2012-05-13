# Create your views here.
from pure_pagination.paginator import PageNotAnInteger, Paginator
from flashcardapp.forms import FlashCardForm, PromptForm
from django.db.models import Q
from flashcardapp.models import FlashCard, Question, wrapUser
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
import settings

def index(request):
    Art = FlashCard.objects.filter(Q(subject='art')).order_by('-vote')[:5]
    Bae = FlashCard.objects.filter(Q(subject='bae')).order_by('-vote')[:5]
    Cos = FlashCard.objects.filter(Q(subject='cos')).order_by('-vote')[:5]
    Geo = FlashCard.objects.filter(Q(subject='geo')).order_by('-vote')[:5]
    Gov = FlashCard.objects.filter(Q(subject='gov')).order_by('-vote')[:5]
    His = FlashCard.objects.filter(Q(subject='his')).order_by('-vote')[:5]
    Mat = FlashCard.objects.filter(Q(subject='mat')).order_by('-vote')[:5]
    Mus = FlashCard.objects.filter(Q(subject='mus')).order_by('-vote')[:5]
    Fol = FlashCard.objects.filter(Q(subject='fol')).order_by('-vote')[:5]
    Sci = FlashCard.objects.filter(Q(subject='sci')).order_by('-vote')[:5]
    Peh = FlashCard.objects.filter(Q(subject='peh')).order_by('-vote')[:5]
    Rel = FlashCard.objects.filter(Q(subject='rel')).order_by('-vote')[:5]

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

@login_required(login_url='/login/')
def create(request):
    if request.method == "POST":
        form = FlashCardForm(request.POST)
        promptForm = PromptForm(request.POST)
        if form.is_valid() and promptForm.is_valid():
            new_flashcard = form.save()
            new_flashcard.user = request.user
            new_flashcard.vote = 0
            new_flashcard.save()

        for i in xrange(settings.QuestNumber):
            if request.POST['Prompt_%d' % (i+1)] != '':
                prompt = request.POST['Prompt_%d' % (i+1)]
                answer = request.POST['Answer_%d' % (i+1)]
                quest = Question.objects.create(prompt=prompt,answer=answer,flashcardID = new_flashcard)
                quest.save()

        return HttpResponseRedirect('/flashcard/' + str(new_flashcard.id))
    else:
        form = FlashCardForm()
        promptForm = PromptForm()
    return render_to_response('flashcard/create.html', {
            'form': form,
            'promptForm': promptForm,
            'user':request.user,
            'value': 1,
    },context_instance=RequestContext(request))

@login_required(login_url='/login/')
def delete(request, flashcard_id):
    card = get_object_or_404(FlashCard, pk = flashcard_id)
    if card.user != request.user:
        return HttpResponseRedirect('/flashcard/')
    quests = Question.objects.filter(flashcardID__exact = card)

    for q in quests:
        q.delete()

    card.delete()

    return render_to_response('flashcard/delsuccess.html' , {
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
                    quest = Question.objects.create(prompt=prompt,answer=answer,flashcardID = card)
                    quest.save()

            return HttpResponseRedirect('/flashcard/' + str(flashcard_id))
    else:
        fc = get_object_or_404(FlashCard, pk = flashcard_id)
        if fc.user.username != request.user.username:
            return HttpResponseRedirect('/flashcard/')
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
        'value': 2,
        },context_instance=RequestContext(request))

@login_required
def copy(request, flashcard_id):
    if request.method == "POST":
        form = FlashCardForm(request.POST)
        promptForm = PromptForm(request.POST)
        if form.is_valid() and promptForm.is_valid():
            new_flashcard = form.save()
            new_flashcard.user = request.user
            new_flashcard.vote = 0
            new_flashcard.save()

            # add questions
            for i in xrange(settings.QuestNumber):
                if request.POST['Prompt_%d' % (i+1)] != '':
                    prompt = request.POST['Prompt_%d' % (i+1)]
                    answer = request.POST['Answer_%d' % (i+1)]
                    quest = Question.objects.create(prompt=prompt,answer=answer,flashcardID = new_flashcard)
                    quest.save()

            return HttpResponseRedirect('/flashcard/' + str(new_flashcard.id))
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
        'value': 3,
        },context_instance=RequestContext(request))

def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(title__icontains=query)
        )
        results = FlashCard.objects.filter(qset).distinct().order_by('-vote')
    else:
        results = []
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    # Provide Paginator with the request object for complete querystring generation
    p = Paginator(results, 5, request=request)
    flashcards = p.page(page)
    paging = isNeedPaging(results, 5)
    return render_to_response("flashcard/search.html", {
        'results': results,
        'query': query ,
		'user':request.user,
        'flashcards': flashcards,
        'paging': paging,
    }, context_instance=RequestContext(request))

def isNeedPaging(list, number):
    if len(list) > number:
        return True
    return False

def view_title(request,sub):
    objects = FlashCard.objects.filter(subject=sub).order_by('-vote')
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(objects, 5, request=request)
    flashcards = p.page(page)
    paging = isNeedPaging(objects, 5)
    return render_to_response('flashcard/viewtitle.html',{
		'flashcards':flashcards,
		'user':request.user,
        'paging': paging,
    },context_instance=RequestContext(request))

def view_flashcard(request, flashcard_id):
    fc = get_object_or_404(FlashCard, pk = flashcard_id)
    if request.user.is_authenticated():
        userlike = fc.uservote.filter(user = request.user)
    else:
        userlike = None
    quests = Question.objects.filter(flashcardID__exact = fc)
    moreFc = FlashCard.objects.filter(Q(user=fc.user)).order_by('-vote')[:5]
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
        'userlike': userlike,
        })

    return render_to_response('flashcard/viewquest.html',var)

@login_required(login_url='/login/')
def like(request, flashcard_id):
    fc = get_object_or_404(FlashCard,pk = flashcard_id)
    userlike = fc.uservote.filter(user = request.user)
    if not userlike:
        fc.vote += 1
        newWrapUser = wrapUser.objects.create(user=request.user)
        newWrapUser.save()
        fc.uservote.add(newWrapUser)
        fc.save()
    variables = RequestContext(request,{
        'fc': fc,
        'userlike': userlike,
        })
    return render_to_response('like.html', variables)