from django.shortcuts import render
from django.contrib import messages
from .forms import ContatoForm, produtoModelForm

def index(request):
    return render(request, 'index.html')

def contato(request):
    form = ContatoForm(request.POST or None)
    
    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()
            # nome = form.cleaned_data['nome']
            # email = form.cleaned_data['email']
            # assunto = form.cleaned_data['assunto']
            # mensagem = form.cleaned_data['mensagem']

            # print('Mensagem enviada')
            # print(f'Nome: {nome}')
            # print(f'E-mail: {email}')
            # print(f'Assunto: {assunto}')
            # print(f'Mensagem: {mensagem}')

            messages.success(request, 'Formulario enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar formulario')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

def produto(request):
    if str(request.method) == 'Post':
        form = produtoModelForm(request.POST, request.FILES)
        if form.is_valid():
            prod = form.save(commit=False)

            print(f'Nome: {prod.name}')
            print(f'Preco: {prod.preco}')
            print(f'Estoque: {prod.estoque}')
            print(f'Imagem: {prod.imagem}')

            messages.success(request, 'Cadastro realizado com sucesso.')
        else:
            messages.error(request, 'Erro ao cadastrar produto.')
    else:
        form = produtoModelForm()
    context = {
        'form': form
    }
    return render(request, 'produto.html', context)