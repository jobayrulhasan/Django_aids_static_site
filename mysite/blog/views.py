from django.shortcuts import render
from .forms import StudentForm


# Main blog pages
def blog(request):
    return render(request, 'blog/index.html')

def blog_more1(request):
    return render(request, 'blog/blogmore1.html')

def blog_more2(request):
    return render(request, 'blog/blogmore2.html')

def blog_more3(request):
    return render(request, 'blog/blogmore3.html')


def show_form(request):
    if request.method == 'POST':
        frm = StudentForm(request.POST)
        # print("Form submitted with data:", frm.data)
        print("POST request received")
        if frm.is_valid():
            print("Form is valid")
            print("Form data:", frm.cleaned_data)
    else:
        frm = StudentForm()  # Initialize an empty form for GET requests
        print("GET request received")
    return render(request, 'blog/form.html', {'form': frm})