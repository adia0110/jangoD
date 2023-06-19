from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):

    peoples =[
        {'name':'Aditya','age':26},
        {'name':'Agarwal','age':23},
        {'name':'Adi','age':24},
        {'name':'Adi_ag','age':16}
    ]
    
    text="""czvn  c k jdn clkdzf  nd kl cxn kckjn.djcn cbdkjfnsckj.dhnfiksldnvdsjk dgfuidfhbdifdkj.ns
        cskdmsac vslkdskcns 
    """
    vegetables =['pumpkin','tomato','potato']
    context={'peoples':peoples,'text':text,'vegetables':vegetables,'page':'home'}
    return render(request,"home/index.html",context)

def about(request):
    context={'page':'about'}
    return render(request,"home/about.html",context)
def contact(request):
    context={'page':'contact'}
    return render(request,"home/contact.html",context)

def success_page(request):
    print("*"*10)
    return HttpResponse("<h1>Success page</h1>")
