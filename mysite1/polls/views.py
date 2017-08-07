from django.shortcuts import render

from django.http import HttpResponse,Http404
from django.template import loader
from .models import Question
#another method to load the templates from the templates directory--shortcut
from django.shortcuts import render
#another method to raise an http404 error using the following shortcut
from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	#template=loader.get_template('polls/index.html')
	context = {
		'latest_question_list' : latest_question_list,
	}
	return render(request,'polls/index.html',context)
	#return HttpResponse(template.render(context,request))
	#return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")

def detail(request, question_id):
	'''try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request,'polls/detail.html',{'question': question})'''
	question = get_object_or_404(Question,pk=question_id)
	return render(request,'polls/detail.html',{'question':question})
	#return HttpResponse("You're looking at question"+' '+str(question_id))

def results(request, question_id):
	return HttpResponse("You're looking at the results of the question "+str(question_id))

def vote(request, question_id):
	return HttpResponse("You're voting on question "+str(question_id))