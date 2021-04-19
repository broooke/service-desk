from django.urls import path
from portal import views

urlpatterns = [
    path('', views.ApplicationsView.as_view(), name='applications'),
    path('others/', views.OthersView.as_view(), name='others'),
    path('add/application/', views.AddApplicationView.as_view(), name='add-application'),
    path('login/', views.SignInView.as_view(), name='login'),
    path('logout/', views.LogOutView.as_view(), name='logout'),
    path('panel/admin/', views.AdminPanelView.as_view(), name='admin-panel'),
    path('done/application/<str:pk>/', views.DoneApplicationView.as_view(), name='done-app')
]