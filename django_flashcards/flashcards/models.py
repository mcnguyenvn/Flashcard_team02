from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Link(models.Model):
 url = models.URLField(unique=True)
 
class Question(models.Model):
 quest = models.CharField(max_length=255)
 user = models.ForeignKey(User)
 link = models.ForeignKey(Link)
 
 def __unicode__(self):
  return self.quest
				
class Answer(models.Model):
 quest = models.ForeignKey(Question)
 answer = models.CharField(max_length=255)
 votes = models.IntegerField()
	
 def __unicode__(self):
  return self.question