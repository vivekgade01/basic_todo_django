from django.urls import path, include
from . import views

app_name = 'my_app'

urlpatterns = [
    
    path('',views.home,name='home'),
    path('add_todo/', views.add_todo, name='todo'),
    path('delete_todo/<int:task_id>/', views.delete_todo, name='delete_todo'),
]
