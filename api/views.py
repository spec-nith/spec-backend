from django.shortcuts import HttpResponse, render

# Create your views here.


def HomeView(request):
    return HttpResponse("<marquee><h2>I'm on</h2></marquee>")
