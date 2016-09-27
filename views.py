from django.contrib.auth.models import User
from rest_framework import viewsets
from api.serializers import UserSerializer, EquipoSerializer, MedicionesSerializer
from equipos.models import Equipo
from mediciones.models import Medicion
from rest_framework import generics
from rest_framework.authtoken.models import Token
from django.shortcuts import render_to_response, render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from usuarios.models import UserProfile
from .forms import GenerarToken
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EquiposViewSet(viewsets.ModelViewSet):
	queryset = Equipo.objects.all()
	serializer_class = EquipoSerializer

class MedicionesViewSet(viewsets.ModelViewSet):
	queryset = Medicion.objects.all()
	serializer_class = MedicionesSerializer

class MedicionLast(generics.ListAPIView):
    serializer_class = MedicionesSerializer
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        indicador = self.kwargs['indicador']
        retorno = Medicion.objects.filter(indicador=indicador).latest("timestamp")
        return [retorno]

class MedicionAdd(generics.CreateAPIView):
    model= Medicion
    serializer_class = MedicionesSerializer

class AsignarToken(SuccessMessageMixin,CreateView):
    models = Token
    form_class = GenerarToken
    template_name = 'generar_token.html'

    def get_success_url(self):
        return reverse('api:Asignar Token')

    def get_context_data(self, **kwargs):
        contexto = super(AsignarToken, self).get_context_data(**kwargs)
        contexto['action'] = reverse('api:Asignar Token')

        dict_usuarios_lista={}
        conjunto_con_token = set()
        conjunto_bot = set()

        usuarios_con_token = Token.objects.all().select_related("user")
        for i in usuarios_con_token:
            conjunto_con_token.add(i.user)

        perfiles_bot= UserProfile.objects.filter(tipo="Bot").select_related("user")
        for k in perfiles_bot:
            conjunto_bot.add(k.user)

        usuarios_aptos = conjunto_bot - conjunto_con_token

        for v in usuarios_aptos:
            dict_usuarios_lista[str(v.pk)] = v.username

        contexto['choices'] = dict_usuarios_lista
        return contexto

    success_message = 'Se ha generado el token correctamente'