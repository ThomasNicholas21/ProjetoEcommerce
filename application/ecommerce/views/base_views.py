from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'ecommerce/index.html')

def about(request):
    return render(request, 'ecommerce/about.html')
