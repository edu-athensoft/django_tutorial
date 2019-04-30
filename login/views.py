from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import UserAccount

# Create your views here.

def login(request):
    html_str = "view: login"
    return HttpResponse(html_str)

# def login(request):
#     template = loader.get_template('login/login.html')
      
#     return HttpResponse(template.render(request, {}))


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