from django.urls import path, include
from . import views

app_name = 'my_app'

urlpatterns = [
    
    path('/',views.home,name='home'),
    path('add_task/',views.add_todo,name='todo'),
]
