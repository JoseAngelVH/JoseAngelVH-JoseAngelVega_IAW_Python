from django.shortcuts import render, redirect
from .forms import UsuarioForm
from .models import Usuario
from openpyxl import Workbook
from django.http import HttpResponse

def inicio(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = UsuarioForm()
    
    return render(request, 'usuarios/formulario.html', {'form': form})

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/lista.html', {'usuarios': usuarios})

def exportar_excel(request):
    wb = Workbook()
    ws = wb.active
    ws.title = "Usuarios"

    # Cabecera
    ws.append(["Nombre"] + [f"Km {i}" for i in range(1, 11)])

    for u in Usuario.objects.all():
        ws.append([
            u.nombre, u.km1, u.km2, u.km3, u.km4,
            u.km5, u.km6, u.km7, u.km8, u.km9, u.km10
        ])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=usuarios.xlsx'
    wb.save(response)

    return response
