from django.shortcuts import render, redirect
from model.models import Image
from django.core.files.storage import FileSystemStorage
from model.forms import ImageForm

# Create your views here.
def home_page(request):
    images = Image.objects.all()
    urls = {}
    for img in images:
        url = FileSystemStorage().url(img.image)
        urls[str(img.id)] = url
    print(urls)
    context = {
        'images': images,
    }
    return render(request, 'index.html', context)

def view_image(request, key):
    img = Image.objects.get(id=key)
    file_name = img.image.url
    url = FileSystemStorage().url(img.image)
    context = {
        'file_name': file_name,
        'img_url': url,
    }
    return render(request, 'image.html', context)

def update_image(request, id):
    image = Image.objects.get(id=id)
    form = ImageForm(instance=image)
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'form.html', context)

def delete_image(request, id):
    image = Image.objects.get(id=id)
    name = image.image.url.split('/')[-1]
    if request.method == "POST":
        image.delete()
        return redirect('/')
    context = {
        'name': name
    }
    return render(request, 'delete.html', context)

def run_inference(request, id):
    image = Image.objects.get(pk=id)
    object = image.image
    imageURL = FileSystemStorage().url(object)
    from model.inference import runInference
    img_url = '/..' + imageURL
    prediction = runInference(img_url)
    context = {
        'prediction': prediction,
        'imageurl': imageURL,
    }
    return render(request, 'upload.html', context)