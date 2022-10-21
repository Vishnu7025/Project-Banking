from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from . forms import BookingForm
from . models import *
from django.utils.safestring import mark_safe

# Create your views here.
def home(request):
    return render(request,'index.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password= request.POST['password']
        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('newpage')
        else :
            messages.info(request,'Invalid details')
            return redirect('login')
    else:
        return render (request,'login.html')

    return render(request,'login.html')

def register(request):
    SpecialSym =['$', '@', '#', '%']
    if request.method=="POST":
        user_name = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,'username already taken')
                return redirect('register')
            elif len(password1) < 8:
                messages.info(request,'password must have atleast 8 letters')
                return redirect('register')
            elif not any(char.isupper() for char in password1):
                messages.info(request,'password must have atleast 1 uppercase')
                return redirect('register')
            elif not any(char.islower() for char in password1):
                messages.info(request,'password must have atleast 1 lowercase')
                return redirect('register')
            elif not any(char in SpecialSym for char in password1):
                messages.info(request,'Password should have at least one of the symbols $@#')
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name,password=password1)
                user.save();
        else:
            messages.info(request,'password not matched')
            return redirect('register')
        return redirect('login')
    else:
         return render(request,'register.html')

def logout(request):
     auth.logout(request)
     return redirect('/')

def newpage(request):
    return render(request,'newpage.html')

def form(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,mark_safe("Application accepted <a href='/'> &ensp; &ensp; &ensp; &ensp; &ensp; &ensp;Go back home</a>"))

    form = BookingForm()
    dict_form = {
        'form': form
    }
    return render(request,'form.html',dict_form)


def load_branch_details(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(
        district=district_id).order_by('name')
    return render(request, 'load_branch_dropdown_list.html', {'branches': branches})