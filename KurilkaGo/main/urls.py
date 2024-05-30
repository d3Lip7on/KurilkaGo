from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('cigarettes/<int:page>', views.getCigarettes,  name='get_cigarettes'),
    path('cigarette/<int:id>', views.getCigarette),
    path('disposablevapes/<int:page>', views.getDisposableVapes),
    path('disposablevape/<int:id>', views.getDisposableVape),
    path('hookahs/<int:page>', views.getHookahs),
    path('hookah/<int:id>', views.getHookah),
    path('iqoses/<int:page>', views.getIqoses),
    path('iqos/<int:id>', views.getIqos),
    path('liquids/<int:page>', views.getLiquids),
    path('liquid/<int:id>', views.getLiquid),
    path('vapes/<int:page>', views.getVapes),
    path('vape/<int:id>', views.getVape),
    path('about', views.about)
]