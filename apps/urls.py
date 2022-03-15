from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='home'),
    path('takequiz/', views.takequiz, name='takequiz'),
    path('findresto/', views.findresto, name='findresto'),
    path('quizresults/', views.quizresults, name='quizresults'),
]