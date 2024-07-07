from django.shortcuts import render


# Create views .
def home_view(request):
    return render(request, 'home.html')
