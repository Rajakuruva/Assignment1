from django.urls import path
from Andhra.views import *
app_name='Andhra'

urlpatterns=[
    path('States/',States,name='States'),
    path('Festivals/',Festivals,name='Festivals'),
    path('History/',History,name='History'),
    path('Culture/',Culture,name='Culture'),
]