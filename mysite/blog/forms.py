from django import forms

# Assuming you want to create a form for the Student model

class StudentForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    batch = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)
    message = forms.CharField(widget=forms.Textarea)
    