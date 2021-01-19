from django.http.response import HttpResponseRedirect
from clasification.utils import submit_image, submit_results
from django.shortcuts import render, HttpResponse
from .forms import  DataForm, ImageForm
from .service import  Densenet

densenetPre = Densenet()
densenet = Densenet(load_weights_file="weights_densenet121_acc_91_val_acc_50.h5")

denseNet = "DenseNet"
denseNetPre = "DenseNet (pre entrenada)"

# Create your views here.
def inicio(request):
    return HttpResponseRedirect("/clasification/procesar/")
    #return render(request, "index.html")

def sorter(request):
    context = {} 
    if request.method == 'POST':
        #print(request.data.get("inputImage"))
        form = ImageForm(request.POST, request.FILES)
        form2 = DataForm(request.POST)
        if form.is_valid() and form2.is_valid():
            print("Es validao")
            img = form.cleaned_data.get("imagen")
            net = form2.cleaned_data.get("net")
            url = submit_image(img.file)
            if net == denseNet:
                densenet.sorter_action(img.file)
                context['result'] = densenet.prediction()
                model = "DN"
            else:
                densenetPre.sorter_action(img.file)
                context['result'] = densenetPre.prediction()
                model = "DNP"
            context['result']['url'] = url
            submit_results(context['result']['name'], url, context['result']['porc'], model)
    else:
        form = ImageForm()
        form2 = DataForm()
    context['form'] = form
    context['form2'] = form2
    return render(request, "index.html", context)
    