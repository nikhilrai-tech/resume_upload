from django.shortcuts import render,HttpResponseRedirect
from . forms import myform
from . models import resume

def home(request):
    if request.method=="POST":
        fm=myform(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/")
    else:
        fm=myform()
    res=resume.objects.all()
    return render(request,"index.html",{"fm":fm,"re":res})

def details(request,id):
    id=id
    fm=resume.objects.get(pk=id)
    return render(request,"details.html",{"fm":fm})
    