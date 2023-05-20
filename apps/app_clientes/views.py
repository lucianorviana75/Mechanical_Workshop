import re
from django.shortcuts import render
from django.http import HttpResponse
from.models import Cliente,Carro

# Create your views here.
def clientes(request):
    if request.method == "GET":
        return render(request, 'clientes.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        carro = request.POST.getlist('carro')
        placa = request.POST.getlist('placa')
        ano = request.POST.getlist('ano')
        
        clientes = Cliente.objects.filter(cpf=cpf)
        
        if clientes.exists():
            return render(request,'clientes.html',{'nome': nome,'sobrenome': sobrenome,'email': email, 'carro':zip(carro,placa,ano)})
        
        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
            return render(request,'clientes.html',{'nome': nome,'sobrenome': sobrenome,'cpf': cpf, 'carro':zip(carro,placa,ano)})
        
        clientes = Cliente(
            nome = nome,
            sobrenome = sobrenome,
            email = email,
            cpf = cpf
        )
        
        clientes.save()
        
        for carro,placa,ano in zip(carro,placa,ano):
          car = Carro(carro=carro, placa=placa, ano=ano, cliente=clientes)
          car.save()
          
        return HttpResponse('Cadastro feito com sucesso')
        
      
        
       