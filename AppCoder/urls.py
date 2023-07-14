from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name='inicio'), 
    path('cursos', views.cursos, name='Cursos'),
    path('profesores', views.profesores, name='Profesores'),
    path('estudiantes', views.estudiantes, name='Estudiantes'),
    path('entregables', views.entregables, name='Entregables'),
    #path('cursoFormulario', views.cursoFormulario, name='CursoFormulario'),
    path('profesorFormulario', views.profesorFormulario, name='ProfesorFormulario'),
    path('busquedaCamada', views.busquedaCamada, name='BusquedaCamada'),
    path('buscar/', views.buscar),
    path('estudiantesFormulario', views.estudiantesFormulario, name='EstudiantesFormulario'),
    path('buscarProfesores/', views.buscarProfesores, name='buscarProfesores'),
    path('busquedaProfesores/', views.busquedaProfesores, name='busquedaProfesores'),
    path('entregables/', views.entregable, name='entregable'),




    
    
]