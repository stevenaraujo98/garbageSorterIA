from django.shortcuts import render, HttpResponse
from .forms import  ImageForm
from .service import  Densenet

densenet = Densenet()

# Create your views here.
def inicio(request):
    return HttpResponse('<p>Garbage Sorter IA</p>')
    #return render(request, "index.html")

def sorter(request):
    context = {} 
    if request.method == 'POST':
        #print(request.data.get("inputImage"))
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            print("Es validao")
            img = form.cleaned_data.get("imagen")
            densenet.sorter_action(img.file)
            context['result'] = densenet.prediction()
        context["message"] = "cargando"
    else:
        form = ImageForm()
    context['form'] = form
    return render(request, "index.html", context)
    