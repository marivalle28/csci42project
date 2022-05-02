from django.shortcuts import render

def home(request):
		return render(request, "apps/home.html")

def takequiz(request):
		return render(request, "apps/takequiz.html")

def findresto(request):
		return render(request, "apps/findresto.html")

def quizresults(request):
		return render(request, "apps/quizresults.html")

def bgc(request):
		return render(request, "apps/bgc.html")

# resto views
def dintaifung(request):
		return render(request, "apps/resto_dintaifung.html")

def lapicara(request):
		return render(request, "apps/resto_lapicara.html")

def mcdo(request):
		return render(request, "apps/resto_mcdo.html")

def mendokoro(request):
		return render(request, "apps/resto_mendokoro.html")

def shakeshack(request):
		return render(request, "apps/resto_shakeshack.html")

def singleorigin(request):
		return render(request, "apps/resto_singleorigin.html")

def thealley(request):
		return render(request, "apps/resto_thealley.html")

def wangfu(request):
		return render(request, "apps/resto_wangfu.html")