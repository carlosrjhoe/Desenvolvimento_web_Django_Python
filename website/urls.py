from django.urls import path
from .views import IndexTemplateView
from .views import FuncionariosListView
from .views import FuncionarioUpdateView
from .views import FuncionarioDeleteView
from .views import FuncionarioCreateView

app_name = 'website'

urlpatterns = [
    path('',
        IndexTemplateView.as_view(),
        name = 'index'
    ),
    path('lista/',
        FuncionariosListView.as_view(),
        name='lista'
    ),
    path('atualiza/<int:id>', 
        FuncionarioUpdateView.as_view(),
        name='atualiza'
    ),
    path('funcionario/excluir/<int:pk>',
        FuncionarioDeleteView.as_view(),
        name='deletar_funcionario'
    ),
    path('funcionario/cadastrar/', 
        FuncionarioCreateView.as_view(),
        name='cadastrar_funcionario'
    ),
]
