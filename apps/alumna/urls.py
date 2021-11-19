
from apps.alumna.models import Alumna
from django.urls import path

from apps.alumna.views import docente, estudiante, index

urlpatterns = [
    path(r'^$', index),
    path(r'^$', docente),
    path(r'^$', estudiante),
]