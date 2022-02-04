
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect, render
from . import models
from . import forms

# Create your views here.
@login_required
def lexique(request):
    photos = models.Photo.objects.all()
    css = "lexique/lexique_style.css"
    return render(request, "lexique/lexique.html", context={'photos': photos, "css":css})


@login_required
def lexique_upload(request):
    form = forms.PhotoForm()
    if request.method == 'POST':
        form = forms.PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            # set the uploader to the user before saving the model
            photo.uploader = request.user
            # now we can save
            photo.save()
            return redirect('home')
    css = "lexique/lexique_style.css"
    return render(request, 'lexique/lexique_upload.html', context={'form': form, 'css':css})