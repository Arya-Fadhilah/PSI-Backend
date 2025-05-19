from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path("pasien/", views.pasien, name="pasien"),
    path("pasien/dataMCU/", views.mcurecord, name="mcurecord"),
    path("pasien/tambah_pasien/", views.tambah, name='tambahpasien'),
    path('pasien/edit/', views.edit, name='editpasien'),
    path('pasien/delete/', views.delete, name='hapuspasien'),
]
