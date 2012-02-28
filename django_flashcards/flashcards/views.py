# Create your views here.

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

def main_page(request):
 template = get_template('index.html')
 variables = Context({
  'title': 'FlashCards',
  'headingh1': 'TEAM 2 - K55CA',
  'sologan'  : 'flashcard application',
 })
 output = template.render(variables)
 return HttpResponse(output)