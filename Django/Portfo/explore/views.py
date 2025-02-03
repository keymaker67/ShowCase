from django.shortcuts import render


# Create your views here.
def explore_home(request):
    return render(request, 'explore_home.html')


# Create your views here.
def turkish_learning(request):
    return render(request, 'turkish_learning.html')


# Create your views here.
def cryptocurrency(request):
    return render(request, 'cryptocurrency.html')


def saat_oyunu(request):
    return render(request, 'saat_oyunu.html')
