from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from . import views
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('advice/', views.advice, name='advice'),
    path('visualization/', views.visualization, name='visualization'),
    path('homepage/', views.homepage, name='homepage'),
    path('transaction_container/', views.transaction_container, name='transaction_container')

]