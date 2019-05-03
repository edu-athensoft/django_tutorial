from django.shortcuts import get_object_or_404,render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import UserAccount

# Create your views here.

# def login(request):
#     html_str = "view: login"
#     return HttpResponse(html_str)

def login(request):
    # template = loader.get_template('login/login.html')
    return render(request, 'login/login.html')


# def lists(request):
#     html_str = "view: lists"
#     return HttpResponse(html_str)


def lists(request):
    user_account_list = UserAccount.objects.order_by('user_name')[:]
    template = loader.get_template('login/list.html')
    context = {
        'user_account_list': user_account_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, user_account_id):
    user_account = get_object_or_404(UserAccount, pk=user_account_id)
    return render(request, 'login/detail.html', {'user_account': user_account})


def profile(request):
    # user_account = get_object_or_404(UserAccount, pk=user_account_id)
    context = {}

    if request.POST:
        context['input_username'] = request.POST['userName']
        context['input_userpassword'] = request.POST['userPassword']
    else:
        return HttpResponse("Invalid")

    # template = loader.get_template('login/profile.html')
    return render_to_response('login/profile.html', context)
    