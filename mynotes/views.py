from django.shortcuts import render,redirect
from .models import Note
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import NoteCreationForm,NoteUpdateForm,AccountSettingsForm,  MyUserRegistrationForm
from django.db.models import Q
#Create your views here.



 
def userlogin(request):
    if request.user.is_authenticated:
        return redirect('mynotes:home')
    if request.method=='POST':
        username = request.POST.get('username')
        #email.lower()
        password = request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('mynotes:home')
        else:
             messages.success(request,"error in logging in")
    
    return render(request,'mynotes/login.html') 

def index(request):
    if request.user.is_authenticated:
        return redirect('mynotes:home')
    return render(request,'mynotes/index.html')


def register(request):
    form=MyUserRegistrationForm()
    context={'form':form}
    if request.method == 'POST':
        form = MyUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()           
            user.save()
            messages.success(request,"Account created successfully!")
            login(request, user)
            return redirect('mynotes:home')
        else:
                messages.error(request, "An error occurred during registration, please try again!")
                return redirect('mynotes:reg_error')
           #login(request, user)
            #return redirect('mynotes/login.html')
        #else:
           # messages.error(request, 'An error occurred during registration')
           # return redirect('mynotes:reg_error')
    return render(request, 'mynotes/register.html',context )

@login_required
def home(request):
    mynotes=Note.objects.filter(author=request.user.id)
    search=request.GET.get('q') if request.GET.get('q')!=None else ''
    mynotes=mynotes.filter(
        
        Q(title__icontains=search)|
        Q(description__icontains=search)
    
        )
    
    count=mynotes.count()
    if count==0:
        check=False
    else:
        check=True
    context={
        'mynotes':mynotes,
        'count':count,
        'check':check
        
    }
    return render(request,'mynotes/home.html',context)       

def add_note(request):
    form=NoteCreationForm()

    if request.method == "POST":
        form=NoteCreationForm(request.POST)

        if form.is_valid():
            note_obj=form.save(commit=False)
            note_obj.author=request.user
            note_obj.save()

            return redirect('mynotes:home')
    context={'form':form}
    return render(request,'mynotes/addnote.html',context)      


@login_required
def account_settings(request):
    
    user=request.user

    form=AccountSettingsForm(instance=user)

    if request.method == "POST":
        form=AccountSettingsForm(request.POST, instance=user)
        if form.is_valid():
            user.save()

       # user.username=request.POST["name"]
        #user.first_name=request.POST["username"]
        #user.last_name=request.POST["email"]

        messages.success(request,"Account Updated Successfully")

        return redirect("mynotes:account_settings")
    context={
        'form':form,
        'user':user
    }
    return render(request,'mynotes/account.html', context) 

def logout(request):
    #return render(request,'mynotes/logout.html')
    return redirect('logout')

def reg_error(request):
    return render(request,'mynotes/reg_error.html')   

@login_required
def update(request, pk):
    note_to_update=Note.objects.get(pk=pk)
    form=NoteUpdateForm(instance=note_to_update)

    if request.method == "POST":
        form=NoteUpdateForm(request.POST)

        if form.is_valid():
            note_to_update.title=form.cleaned_data["title"]
            note_to_update.description=form.cleaned_data["description"]

            note_to_update.save()

            return redirect('mynotes:home')

    context={
        'note':note_to_update,
        'updateform':form
    }
    return render(request,'mynotes/update.html', context)  

    
@login_required
def delete(request, pk):
    note_to_delete=Note.objects.get(pk=pk)
    form=NoteUpdateForm(instance=note_to_delete)

    if request.method == "POST":

       note_to_delete.delete()
       messages.info(request, "Note has been deleted succesfuly")
       return redirect('mynotes:home')

    context={
        'note':note_to_delete,
        'deleteform':form
    }

    return render(request,'mynotes/delete.html', context)      

def search_note(request):
    if request.method == 'POST':
        search_value = request.POST['search']
        notes=Note.objects.filter(title__icontains = search_value) | Note.objects.filter(description__icontains = search_value)
        return redirect('mynotes:home')
    
    return render(request, 'search.html', {'notes':mynotes})
 