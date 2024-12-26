from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile, Project
from .forms import UserProfileForm, ProjectForm

# List all profiles
def profile_list(request):
    profiles = UserProfile.objects.all()
    return render(request, 'profiles/profile_list.html', {'profiles': profiles})

# View individual profile
def profile_detail(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)
    projects = profile.projects.all()
    return render(request, 'profiles/profile_detail.html', {'profile': profile, 'projects': projects})

# Create new profile
def profile_create(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = UserProfileForm()
    return render(request, 'profiles/profile_form.html', {'form': form})

# Update existing profile
def profile_update(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_detail', pk=profile.pk)
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'profiles/profile_form.html', {'form': form})

# Delete existing profile
def profile_delete(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)
    profile.delete()
    return redirect('profile_list')

# Create new project
def project_create(request, profile_pk):
    profile = get_object_or_404(UserProfile, pk=profile_pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user_profile = profile
            project.save()
            return redirect('profile_detail', pk=profile.pk)
    else:
        form = ProjectForm()
    return render(request, 'profiles/project_form.html', {'form': form, 'profile': profile})

# Update existing project
def project_update(request, profile_pk, pk):
    profile = get_object_or_404(UserProfile, pk=profile_pk)
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('profile_detail', pk=profile.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'profiles/project_form.html', {'form': form, 'profile': profile})

# Delete existing project
def project_delete(request, profile_pk, pk):
    profile = get_object_or_404(UserProfile, pk=profile_pk)
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return redirect('profile_detail', pk=profile.pk)
