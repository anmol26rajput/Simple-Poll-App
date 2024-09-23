from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vote/<int:pk>/', views.vote, name='vote'),  # Changed to <int:pk> and added trailing slash
    path('result/<int:pk>/', views.result, name='result'),  # Changed to <int:pk> and added trailing slash
    path('final_result/', views.result_view, name='final_result'),  # Added final_result view
]
