from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='all_cities'),
    path('', views.CityListView.as_view(), name='all_cities'),
    path('detail/<int:pk>/', views.CityDetailView.as_view(), name='city_detail'),
    path('add/', views.CityCreateView.as_view(), name='city_add'),
    path('update/<int:pk>/', views.CityUpdateView.as_view(), name='city_update'),
    path('delete/<int:pk>/', views.CityDeleteView.as_view(), name='city_delete'),

]
