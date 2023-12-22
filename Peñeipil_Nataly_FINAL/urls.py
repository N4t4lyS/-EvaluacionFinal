from django.urls import path
from seminario_app.views import (
    InscritoListCreateView, InscritoDetailView,
    InstitucionListCreateView, InstitucionDetailView,
    home
)

urlpatterns = [
    path('inscritos/', InscritoListCreateView.as_view(), name='inscrito-list-create'),
    path('inscritos/<int:pk>/', InscritoDetailView.as_view(), name='inscrito-detail'),
    path('instituciones/', InstitucionListCreateView.as_view(), name='institucion-list-create'),
    path('instituciones/<int:pk>/', InstitucionDetailView.as_view(), name='institucion-detail'),
    path('', home, name='pagina_principal'),
]