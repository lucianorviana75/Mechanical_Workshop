from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def lista(request):
    if request.method == "get":
        nome = 'Luciano'
        return render(request,'index.html',{'nome': nome})
    elif request.method == "POST":
        nome=request.POST.get('name')
        idade=request.POST.get('idade')
        print(idade)
        
        return HttpResponse('fui chamado')
