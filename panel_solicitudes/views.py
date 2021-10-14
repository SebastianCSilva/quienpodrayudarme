from django.shortcuts import render

# Create your views here.
def maestros_lista(request):
    return render(request, 'panel_solicitudes/templates/maestros_lista.html', {})