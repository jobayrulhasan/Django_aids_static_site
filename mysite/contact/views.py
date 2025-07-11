from django.shortcuts import render

# Create your views here.
def contact(response):
    return render(response, 'contact/index.html')