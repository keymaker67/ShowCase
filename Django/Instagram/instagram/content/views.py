from django.shortcuts import render


# Create content view
def post_view(request):
    user = request.user
    return render(request, 'main/index.html')
