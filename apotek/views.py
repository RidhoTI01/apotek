from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import json
import os
from datetime import datetime
import random

# Path untuk menyimpan data lokal
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
os.makedirs(DATA_DIR, exist_ok=True)

PRODUK_FILE = os.path.join(DATA_DIR, 'produk.json')
PESANAN_FILE = os.path.join(DATA_DIR, 'pesanan.json')
USERS_FILE = os.path.join(DATA_DIR, 'users.json')
KATEGORI_FILE = os.path.join(DATA_DIR, 'kategori.json')

DEFAULT_PRODUK = [
    {
        'id': 1,
        'nama': 'Paracetamol 500mg',
        'kategori': 'Obat Bebas',
        'harga': 15000,
        'stok': 100,
        'deskripsi': 'Obat pereda demam dan nyeri',
        'gambar': 'https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80'
    },
    {
        'id': 2,
        'nama': 'Amoxicillin 500mg',
        'kategori': 'Obat Keras',
        'harga': 50000,
        'stok': 50,
        'deskripsi': 'Antibiotik untuk infeksi bakteri',
        'gambar': 'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80'
    },
    {
        'id': 3,
        'nama': 'Vitamin C 1000mg',
        'kategori': 'Suplemen',
        'harga': 35000,
        'stok': 200,
        'deskripsi': 'Suplemen vitamin C untuk daya tahan tubuh',
        'gambar': 'https://images.unsplash.com/photo-1584017911766-d451b3d0e843?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80'
    },
    {
        'id': 4,
        'nama': 'Betadine Solution 30ml',
        'kategori': 'Obat Luar',
        'harga': 25000,
        'stok': 75,
        'deskripsi': 'Antiseptik untuk luka luar',
        'gambar': '../static/images_produk/betadine.jpeg'
    },
    {
        'id': 5,
        'nama': 'Obat Batuk Hitam 60ml',
        'kategori': 'Obat Bebas',
        'harga': 18000,
        'stok': 120,
        'deskripsi': 'Obat batuk berdahak',
        'gambar': 'https://images.unsplash.com/photo-1583418855867-9d3a7d939d59?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80'
    },
]

# Default user admin
DEFAULT_USERS = [
    {
        'username': 'admin',
        'password': 'admin123',
        'email': 'admin@apotek.com'
    }
]

# Default kategori
DEFAULT_KATEGORI = [
    {'id': 1, 'nama': 'Obat Bebas', 'deskripsi': 'Obat yang dapat dibeli tanpa resep dokter'},
    {'id': 2, 'nama': 'Obat Keras', 'deskripsi': 'Obat yang memerlukan resep dokter'},
    {'id': 3, 'nama': 'Suplemen', 'deskripsi': 'Suplemen dan vitamin kesehatan'},
    {'id': 4, 'nama': 'Obat Luar', 'deskripsi': 'Obat untuk penggunaan luar seperti salep dan antiseptik'},
]

# Fungsi helper untuk membaca/menulis data
def load_produk():
    if os.path.exists(PRODUK_FILE):
        with open(PRODUK_FILE, 'r') as f:
            return json.load(f)
    else:
        save_produk(DEFAULT_PRODUK)
        return DEFAULT_PRODUK

def save_produk(data):
    with open(PRODUK_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def load_pesanan():
    if os.path.exists(PESANAN_FILE):
        with open(PESANAN_FILE, 'r') as f:
            return json.load(f)
    return []

def save_pesanan(data):
    with open(PESANAN_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    else:
        save_users(DEFAULT_USERS)
        return DEFAULT_USERS

def save_users(data):
    with open(USERS_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def about_us(request):
    team_members = [
        {
            'name': 'Fabian Damar Setiawan',
            'role': 'Project Manager',
            'image': 'images_teams/damar.jpeg',
            'description': 'Mengkoordinasi seluruh proses pengembangan website dan memastikan timeline berjalan sesuai rencana.'
        },
        {
            'name': 'Alya Dwi Cahyani',
            'role': 'Frontend Developer',
            'image': 'images_teams/alya.jpeg',
            'description': 'Bertanggung jawab dalam desain UI/UX dan implementasi antarmuka pengguna yang responsif.'
        },
        {
            'name': 'Muhammad Taufiq Ridho',
            'role': 'Backend Developer',
            'image': 'images_teams/ridho.jpeg',
            'description': 'Mengembangkan sistem database, logika bisnis, dan fitur-fitur utama website.'
        },
        {
            'name': 'Muhamad Fauzan Bagaskara',
            'role': 'Content Specialist',
            'image': 'images_teams/bagas.jpeg',
            'description': 'Menyusun konten produk, artikel kesehatan, dan informasi medis yang akurat.'
        }
    ]

    context = {
        'team_members': team_members,
    }

    return render(request, 'about_us.html', context)

def gallery(request):
    return render(request, 'gallery.html')

def load_kategori():
    if os.path.exists(KATEGORI_FILE):
        with open(KATEGORI_FILE, 'r') as f:
            return json.load(f)
    else:
        save_kategori(DEFAULT_KATEGORI)
        return DEFAULT_KATEGORI

def save_kategori(data):
    with open(KATEGORI_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def get_produk_by_id(pk):
    produk_list = load_produk()
    for p in produk_list:
        if p['id'] == pk:
            return p
    return None

def get_kategori_by_id(pk):
    kategori_list = load_kategori()
    for k in kategori_list:
        if k['id'] == pk:
            return k
    return None

# Auth views
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        users = load_users()
        user_found = False
        
        for user in users:
            if user['username'] == username and user['password'] == password:
                user_found = True
                request.session['logged_in'] = True
                request.session['username'] = username
                messages.success(request, f'Selamat datang, {username}!')
                return redirect('dashboard')
        
        if not user_found:
            messages.error(request, 'Username atau password salah!')
    
    if request.session.get('logged_in'):
        return redirect('dashboard')
    
    return render(request, 'login.html')

def logout_view(request):
    request.session.flush()
    messages.success(request, 'Anda telah logout')
    return redirect('home')

# Decorator untuk proteksi halaman dashboard
def login_required_custom(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('logged_in'):
            messages.error(request, 'Silakan login terlebih dahulu')
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper

# Views untuk customer
def home(request):
    produk_list = load_produk()
    return render(request, 'home.html', {'produk_list': produk_list[:6]})

def produk_list(request):
    produk_list = load_produk()
    kategori = request.GET.get('kategori', '')
    
    if kategori:
        produk_list = [p for p in produk_list if p['kategori'] == kategori]
    
    kategori_list = load_kategori()
    return render(request, 'produk_list.html', {
        'produk_list': produk_list, 
        'kategori': kategori,
        'kategori_list': kategori_list
    })

def produk_detail(request, pk):
    produk = get_produk_by_id(pk)
    if not produk:
        messages.error(request, 'Produk tidak ditemukan')
        return redirect('produk_list')
    return render(request, 'produk_detail.html', {'produk': produk})

def keranjang(request):
    keranjang = request.session.get('keranjang', {})
    produk_list = load_produk()
    
    items = []
    subtotal = 0
    for produk_id, qty in keranjang.items():
        produk = get_produk_by_id(int(produk_id))
        if produk:
            item_subtotal = produk['harga'] * qty
            items.append({
                'produk': produk,
                'qty': qty,
                'subtotal': item_subtotal
            })
            subtotal += item_subtotal
    
    # Hitong ongkir (gratis jika subtotal >= 100000)
    ongkir = 0 if subtotal >= 100000 else 15000
    total = subtotal + ongkir
    
    return render(request, 'keranjang.html', {
        'items': items, 
        'subtotal': subtotal,
        'ongkir': ongkir,
        'total': total,
        'is_free_ongkir': subtotal >= 100000
    })

def tambah_keranjang(request, pk):
    keranjang = request.session.get('keranjang', {})
    produk = get_produk_by_id(pk)
    
    if not produk:
        messages.error(request, 'Produk tidak ditemukan')
        return redirect('produk_list')
    
    produk_id = str(pk)
    if produk_id in keranjang:
        keranjang[produk_id] += 1
    else:
        keranjang[produk_id] = 1
    
    request.session['keranjang'] = keranjang
    messages.success(request, f'{produk["nama"]} ditambahkan ke keranjang')
    return redirect('keranjang')

def hapus_keranjang(request, pk):
    keranjang = request.session.get('keranjang', {})
    produk_id = str(pk)
    
    if produk_id in keranjang:
        del keranjang[produk_id]
        request.session['keranjang'] = keranjang
        messages.success(request, 'Produk dihapus dari keranjang')
    
    return redirect('keranjang')

# Tambahkan setelah fungsi hapus_keranjang
def update_keranjang(request, pk):
    if request.method == 'POST':
        keranjang = request.session.get('keranjang', {})
        produk = get_produk_by_id(pk)
        
        if not produk:
            messages.error(request, 'Produk tidak ditemukan')
            return redirect('keranjang')
        
        try:
            new_qty = int(request.POST.get('qty', 1))
            
            if new_qty <= 0:
                # Jika quantity 0 atau kurang, hapus dari keranjang
                produk_id = str(pk)
                if produk_id in keranjang:
                    del keranjang[produk_id]
                    messages.success(request, f'{produk["nama"]} dihapus dari keranjang')
            else:
                # Cek stok
                if new_qty > produk['stok']:
                    messages.error(request, f'Stok {produk["nama"]} hanya tersedia {produk["stok"]} unit')
                    return redirect('keranjang')
                
                # Update quantity
                keranjang[str(pk)] = new_qty
                messages.success(request, f'Jumlah {produk["nama"]} diupdate menjadi {new_qty}')
            
            request.session['keranjang'] = keranjang
            request.session.modified = True
            
        except ValueError:
            messages.error(request, 'Jumlah harus berupa angka')
    
    return redirect('keranjang')

# Update fungsi checkout di views.py
def checkout(request):
    if request.method == 'POST':
        keranjang = request.session.get('keranjang', {})
        if not keranjang:
            messages.error(request, 'Keranjang kosong')
            return redirect('keranjang')
        
        nama = request.POST.get('nama')
        alamat = request.POST.get('alamat')
        telepon = request.POST.get('telepon')
        
        # Hitung subtotal
        items = []
        subtotal = 0
        for produk_id, qty in keranjang.items():
            produk = get_produk_by_id(int(produk_id))
            if produk:
                item_subtotal = produk['harga'] * qty
                items.append({
                    'produk_id': produk['id'],
                    'nama': produk['nama'],
                    'qty': qty,
                    'harga': produk['harga'],
                    'subtotal': item_subtotal
                })
                subtotal += item_subtotal
        
        # Hitung ongkir
        ongkir = 0 if subtotal >= 100000 else 15000
        total = subtotal + ongkir
        
        pesanan_list = load_pesanan()
        pesanan_id = len(pesanan_list) + 1
        
        pesanan = {
            'id': pesanan_id,
            'nama': nama,
            'alamat': alamat,
            'telepon': telepon,
            'items': items,
            'subtotal': subtotal,
            'ongkir': ongkir,
            'total': total,
            'status': 'Pending',
            'tanggal': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        pesanan_list.append(pesanan)
        save_pesanan(pesanan_list)
        
        request.session['keranjang'] = {}
        messages.success(request, f'Pesanan berhasil! Nomor pesanan: {pesanan_id}')
        return redirect('home')
    
    # GET request - tampilkan form checkout
    keranjang = request.session.get('keranjang', {})
    if not keranjang:
        messages.error(request, 'Keranjang kosong')
        return redirect('keranjang')
    
    # Hitung total untuk ditampilkan
    items = []
    subtotal = 0
    for produk_id, qty in keranjang.items():
        produk = get_produk_by_id(int(produk_id))
        if produk:
            item_subtotal = produk['harga'] * qty
            items.append({
                'produk': produk,
                'qty': qty,
                'subtotal': item_subtotal
            })
            subtotal += item_subtotal
    
    ongkir = 0 if subtotal >= 100000 else 15000
    total = subtotal + ongkir
    
    return render(request, 'checkout.html', {
        'items': items,
        'subtotal': subtotal,
        'ongkir': ongkir,
        'total': total,
        'is_free_ongkir': subtotal >= 100000
    })

# Views untuk admin dashboard (dengan proteksi login)
@login_required_custom
def dashboard(request):
    produk_list = load_produk()
    pesanan_list = load_pesanan()
    kategori_list = load_kategori()
    
    total_produk = len(produk_list)
    total_pesanan = len(pesanan_list)
    total_pendapatan = sum(p['total'] for p in pesanan_list)
    total_kategori = len(kategori_list)
    
    context = {
        'total_produk': total_produk,
        'total_pesanan': total_pesanan,
        'total_pendapatan': total_pendapatan,
        'total_kategori': total_kategori,
        'pesanan_terbaru': pesanan_list[-5:][::-1] if pesanan_list else [],
        'username': request.session.get('username')
    }
    return render(request, 'dashboard/dashboard.html', context)

@login_required_custom
def dashboard_produk(request):
    produk_list = load_produk()
    return render(request, 'dashboard/produk.html', {
        'produk_list': produk_list,
        'username': request.session.get('username')
    })

@login_required_custom
def dashboard_produk_tambah(request):
    if request.method == 'POST':
        produk_list = load_produk()
        new_id = max([p['id'] for p in produk_list]) + 1 if produk_list else 1
        
        produk = {
            'id': new_id,
            'nama': request.POST.get('nama'),
            'kategori': request.POST.get('kategori'),
            'harga': int(request.POST.get('harga')),
            'stok': int(request.POST.get('stok')),
            'deskripsi': request.POST.get('deskripsi'),
            'gambar': request.POST.get('gambar', 'https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80')  # Default image
        }
        
        produk_list.append(produk)
        save_produk(produk_list)
        messages.success(request, 'Produk berhasil ditambahkan')
        return redirect('dashboard_produk')
    
    kategori_list = load_kategori()
    return render(request, 'dashboard/produk_form.html', {
        'username': request.session.get('username'),
        'kategori_list': kategori_list
    })

@login_required_custom
def dashboard_produk_edit(request, pk):
    produk = get_produk_by_id(pk)
    if not produk:
        messages.error(request, 'Produk tidak ditemukan')
        return redirect('dashboard_produk')
    
    if request.method == 'POST':
        produk_list = load_produk()
        for i, p in enumerate(produk_list):
            if p['id'] == pk:
                produk_list[i]['nama'] = request.POST.get('nama')
                produk_list[i]['kategori'] = request.POST.get('kategori')
                produk_list[i]['harga'] = int(request.POST.get('harga'))
                produk_list[i]['stok'] = int(request.POST.get('stok'))
                produk_list[i]['deskripsi'] = request.POST.get('deskripsi')
                produk_list[i]['gambar'] = request.POST.get('gambar', p['gambar'])
                break
        
        save_produk(produk_list)
        messages.success(request, 'Produk berhasil diupdate')
        return redirect('dashboard_produk')
    
    kategori_list = load_kategori()
    return render(request, 'dashboard/produk_form.html', {
        'produk': produk,
        'username': request.session.get('username'),
        'kategori_list': kategori_list
    })

@login_required_custom
def dashboard_produk_hapus(request, pk):
    produk_list = load_produk()
    produk_list = [p for p in produk_list if p['id'] != pk]
    save_produk(produk_list)
    messages.success(request, 'Produk berhasil dihapus')
    return redirect('dashboard_produk')

@login_required_custom
def dashboard_pesanan(request):
    pesanan_list = load_pesanan()
    return render(request, 'dashboard/pesanan.html', {
        'pesanan_list': pesanan_list[::-1],
        'username': request.session.get('username')
    })

# Views untuk manajemen kategori
@login_required_custom
def dashboard_kategori(request):
    kategori_list = load_kategori()
    produk_list = load_produk()
    
    # Hitung jumlah produk per kategori
    for kategori in kategori_list:
        kategori['jumlah_produk'] = len([p for p in produk_list if p['kategori'] == kategori['nama']])
    
    return render(request, 'dashboard/kategori.html', {
        'kategori_list': kategori_list,
        'username': request.session.get('username')
    })

@login_required_custom
def dashboard_kategori_tambah(request):
    if request.method == 'POST':
        kategori_list = load_kategori()
        new_id = max([k['id'] for k in kategori_list]) + 1 if kategori_list else 1
        
        kategori = {
            'id': new_id,
            'nama': request.POST.get('nama'),
            'deskripsi': request.POST.get('deskripsi')
        }
        
        kategori_list.append(kategori)
        save_kategori(kategori_list)
        messages.success(request, 'Kategori berhasil ditambahkan')
        return redirect('dashboard_kategori')
    
    return render(request, 'dashboard/kategori_form.html', {
        'username': request.session.get('username')
    })

@login_required_custom
def dashboard_kategori_edit(request, pk):
    kategori = get_kategori_by_id(pk)
    if not kategori:
        messages.error(request, 'Kategori tidak ditemukan')
        return redirect('dashboard_kategori')
    
    if request.method == 'POST':
        kategori_list = load_kategori()
        old_nama = None
        
        for i, k in enumerate(kategori_list):
            if k['id'] == pk:
                old_nama = k['nama']
                kategori_list[i]['nama'] = request.POST.get('nama')
                kategori_list[i]['deskripsi'] = request.POST.get('deskripsi')
                break
        
        save_kategori(kategori_list)
        
        # Update kategori di semua produk
        if old_nama:
            produk_list = load_produk()
            for i, p in enumerate(produk_list):
                if p['kategori'] == old_nama:
                    produk_list[i]['kategori'] = request.POST.get('nama')
            save_produk(produk_list)
        
        messages.success(request, 'Kategori berhasil diupdate')
        return redirect('dashboard_kategori')
    
    return render(request, 'dashboard/kategori_form.html', {
        'kategori': kategori,
        'username': request.session.get('username')
    })

@login_required_custom
def dashboard_kategori_hapus(request, pk):
    kategori = get_kategori_by_id(pk)
    if not kategori:
        messages.error(request, 'Kategori tidak ditemukan')
        return redirect('dashboard_kategori')
    
    # Cek apakah ada produk yang menggunakan kategori ini
    produk_list = load_produk()
    produk_dengan_kategori = [p for p in produk_list if p['kategori'] == kategori['nama']]
    
    if produk_dengan_kategori:
        messages.error(request, f'Tidak dapat menghapus kategori "{kategori["nama"]}" karena masih ada {len(produk_dengan_kategori)} produk yang menggunakannya')
        return redirect('dashboard_kategori')
    
    kategori_list = load_kategori()
    kategori_list = [k for k in kategori_list if k['id'] != pk]
    save_kategori(kategori_list)
    messages.success(request, 'Kategori berhasil dihapus')
    return redirect('dashboard_kategori')

def bmi_calculator(request):
    result = None

    if request.method == 'POST':
        try:
            berat = float(request.POST.get('berat'))
            tinggi = float(request.POST.get('tinggi')) / 100  # cm ke meter

            bmi = round(berat / (tinggi ** 2), 2)

            if bmi < 18.5:
                category = 'Kekurangan Berat Badan'
                advice = 'Anda perlu menambah berat badan. Konsultasikan dengan dokter atau ahli gizi.'
                css_class = 'bmi-under'
            elif 18.5 <= bmi < 25:
                category = 'Normal (Ideal)'
                advice = 'Berat badan Anda ideal! Pertahankan pola makan sehat dan rutin berolahraga.'
                css_class = 'bmi-normal'
            elif 25 <= bmi < 30:
                category = 'Kelebihan Berat Badan'
                advice = 'Anda memiliki kelebihan berat badan. Atur pola makan dan tingkatkan aktivitas fisik.'
                css_class = 'bmi-over'
            else:
                category = 'Obesitas'
                advice = 'Sangat disarankan berkonsultasi dengan dokter untuk program penurunan berat badan.'
                css_class = 'bmi-obese'

            result = {
                'bmi': bmi,
                'category': category,
                'advice': advice,
                'css_class': css_class,
                'berat': berat,
                'tinggi': tinggi * 100
            }

        except (ValueError, TypeError, ZeroDivisionError):
            messages.error(request, 'Mohon masukkan angka yang valid!')

    return render(request, 'bmi_calculator.html', {'result': result})