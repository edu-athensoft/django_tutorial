from django.urls import path

from . import views

<<<<<<< HEAD
app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
=======
#django convention
app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),

    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),

    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    
>>>>>>> e00851f4d4c91a380696df66f81856db26ec8576
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

]
