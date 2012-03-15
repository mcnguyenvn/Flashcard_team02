# Create your views here.
from Engrade.flashcardapp.forms import FlashCardForm
from Engrade.flashcardapp.models import FlashCard, Question
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    objects = FlashCard.objects.all();
    return render_to_response('index.html', {'objects': objects})

def create(request):
    if request.method == "POST":
        flashcardForm = FlashCardForm(request.POST)
        if flashcardForm.is_valid():
            new_flashcard = flashcardForm.save()
            new_flashcard.save()
            return HttpResponseRedirect('success/')
    else:
        flashcardForm = FlashCardForm()
    return render_to_response('create.html', {
        'flashcardForm': flashcardForm,
    })
    
def create_success(request):
    return render_to_response('create_success.html', {})

def edit(request, flashcard_id):
    #flashcard = FlashCard.objects.get(pk = flashcard_id)
    return render_to_response('edit.html', {'flashcard_id': flashcard_id})

def view_flashcard(request, flashcard_id):
    fc = get_object_or_404(FlashCard, pk = flashcard_id)
    quests = Question.objects.filter(flashcardID__exact = fc)
    return render_to_response('view.html', {
            'fc': fc,
            'quests': quests,
            'flashcard_id': flashcard_id,
    })