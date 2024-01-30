from django.urls import path
from . import views

urlpatterns = [

    path('', views.TrainListView.as_view(), name='all_trains'),
    path('detail/<int:pk>/', views.TrainDetailView.as_view(), name='train_detail'),
    path('add/', views.TrainCreateView.as_view(), name='train_add'),
    path('update/<int:pk>/', views.TrainUpdateView.as_view(), name='train_update'),
    path('delete/<int:pk>/', views.TrainDeleteView.as_view(), name='train_delete'),

]
