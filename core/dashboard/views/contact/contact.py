from django.views import View
from django.shortcuts import render

class ContactView(View):
    def get(self, request):
        return render(request, 'contacto.html')

    def post(self, request):
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')
        return render(request, 'contacto.html', {'success': True})