from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Funcionario
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import UpdateView

# Create your views here.
# """Usando (Function Based Views"""
# def lista_funcionarios(request):
#     # Buscar funcionários
#     funcionarios = Funcionario.objetos.all()

#     # Incluindo contexto
#     contexto = {
#         'funcionarios': funcionarios,
#     }
    
#     # Retornando o template para listar os funcionarios
#     return render(request, 'website/funcionarios.html', contexto)

def criar_funcionario(request, pk):
    # VERIFICAR SE O METODOD É POST
    if request.method == 'POST':
        form = FormularioDeCriacao(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lista_funcionarios'))
    else:
        # Qualquer outro método: GET, OPTION, DELETE, etc...
        return render(request, 'website/form.html', {'form': form})

class IndexTemplateView(TemplateView):
    template_name = 'website/index.html'
    

"""Usando Class Based Views"""
class FuncionariosListView(ListView):
    model = Funcionario
    template_name = 'website/lista.html'
    context_object_name = 'funcionarios'


class FuncionarioUpdateView(UpdateView):
    template_name = 'website/atualiza.html'
    model = Funcionario
    fields = ['__all__']
    context_object_name = 'funcionario'

    def get_object(self, queryset=None):
        funcionario = None

        # Os campos {pk} e {slug} estão presentes em self.kwargs
        id = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)

        if id is not None:
            # Busca o funcionario apartir do id
            funcionario = Funcionario.objects.filter(id=id).first()
        elif slug is not None:
            # Pega o campo slug do Model
            campo_slug = self.get_slug_field()
            # Busca o funcionario apartir do slug
            funcionario = Funcionario.objects.filter(
                **{campo_slug: slug}
            ).first()
            
        return funcionario
    