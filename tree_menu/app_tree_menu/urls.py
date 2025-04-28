from django.urls import path
from . import views

urlpatterns = [
    path('<slug:item_slug>/', views.draw_menu, name='menu'),
    path('', views.draw_menu, name='main'),
]
