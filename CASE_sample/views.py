from django.shortcuts import render

# Create your views here.
def JuniperCaseMain(request):
    return render(request, 'CASE/main.html')