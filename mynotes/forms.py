from django import forms
from .models import  Note
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import Textarea, TextInput, PasswordInput





class MyUserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields= ['username', 'password1', 'password2', ]
        widgets = {
            'password1':PasswordInput(
                attrs={
                   
                   "class":"form-control"
                }
            ),
        
            'username':TextInput(
                attrs={
                   "placeholder": "Enter username",
                   "class":"form-control"
                }
            ),
             
            
         }



class NoteCreationForm(forms.ModelForm):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs = {
        "class": "form-control", "placeholder": "Enter Title"
    }))

    description = forms.CharField(max_length=10000, widget=forms.Textarea(attrs = {
        "class": "form-control", "placeholder": "Enter Description", "rows": "8"
    }))
    class Meta:
        model=Note
        fields=['title','description']

class NoteUpdateForm(forms.ModelForm):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs = {
        "class": "form-control", "placeholder": "Enter Title"
    }))

    description = forms.CharField(max_length=10000, widget=forms.Textarea(attrs = {
        "class": "form-control", "placeholder": "Enter Description", "rows": "8"
    }))
    class Meta:
        model=Note
        fields=['title','description']
        

class AccountSettingsForm(UserCreationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs = {
        "class": "form-control", "placeholder": "Username"
    }))

    password1 = forms.CharField(max_length=50, widget=forms.TextInput(attrs = {
        "class": "form-control", "placeholder": "New password"
    }))

    password2 = forms.CharField(max_length=50, widget=forms.TextInput(attrs = {
        "class": "form-control", "placeholder": "Confirm password"
    }))

    
    first_name = forms.CharField( widget=forms.TextInput(attrs={
        'placeholder': 'First name', 'class':'form-control'
    }))

    last_name = forms.CharField( widget=forms.TextInput(attrs={
        'placeholder': 'Last name', 'class':'form-control'
    }))
    class Meta:
        model=User
        fields=['username', 'password1', 'password2', 'first_name', 'last_name' ]        