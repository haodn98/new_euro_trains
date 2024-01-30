from django.contrib import admin
from django.urls import path, include
from . import views
from routes.views import find_routes, add_route, save_route, RouteListView, RouteDetail, RouteDeleteView

urlpatterns = [
    path('find_routes/', find_routes, name="find_routes"),
    path('add_route/', add_route, name="add_route"),
    path('save_route/', save_route, name="save_route"),
    path('all_routes/', RouteListView.as_view(), name="all_routes"),
    path('detail/<int:pk>/', RouteDetail.as_view(), name="route_detail"),
    path('delete/<int:pk>/', RouteDeleteView.as_view(), name="route_delete"),
]
