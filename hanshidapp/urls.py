from django.urls import path,include
from .import views

urlpatterns = [
 path('hello',views.testfun,name='hello')
 
]
