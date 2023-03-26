from States.views import *
from django.urls import path
app_name='States'

urlpatterns=[
    path('Disticts/',Disticts,name='Disticts'),
    path('Rayal/',Rayal,name='Rayal'),
    path('Kosta/',Kosta,name='Kosta'),
]