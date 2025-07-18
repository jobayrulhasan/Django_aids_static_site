from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request, 'blog/index.html')

def blog_more1(request):
    return render(request, 'blog/blogmore1.html')

def blog_more2(request):
    return render(request, 'blog/blogmore2.html')

def blog_more3(request):
    return render(request, 'blog/blogmore3.html')