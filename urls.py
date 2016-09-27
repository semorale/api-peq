# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework import routers
import views
from .views import MedicionLast, MedicionAdd, AsignarToken

router = routers.DefaultRouter()
router.register(r'equipos', views.EquiposViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'mediciones',views.MedicionesViewSet)

urlpatterns = [
	url('^asignar_token/$', AsignarToken.as_view(), name="Asignar Token" ),
	url('^mediciones/(?P<indicador>.+)/last/$', MedicionLast.as_view()),
	url('^mediciones/add/$', MedicionAdd.as_view()),
	url(r'^', include(router.urls)),
]