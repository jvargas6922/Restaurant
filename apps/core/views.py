from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def contador_visitas(request):
    # Obtener el número de visitas desde la sesión, o establecerlo en 0 si no existe
    visita = request.session.get('contador_visitas', 0)
    # Incrementar el contador de visitas y guardarlo de nuevo en la sesión
    request.session['contador_visitas'] = visita + 1
    # Devolver una respuesta con el número de visitas
    return HttpResponse(f'Número de visitas: {visita}')
