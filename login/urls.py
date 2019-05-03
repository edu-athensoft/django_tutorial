from django.urls import path

from . import views

app_name = 'login'

urlpatterns = [
    path('', views.login, name='login'),
    path('lists/', views.lists, name='lists'),
    path('lists/<int:user_account_id>/',views.detail, name='detail'),
    path('profile/',views.profile, name='profile'),
]
