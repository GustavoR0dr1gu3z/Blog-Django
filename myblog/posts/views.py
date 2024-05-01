from django.http import HttpResponse
from django.views.generic.base import View

class bienvenidaAdmin(View):
    def get(self, response):
        return HttpResponse(
            content="Hola soy gustavo"
        )