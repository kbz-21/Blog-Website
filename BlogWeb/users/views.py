from django.shortcuts import render,redirect
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required



# ...........this is for the user registration form from user application........
def register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Account Succesfuly Created for {username}')
            return redirect('blog-home')
    else:
        form=UserRegisterForm() 
    return render(request, 'users/register.html',{'form':form})

# profile updating codes

@login_required
def profile(request):
    return render(request,'users/profile.html')
@login_required
def profile_update(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if u_form.is_valid and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"your profile succesfully updated!!")
            return redirect('profile')
        
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context ={
        'u_form': u_form,
        'p_form': p_form 
    }
    return render(request,'users/profile_update.html',context)


