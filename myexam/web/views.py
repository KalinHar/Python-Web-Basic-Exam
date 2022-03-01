from django.shortcuts import render, redirect

from myexam.web.forms import CreateProfileForm, CreateAlbumForm, DeleteAlbumForm, DeleteProfileForm
from myexam.web.models import Profile, Album


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def home(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')
    albums = Album.objects.all()
    context = {
        'profile': profile,
        'albums': albums
    }
    return render(request, 'home-with-profile.html', context)


def add_album(request):
    profile = get_profile()
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateAlbumForm()

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'add-album.html', context)


def album_details(request, pk):
    album = Album.objects.get(pk=pk)
    profile = get_profile()
    context = {
        'profile': profile,
        'album': album,
    }
    return render(request, 'album-details.html', context)


def edit_album(request, pk):
    profile = get_profile()
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateAlbumForm(instance=album)

    context = {
        'profile': profile,
        'form': form,
        'album': album
    }
    return render(request, 'edit-album.html', context)


def delete_album(request, pk):
    profile = get_profile()
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DeleteAlbumForm(instance=album)

    context = {
        'form': form,
        'profile': profile,
        'album': album,
    }
    return render(request, 'delete-album.html', context)


def profile_details(request):
    profile = get_profile()
    albums_count = len(Album.objects.all())
    context = {
        'profile': profile,
        'album_count': albums_count,
    }
    return render(request, 'profile-details.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            Album.objects.all().delete()
            form.save()
            return redirect('home')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'profile-delete.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)