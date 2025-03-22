from django.urls import path
from . import views  # Mengimpor views dari aplikasi landing

urlpatterns = [
    path('home/', views.home, name='home'),  # URL untuk home
    path('about/', views.about, name='about'),  # URL untuk about
]
