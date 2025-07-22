from django.shortcuts import render
from .models import Student

# Create your views here.
def about(request):
    return render(request, 'about/index.html')

def std_info(request):
    # Logic to fetch student information
    sdetails = Student.objects.all()  # Assuming Student model is imported
    return render(request, 'about/student_info.html', {'std':sdetails})