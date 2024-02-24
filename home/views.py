from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("hi iam suraj")
    #now bind this method with url in url section (project url section)
#now we are return a html index page
def page(request):
    return render(request,"index.html")
def page2(request):
    people = [
        {"name":"suraj","age":10 ,"text":"hi i am suraj and you?"},
        {"name":"akansha","age":14,"text":"hi i am akansha and you?"},
        {"name":"satyam","age":8,"text":"hi i am satyam and you?"},
    ]
    name1 = ["suraj","bauwa","akansha","kuttu"]
    return render(request,"index.html",context={"people":people,"name":name1})