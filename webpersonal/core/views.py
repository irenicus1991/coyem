from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "core/home.html")
def about(request):
    return render(request, "core/about.html")
def contact(request):
    return render(request, "core/contacto.html")
def filosofia(request):
    return render(request, "core/filosofia.html")
def misión(request):
    return render(request, "core/misión.html")
def visión(request):
    return render(request, "core/visión.html")

