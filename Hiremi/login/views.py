from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "log-in.html")

def dashboard(request):
    return render(request, "dash.html")

def totalaccount(request):
    return render(request, "totalaccount.html")

def profile(request):
    return render(request, "profile.html")