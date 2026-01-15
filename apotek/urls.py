from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('produk/', views.produk_list, name='produk_list'),
    path('produk/<int:pk>/', views.produk_detail, name='produk_detail'),
    path('keranjang/', views.keranjang, name='keranjang'),
    path('tambah-keranjang/<int:pk>/', views.tambah_keranjang, name='tambah_keranjang'),
    path('keranjang/update/<int:pk>/', views.update_keranjang, name='update_keranjang'),
    path('hapus-keranjang/<int:pk>/', views.hapus_keranjang, name='hapus_keranjang'),
    path('checkout/', views.checkout, name='checkout'),

    path('about-us/', views.about_us, name='about_us'),
    path('gallery/', views.gallery, name='gallery'),
    
    # BMI Calculator
    path('bmi-calculator/', views.bmi_calculator, name='bmi_calculator'),
    
    # Auth
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Admin Dashboard (requires login)
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/produk/', views.dashboard_produk, name='dashboard_produk'),
    path('dashboard/produk/tambah/', views.dashboard_produk_tambah, name='dashboard_produk_tambah'),
    path('dashboard/produk/edit/<int:pk>/', views.dashboard_produk_edit, name='dashboard_produk_edit'),
    path('dashboard/produk/hapus/<int:pk>/', views.dashboard_produk_hapus, name='dashboard_produk_hapus'),
    path('dashboard/pesanan/', views.dashboard_pesanan, name='dashboard_pesanan'),
    
    # Manajemen Kategori
    path('dashboard/kategori/', views.dashboard_kategori, name='dashboard_kategori'),
    path('dashboard/kategori/tambah/', views.dashboard_kategori_tambah, name='dashboard_kategori_tambah'),
    path('dashboard/kategori/edit/<int:pk>/', views.dashboard_kategori_edit, name='dashboard_kategori_edit'),
    path('dashboard/kategori/hapus/<int:pk>/', views.dashboard_kategori_hapus, name='dashboard_kategori_hapus'),
]