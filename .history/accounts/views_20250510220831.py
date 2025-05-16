from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile, User
from .forms import Profile, UpdateProfileForm
from django.contrib.auth.decorators import login_required

def index(request):
    
    return render(request, 'index.html')

def about(request):
    
    return render(request, 'about.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    
    return render(request,  'profile.html', {'user': current_user, 'profile': profile})

@login_required(login_url='/accounts/login/')
def update_profile(request, id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user_id=user)

    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            user.first_name = form.cleaned_data.get('first_name', user.first_name)
            user.last_name = form.cleaned_data.get('last_name', user.last_name)
            user.save()
            profile.save()
            return redirect('profile')
    else:
        form = UpdateProfileForm(instance=profile, initial={
            'first_name': user.first_name,
            'last_name': user.last_name
        })

    return render(request, 'update_profile.html', {'form': form})
