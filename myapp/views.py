from django.shortcuts import render, get_object_or_404, redirect
from . models import Image
from . forms import ImageForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseForbidden





def home(request):
    # Imports all the images and save in the database
    image = Image.objects.all()
    cloudinary_img = {'image':image}

    return render(request, 'myapp/home.html', cloudinary_img)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def dashboard(request):
    images = Image.objects.filter(user=request.user)
    return render(request, 'myapp/dashboard.html', {'images': images})

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ImageForm(user=request.user)
    return render(request, 'myapp/upload_image.html', {'form': form})

@login_required
def edit_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)

    # Verifica se o usuário atual é o proprietário da imagem
    if image.user != request.user:
        return HttpResponseForbidden("Você não tem permissão para editar esta imagem.")

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ImageForm(instance=image)

    return render(request, 'myapp/edit_image.html', {'form': form})

@login_required
def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)

    # Verifica se o usuário atual é o proprietário da imagem
    if image.user != request.user:
        return HttpResponseForbidden("Você não tem permissão para deletar esta imagem.")

    if request.method == 'POST':
        image.delete()
        return redirect('dashboard')

    return render(request, 'myapp/confirm_delete.html', {'image': image})



