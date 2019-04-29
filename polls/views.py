<<<<<<< HEAD
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import Http404
from django.urls import reverse

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from .models import Question, Choice

# def index(request):
#     html_str = r"<!doctype html><html><head><title>Polls</title></head><body><h1>My First App Polls</h1><div><p>test this web page<br/>Hello, world. You're at the polls index.</p><img src='https://thumbs.dreamstime.com/z/assassin-outlaw-thief-burglar-fantasy-medieval-action-rpg-game-character-layered-animation-ready-vector-illustration-131042596.jpg' width='20%'/></div></body></html>"

#     img_path= r"https://thumbs.dreamstime.com/z/assassin-outlaw-thief-burglar-fantasy-medieval-action-rpg-game-character-layered-animation-ready-vector-illustration-131042596.jpg"

#     return HttpResponse(html_str)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

# def detail(request, question_id):
#    return HttpResponse("You're looking at question %s." % question_id)
=======
# from django.shortcuts import get_object_or_404, render

# Create your views here.
# from django.http import HttpResponse
# from django.template import loader

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question,Choice


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

>>>>>>> e00851f4d4c91a380696df66f81856db26ec8576

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})

<<<<<<< HEAD
=======

>>>>>>> e00851f4d4c91a380696df66f81856db26ec8576
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


<<<<<<< HEAD
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
=======

>>>>>>> e00851f4d4c91a380696df66f81856db26ec8576

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

<<<<<<< HEAD
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
=======

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
>>>>>>> e00851f4d4c91a380696df66f81856db26ec8576
