from django.urls import path
from . import views

urlpatterns = [
    path('',views.new_app,name='new_app'),

]
