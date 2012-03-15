'''
Created on Mar 13, 2012

@author: thacdu
'''
from Engrade.flashcardapp.models import FlashCard
from django import forms

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
    
    '''    
    def __init__(self, title, description, grade, subject):
        self.title = title
        self.description = description
        self.grade = grade
        self.subject = subject
    '''
         
    def save(self):
        new_flashcard = FlashCard()
        new_flashcard.title = self.cleaned_data['title']
        new_flashcard.description = self.cleaned_data['description']
        new_flashcard.grade = self.cleaned_data['grade']
        new_flashcard.subject = self.cleaned_data['subject']
        new_flashcard.save()
        return new_flashcard