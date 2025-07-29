from django.shortcuts import render
from .models import Student
# django default forms
from .forms import userCreate
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def about(request):
    return render(request, 'about/index.html')

def std_info(request):
    # Logic to fetch student information
    sdetails = Student.objects.all()  # Assuming Student model is imported
    return render(request, 'about/student_info.html', {'std':sdetails})

#user creation form
def user_creation_form(request):
    if request.method == 'POST':
        frm = userCreate(request.POST)
        if frm.is_valid():
            frm.save()
    else:
       frm = userCreate()
    return render(request, 'about/user_creation.html', {'form': frm})

def user_login(request):
    frm = AuthenticationForm()
    return render(request, 'about/user_login.html', {'form': frm})