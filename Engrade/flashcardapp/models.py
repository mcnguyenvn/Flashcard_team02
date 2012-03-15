from django.db import models

# Create your models here.

class FlashCard(models.Model):
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 300)
    grade = models.CharField(max_length = 200)
    subject = models.CharField(max_length = 200)
    
    def is_valid(self):
        if(self.title == None or
           self.grade == None or
           self.subject == None
        ): return False
        return True
        
        
    '''
    def __init__(self, title, description, gradeLevel, subject):
        self.title = title
        self.description = description
        self.gradeLevel = gradeLevel
        self.subject = subject
    '''
        
class Question(models.Model):
    prompt = models.CharField(max_length = 500, null = True, blank = True)
    answer = models.CharField(max_length = 500, null = True, blank = True)
    flashcardID = models.ForeignKey(FlashCard, null = True, blank = True)
    
    def is_valid(self):
        return (self.prompt != None and self.answer != None)
    '''
    def __init__(self, prompt, answer, flashcardID):
        self.prompt = prompt
        self.answer = answer
        self.flashcardID = flashcardID
    '''