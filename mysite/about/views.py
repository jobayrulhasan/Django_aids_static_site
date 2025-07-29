from django.shortcuts import render, HttpResponseRedirect
from .models import Student
# django default forms
from .forms import userCreate
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def about(request):
    return render(request, 'about/index.html')

def std_info(request):
    # Logic to fetch student information
    sdetails = Student.objects.all()  # Assuming Student model is imported
    return render(request, 'about/student_info.html', {'std':sdetails})

#user create
def user_creation_form(request):
    if request.method == 'POST':
        frm = userCreate(request.POST)
        if frm.is_valid():
            frm.save()
    else:
       frm = userCreate()
    return render(request, 'about/user_creation.html', {'form': frm})

# user login
def user_login(request):
    if request.method == 'POST':
        frm = AuthenticationForm(request=request, data=request.POST)
        if frm.is_valid():
            uName = frm.cleaned_data.get('username')
            uPassword = frm.cleaned_data.get('password')
            user = authenticate(username=uName, password=uPassword)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/about/login_success')
    else:
      frm = AuthenticationForm()
    return render(request, 'about/user_login.html', {'form': frm})

# user logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/about/userLogin')

# change password
def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            frm = PasswordChangeForm(user=request.user, data=request.POST)
            if frm.is_valid():
                frm.save()
                update_session_auth_hash(request, frm.user)  # Important to keep the user logged in
                return HttpResponseRedirect('/about/changepasswordsuccess')
        else:
            frm = PasswordChangeForm(user=request.user) 
        return render(request, 'about/change_password.html', {'form': frm})
    else:
        return HttpResponseRedirect('/about/userLogin')


# success page after login
def successPage(request):
    return render(request, 'about/login_success.html')

def passwordChangeSuccess(request):
    return render(request, 'about/password_change_success.html')