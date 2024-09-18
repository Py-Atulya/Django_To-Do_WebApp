from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('get_todo/',views.get_todo_lits,name='get_todo'),
    path('remove_todo/<int:id>/',views.remove_todo_item,name='remove_todo_item')
]