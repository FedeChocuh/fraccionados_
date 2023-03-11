from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('niveles',views.niveles,name='niveles'),
    path('calificacion',views.calificacion,name='calificacion'),
    path('tiempo',views.tiempo,name='tiempo'),
    path('stats',views.stats,name='stats'),
    path('save',views.save,name='save') , 
    path('scoreboard',views.scoreboard,name='scoreboard'),
]
