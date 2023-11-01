from . import views
from django.urls import path

urlpatterns = [
    path('', views.Advocate_list),
    path('<str:username>/', views.Advocate_detail)
]