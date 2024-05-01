from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
   context = {
       "variable":"Milan Khatiwada"
   }
   return render(request, 'index.html', context)
#     return HttpResponse("This is my Home Page")

def about(request):
    return HttpResponse("This is my About Page")

def services(request):
    return HttpResponse("This is my Services Page")

def contact(request):
    return HttpResponse("This is my Contact Page")



