from django.shortcuts import render,redirect
from.models import*
from rest_framework.response import Response

# Create your views here.
def vege(request):
    if request.method=="POST":
        rname = request.POST.get("rname")
        rdes = request.POST.get("rdes")
        rphot = request.FILES.get('rphot')
        #print(rname)
        Recipy.objects.create(rname=rname,
                  rdes=rdes,
                  rphot=rphot,)
        return redirect("/vege")
    data = Recipy.objects.all()
    context = {"datas":data}
    return render(request,"vege.html",context)
def dele(request,id):
    de = Recipy.objects.get(id = id)
    de.delete()
    return redirect("/vege")
def upda(request,id):
    queryset = Recipy.objects.get(id = id)
    context = {
        "datas":queryset
    }
    if request.method=="POST":
        rname = request.POST.get("rname")
        rdes = request.POST.get("rdes")
        rphot = request.FILES.get('rphot')
        #updating
        queryset.rname =rname
        queryset.rdes =rdes
        if rphot:

            queryset.rname =rname
        queryset.save()
        return redirect("/vege")

    return render(request,"update.html",context)
#dumy api
from rest_framework.decorators import api_view
@api_view(["GET","POST"])
def api_home(request):
    if request.method=="GET":
        return Response({"message": "Hello, world!"})
    elif request.method=="POST":
        data = request.data
        print(data)
        return Response({"message": "Hell0"})
    
