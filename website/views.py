from django.db.models.base import Model as Model
from django.urls import reverse_lazy
from .models import Funcionario
from .forms import InsereFuncionarioForm
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import CreateView


class FuncionarioCreateView(CreateView):
    template_name = 'website/criar.html'
    model = Funcionario
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy('website:lista')
    

class FuncionarioDeleteView(DeleteView):
    template_name = 'website/exclui.html'
    model = Funcionario
    context_object_name = 'funcionario'
    success_url = reverse_lazy('website:lista')


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
    context_object_name = 'funcionarios'

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
    