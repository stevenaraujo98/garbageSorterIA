from django.http.response import HttpResponseRedirect
from clasification.utils import submit_image, submit_results
from django.shortcuts import render, HttpResponse
from .forms import  ImageForm
from .service import  Densenet

densenet = Densenet()

# Create your views here.
def inicio(request):
    return HttpResponseRedirect("/clasification/procesar/")
    #return render(request, "index.html")

def sorter(request):
    context = {} 
    if request.method == 'POST':
        #print(request.data.get("inputImage"))
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            print("Es validao")
            img = form.cleaned_data.get("imagen")
            url = submit_image(img.file)
            densenet.sorter_action(img.file)
            context['result'] = densenet.prediction()
            context['result']['url'] = url
            submit_results(context['result']['name'], url, context['result']['porc'])
        context["message"] = "cargando"
    else:
        form = ImageForm()
    context['form'] = form
    return render(request, "index.html", context)
    