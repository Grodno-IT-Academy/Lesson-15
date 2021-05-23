from django.shortcuts import render, redirect
from .forms import ImageForm
from django.core.files.storage import FileSystemStorage
from .models import Image
from django.contrib.staticfiles.storage import staticfiles_storage

# Create your views here.
def form(request):
    context = {
        'form': ImageForm(),
    }
    return render(request, 'form.html', context=context)

def upload(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            id = form.save()
            object = Image.objects.get(pk=id.id).image
            imageURL = FileSystemStorage().url(object)
            from .inference import runInference
            prediction = runInference(imageURL)
            context = {
                'prediction': prediction,
                'imageurl': imageURL,
            }
            return render(request, 'upload.html', context=context)
    return redirect('home')