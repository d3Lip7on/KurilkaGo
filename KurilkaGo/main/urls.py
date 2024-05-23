from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('cigarettes/<int:page>',views.cigarettes),
    path('cigarette/<int:id>', views.cigarette)
]