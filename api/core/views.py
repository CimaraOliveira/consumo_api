from django.shortcuts import render
import requests 

def cadastro(request):
    return render(request, 'core/cadastro.html') 

def requisicao_api(request):
    if request.method == 'POST':
        cep = request.POST['cep']
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if response.status_code == 200:
            dados = response.json()
            return render(request, 'core/cep.html', {"dados": dados})

    return render(request, 'core/requisicao_api.html')
