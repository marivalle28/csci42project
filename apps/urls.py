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

    path('result_mcdo/', views.result_mcdo, name='result_mcdo'),
    path('result_lapicara/', views.result_lapicara, name='result_lapicara'),
    path('result_thealley/', views.result_thealley, name='result_thealley'),
    path('result_dintaifung/', views.result_dintaifung, name='result_dintaifung'),
    path('result_mendokoro/', views.result_mendokoro, name='result_mendokoro'),
    path('result_wangfu/', views.result_wangfu, name='result_wangfu'),
    path('result_shakeshack/', views.result_shakeshack, name='result_shakeshack'),
    path('result_singleorigin/', views.result_singleorigin, name='result_singleorigin'),
    path('result_wolfgang/', views.result_wolfgang, name='result_wolfgang'),
    path('result_starbucks/', views.result_starbucks, name='result_starbucks'),
    path('result_nomatch/', views.result_nomatch, name='result_nomatch'),
]