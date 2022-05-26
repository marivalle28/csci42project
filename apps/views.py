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

def wolfgangs(request):
		return render(request, "apps/resto_wolfgangs.html")

def starbucks(request):
		return render(request, "apps/resto_starbucks.html")

def highestratedrestos(request):
		return render(request, "apps/highestratedrestos.html")

def spanish(request):
		return render(request, "apps/cuisine_spanish.html")

def international(request):
		return render(request, "apps/cuisine_international.html")

def japanese(request):
		return render(request, "apps/cuisine_japanese.html")

def taiwanese(request):
		return render(request, "apps/cuisine_taiwanese.html")

def chinese(request):
		return render(request, "apps/cuisine_chinese.html")

def american(request):
		return render(request, "apps/cuisine_american.html")

def result_mcdo(request):
		return render(request, "apps/result_mcdo.html")

def result_lapicara(request):
		return render(request, "apps/result_lapicara.html")

def result_thealley(request):
		return render(request, "apps/result_thealley.html")

def result_dintaifung(request):
		return render(request, "apps/result_dintaifung.html")

def result_mendokoro(request):
		return render(request, "apps/result_mendokoro.html")

def result_wangfu(request):
		return render(request, "apps/result_wangfu.html")

def result_shakeshack(request):
		return render(request, "apps/result_shakeshack.html")

def result_singleorigin(request):
		return render(request, "apps/result_singleorigin.html")

def result_wolfgang(request):
		return render(request, "apps/result_wolfgang.html")

def result_starbucks(request):
		return render(request, "apps/result_starbucks.html")

def result_nomatch(request):
		return render(request, "apps/result_nomatch.html")