from . import views
from django.urls import path

urlpatterns = [
    path('', views.Advocate_list.as_view(), name='advocates'),
    path('<str:username>/', views.Advocate_detail.as_view())
]