from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='home'),
    path('takequiz/', views.takequiz, name='takequiz'),
    path('findresto/', views.findresto, name='findresto'),
    path('quizresults/', views.quizresults, name='quizresults'),
    path('bgc/', views.bgc, name='bgc'),

    path('dintaifung/', views.dintaifung, name='dintaifung'),
    path('lapicara/', views.lapicara, name='lapicara'),
    path('mcdo/', views.mcdo, name='mcdo'),
    path('mendokoro/', views.mendokoro, name='mendokoro'),
    path('shakeshack/', views.shakeshack, name='shakeshack'),
    path('singleorigin/', views.singleorigin, name='singleorigin'),
    path('thealley/', views.thealley, name='thealley'),
    path('wangfu/', views.wangfu, name='wangfu'),
    path('wolfgangs/', views.wolfgangs, name='wolfgangs'),
    path('starbucks/', views.starbucks, name='starbucks'),
    path('highestratedrestos/', views.highestratedrestos, name='highestratedrestos'),

    path('spanish/', views.spanish, name='spanish'),
    path('american/', views.american, name='american'),
    path('chinese/', views.chinese, name='chinese'),
    path('japanese/', views.japanese, name='japanese'),
    path('taiwanese/', views.taiwanese, name='taiwanese'),
    path('international/', views.international, name='international'),
    path('low_american/', views.low_american, name='low_american'),

]