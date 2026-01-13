from django.shortcuts import render

# Create your views here.
def index(request):
    print("View is being called")
    return render(request, 'index.html')