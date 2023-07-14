from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso, Profesor,Entregable,Estudiante
from AppCoder.forms import CursoFormulario, ProfesorFormulario , EstudiantesFormulario, EntregableFormulario

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
        #return render (request, 'resultadosBusqueda.html', {'cursos': cursos, 'camada': camada})
        return render (request, 'inicio.html', {'cursos': cursos, 'camada': camada})
    else:
        respuesta = "no enviaste datos"

    #return HttpResponse (respuesta)
    return render (request, 'inicio.html', {'respuesta' : respuesta})



def busquedaProfesores(request):
    return render(request, 'busquedaProfesores.html')



def buscarProfesores (request):
    if request.GET['profesor']:
        nombre = request.GET['nombre']
        apellido = Curso.objects.filter(apellido__icontains=apellido)
        return render (request, 'profesorFormulario.html', {'nombre': nombre, 'apellido': apellido})
    else:
        respuesta = "no enviaste datos"

    return render (request, 'profesorFormulario.html', {'respuesta' : respuesta})


        
def estudiantesFormulario(request):
    if request.method == "POST":
        miFormulario = EstudiantesFormulario(request.POST) 
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            estudiante = Estudiante(nombre=informacion['nombre'], 
                                    apellido=informacion['apellido'],)
            estudiante.save()
            return render(request, 'inicio.html')
    else:
        miFormulario = EstudiantesFormulario()
        return render(request, 'estudiantesFormulario.html', {'miFormulario':miFormulario})

def entregable(request):
    if request.method == "POST":
        miFormulario = (request.POST) 
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            entregable = Entregable(nombre=informacion['nombre'], 
                                    apellido=informacion['apellido'],)
            entregable.save()
            return render(request, 'inicio.html')
    else:
        miFormulario = EntregableFormulario()
        return render(request, 'entregableFormulario.html', {'miFormulario':miFormulario})        