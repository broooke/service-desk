from django.urls import path
from portal import views

urlpatterns = [
    path('', views.ApplicationsView.as_view(), name='applications'),
    path('others/', views.OthersView.as_view(), name='others'),
    path('add/application/', views.AddApplicationView.as_view(), name='add-application'),
]