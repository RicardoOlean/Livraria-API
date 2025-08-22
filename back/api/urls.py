from django.urls import path
from .views import *

urlpatterns = [
    path("authors" , listar_autores),
    path("publisher", listar_editoras),
    path("book", listar_livros),

    ####GET e POST ###########
    path('autores', AutoresView.as_view()),
    path("editoras", EditoraView.as_view()),
    path("livros", LivroView.as_view()),
    
    ############UPDATE e DELETE
    path('autor/<int:pk>', AutoresDetailView.as_view()),
    path('editora/<int:pk>', EditoraDetailView.as_view()),
    path('livros/<int:pk>', LivroDetailView.as_view),
]

