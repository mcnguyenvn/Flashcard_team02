'''
Created on Mar 13, 2012

@author: thacdu
'''
from flashcardapp.models import FlashCard
from django import forms
import settings

GRADE_CHOICES = (
    ('first', '1st Grade'),
    ('second', '2nd Grade'),
    ('third', '3rd Grade'),
    ('fourth', '4th Grade'),
    ('fifth', '5th Grade'),
    ('sixth', '6th Grade'),
    ('seventh', '7th Grade'),
    ('eighth', '8th Grade'),
    ('ninth', '9th Grade'),
    ('tenth', '10th Grade'),
    ('eleventh', '11th Grade'),
    ('twelfth', '12th Grade'),
)

SUBJECT_CHOICES = (
    ('art', 'Art'),
<<<<<<< HEAD
    ('bae', 'Business & Economics'),
    ('cos', 'Computer Science'),
    ('geo', 'Geography'),
    ('gov', 'Government & Politics'),
    ('his', 'History'),
    ('mat', 'Math'),
    ('mus', 'Music'),
    ('fol', 'Foreign Language'),
    ('sci', 'Science'),
    ('peh', 'PE & Health'),
    ('rel', 'Religion'),                 
=======
    ('buseco', 'Business & Economics'),
    ('cs', 'Computer Science'),
    ('geo', 'Geography'),
    ('gov', 'Government & Politics'),
    ('history', 'History'),
    ('math', 'Math'),
    ('music', 'Music'),
    ('foreign', 'Foreign Language'),
    ('science', 'Science'),
    ('peh', 'PE & Health'),
    ('religion', 'Religion'),                 
>>>>>>> c64d101212f1ab4060c9ca4390c56bdd4c0432b3
)

class FlashCardForm(forms.ModelForm):
    title = forms.CharField()
    description = forms.CharField(
        widget = forms.Textarea(attrs = {'cols': 50, 'rows': 2}), 
        required = False)
    grade = forms.ChoiceField(
        choices = GRADE_CHOICES)
    subject = forms.ChoiceField(
        choices = SUBJECT_CHOICES)
    
    class Meta:
        model = FlashCard

    def __init__(self, *args, **kwargs):
        super(FlashCardForm, self).__init__(*args, **kwargs)
        for i in xrange(settings.QuestNumber):
            if i < 9:
                self.fields['Prompt_%d' % (i+1)] = forms.CharField(label='Prompt 0%d' % (i+1), required=False)
                # self.fields['Prompt_%d' % (i+1)].widget.attrs = {'class': 'quest'}
                self.fields['Answer_%d' % (i+1)] = forms.CharField(label='Answer 0%d' % (i+1), required=False)
                # self.fields['Answer_%d' % (i+1)].widget.attrs = {'class': 'ans'}
            else:
                self.fields['Prompt_%d' % (i+1)] = forms.CharField(required=False)
                # self.fields['Prompt_%d' % (i+1)].widget.attrs = {'class': 'quest'}
                self.fields['Answer_%d' % (i+1)] = forms.CharField(required=False)
                # self.fields['Answer_%d' % (i+1)].widget.attrs = {'class': 'ans'}


    def save(self):
        new_flashcard = FlashCard()
        new_flashcard.title = self.cleaned_data['title']
        new_flashcard.description = self.cleaned_data['description']
        new_flashcard.grade = self.cleaned_data['grade']
        new_flashcard.subject = self.cleaned_data['subject']
        new_flashcard.save()
        return new_flashcard
    