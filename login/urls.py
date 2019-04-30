from django.urls import path

from . import views

app_name = 'login'

urlpatterns = [
    path('', views.login, name='login'),
    path('lists/', views.lists, name='lists'),
    path('lists/<int:question_id>/',views.detail, name='detail'),
]
