from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from . import views
from .views import custom_logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('homepage', views.homepage, name='homepage'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('help/', views.help, name='help'),
    path('profile/', views.profile, name='profile'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)