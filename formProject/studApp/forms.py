from django import forms

class StudForm(forms.Form):
    sname=forms.CharField(label="Name",max_length=50)
    addr=forms.CharField(label="Address",max_length=100)
    phn=forms.IntegerField(label="Phone number")
    course=forms.CharField(label="Course",max_length=50)#WIdgets
