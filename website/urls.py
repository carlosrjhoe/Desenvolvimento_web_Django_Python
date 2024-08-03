from django.urls import path
from .views import FuncionariosListView
from .views import IndexTemplateView
from .views import FuncionarioUpdateView

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
    path('atualiza/<id>', 
        FuncionarioUpdateView.as_view(),
        name='atualiza'
    ),
]
