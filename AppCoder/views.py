from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso, Profesor
from AppCoder.forms import CursoFormulario, ProfesorFormulario
# Create your views here.

def curso(self):
    curso = Curso(nombre='Desarrollo Web', camada= '19881')
    curso.save()
    documentodeTexto = f'---->Curso: {curso.nombre} Camada: {curso.camada}'
    return HttpResponse(documentodeTexto)

def inicio(request):
    return render(request,'inicio.html')

#def cursos(request):
 #   return render(request,'cursos.html')

def profesores(request):
    return render(request, 'profesores.html')

def estudiantes(request):
    return render (request,'estudiantes.html')

def entregables(request):
    return render (request,'entregables.html')


def cursos(request):

    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST) #donde llega la info del html
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion['nombre'], camada=informacion['camada'])
            curso.save()
            return render(request, 'inicio.html')

    else:
        miFormulario = CursoFormulario()

    return render (request,'cursos.html', {'miFormulario':miFormulario})

       
def profesorFormulario(request):
    if request.method == "POST":
        miFormulario = ProfesorFormulario(request.POST) 
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], 
                                apellido=informacion['apellido'],
                                email=informacion['email'],
                                profesion=informacion['profesion'])
            profesor.save()
            return render(request, 'inicio.html')
    else:
        miFormulario = ProfesorFormulario()
    return render(request, 'profesorFormulario.html', {'miFormulario':miFormulario})

def busquedaCamada(request):
    return render(request, 'busquedaCamada.html')

def buscar (request):
    if request.GET['camada']:
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=camada)
        return render (request, 'resultadosBusqueda.html', {'cursos': cursos, 'camada': camada})
    else:
        respuesta = "no enviaste datos"

    return HttpResponse (respuesta)