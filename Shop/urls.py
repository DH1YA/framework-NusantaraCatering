from django.urls import path
from Shop import views

urlpatterns = [
  path('Shop/', views.index)
]