from django import forms

# Assuming you want to create a form for the Student model

class StudentForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField(error_messages={'required': 'Please enter your last name.'})
    email = forms.EmailField()
    batch = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8, max_length=20)
    re_password = forms.CharField(widget=forms.PasswordInput(), min_length=8, max_length=20)
    message = forms.CharField(widget=forms.Textarea)
    payment = forms.DecimalField(min_value=2500, max_value=10000.0, decimal_places=2)
    django = forms.BooleanField()