from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            # print(form.errors)
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def loginPage(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('blog')
        else:
            error_message = "Wrong credentials.This user doesn't exist"

    return render(request, 'registration/login.html', {'error_message':error_message})

def log_out(request):
    logout(request)
    return redirect('blog')




















# from django.shortcuts import render,redirect, HttpResponse
# from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
# # from django.views import generic
# # from django.contrib.auth.forms import UserCreationForm
# # from django.urls import reverse_lazy
# # from django.contrib import messages
# # Create your views here.

# # def SignupPage(request):
# #     if request.method=='POST':
# #         uname=request.POST.get('username')
# #         email=request.POST.get('email')
# #         pass1=request.POST.get('password1')
# #         pass2=request.POST.get('password2')

# #         if pass1!=pass2:
# #             return HttpResponse("Your password and confirm password are not Same!!")
# #         else:

# #             my_user=User.objects.create_user(uname,email,pass1)
# #             my_user.save()
# #             return redirect('login')
        



# #     return render (request,'registration/signup.html')

# # def LoginPage(request):
# #     if request.method=='POST':
# #         username=request.POST.get('username')
# #         pass1=request.POST.get('pass')
# #         user=authenticate(request,username=username,password=pass1)
# #         if user is not None:
# #             login(request,user)
# #             return redirect('blog')
# #         else:
# #             return HttpResponse ("Username or Password is incorrect!!!")

# #     return render (request,'registration/login.html')

# # def LogoutPage(request):
# #     logout(request)
# #     return redirect('blog')



# # def signup(request):
# # #     if request.method == 'POST':
# # #         form = UserCreationForm(request. POST)
# # #         if form.is_valid ():
# # #             form.save()
# # # # log the user in
# # #             return redirect('blog')
# # #     else:   
# # #         form = UserCreationForm()
# # #     return render(request, 'authors/register.html', { 'form': form })
# #     if request.method == "POST":
# #         form = UserCreationForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #         messages.success(request, "your acc created")
# #         return redirect('blog')
# #     else:
# #         form = UserCreationForm()
# #     return render(request, 'authors/register.html', {'form':form})

# # def login(request):
# #     return render (request, 'authors/login.html')