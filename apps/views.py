from django.shortcuts import render

def home(request):
		return render(request, "apps/home.html")

def takequiz(request):
		return render(request, "apps/takequiz.html")

def findresto(request):
		return render(request, "apps/findresto.html")

def quizresults(request):
		return render(request, "apps/quizresults.html")