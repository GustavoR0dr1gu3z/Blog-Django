from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render

class bienvenidaAdmin(View):
    def get(self, request):
        data = {
            'name': 'Calzada',
            'year': 24,
            'codes': ['Python', 'Django', 'Lit']
        }
        return render(request, 'msjBienvenida.html', context=data)