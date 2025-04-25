from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('menu/<slug:item_slug>/', views.switch_to_menu_item, name='menu')
]