from prettytable import PrettyTable
import os

dataSaham = []
dataSaham = [
        {'kode':'AADI',
        'perusahaan':'Adaro Andalan Indonesia Tbk.', 
        'hargaPembukaan':6550,
        'hargaPenutupan':6800,
        'perubahan':3.82, 
        'nilai':44460882500, 
        'hapus':False},

        {'kode':'AALI',
        'perusahaan':'Astra Agro Lestari Tbk.', 
        'hargaPembukaan':5675,
        'hargaPenutupan':5550,
        'perubahan':2.20, 
        'nilai':3764012500, 
        'hapus':False},

        {'kode':'BBCA',
        'perusahaan':'Bank Central Asia Tbk.',
        'hargaPembukaan':8275,
        'hargaPenutupan':7900,
        'perubahan':-4.53,
        'nilai':736670570000,
        'hapus':False},

        {'kode':'BBRI',
        'perusahaan':'Bank Rakyat Indonesia (Persero) Tbk.', 
        'hargaPembukaan':3930,
        'hargaPenutupan':5550,
        'perubahan':41.23, 
        'nilai':941219074000, 
        'hapus':False},
                
        {'kode':'BRIS',
        'perusahaan':'Bank Syariah Indonesia Tbk.', 
        'hargaPembukaan':2610,
        'hargaPenutupan':5550,
        'perubahan':112.22, 
        'nilai':85977800000, 
        'hapus':False},

        {'kode':'BMRI',
        'perusahaan':'Bank Mandiri (Persero) Tbk.', 
        'hargaPembukaan':4870,
        'hargaPenutupan':5550,
        'perubahan':13.97, 
        'nilai':570806151000, 
        'hapus':False},

        {'kode': 'AAPL', 
        'perusahaan': 'Apple Inc.', 
        'hargaPembukaan': 1450, 
        'hargaPenutupan': 1495, 
        'perubahan': 3.13, 
        'nilai': 2469100000000,
        'hapus': False},

        {'kode': 'AMZN', 
        'perusahaan': 'Amazon.com Inc.', 
        'hargaPembukaan': 3400, 
        'hargaPenutupan': 3450, 
        'perubahan': 1.47, 
        'nilai': 1740500000000,  
        'hapus': False},
        
        {'kode': 'TSLA', 
        'perusahaan': 'Tesla, Inc.', 
        'hargaPembukaan': 9005, 
        'hargaPenutupan': 9205, 
        'perubahan': 2.22, 
        'nilai': 860000000000,  
        'hapus': False},

        {'kode':'TLKM',
        'perusahaan':'Telkom Indonesia (Persero) Tbk.', 
        'hargaPembukaan':2430,
        'hargaPenutupan':5550,
        'perubahan':128.57, 
        'nilai':439964438000, 
        'hapus':False}
        ]

def bersihkan_layar():
        if os.name == 'nt':
                os.system('cls') # Windows
        else:
                os.system('clear') # Linux/macOS

def login():
        while True:
                bersihkan_layar()
                print('='*110)
                print(f"{'SELAMAT DATANG DI':^100}")
                print(f"{'SISTEM MANAJEMEN DATA SAHAM KONOHA':^100}")
                print('='*110)
                
                daftar_pengguna = {
                        'admin' : 'admin29',
                        'investor' : 'investor29'
                }

                # Login pengguna
                username = input('Status Pengguna : ')
                password = input(f'Kata Sandi\t: ')
                input('Tekan Enter untuk melanjutkan..')

                if daftar_pengguna.get(username) ==  password:
                        return username
                else:
                        print('\nStatus pengguna atau kata sandi yang Anda masukkan salah. Silakan coba lagi.\n')

# tampilan menu utama 
def menu_utama(pengguna):
        bersihkan_layar()
        while True:
                if pengguna == 'admin':
                        print('\n')
                        print('='*110)
                        print(f"{'SISTEM MANAJEMEN DATA SAHAM KONOHA':^100}")
                        print('='*110)

                        menu_admin = input('''
                                =====================================
                                  *** Manajemen Data Saham 2025 ***
                                =====================================
                                Daftar Menu Utama: 
                                =====================================
                                [1] Menampilkan Data Saham 
                                [2] Menambah Data Saham 
                                [3] Memperbarui Data Saham 
                                [4] Menghapus Data Saham           
                                [5] Keluar   
                                ======================================
                                => Pilih menu yang ingin Anda akses : ''')

                        if menu_admin == '1':
                                tampilkanData()
                        elif menu_admin == '2':
                                tambahData()
                        elif menu_admin == '3':
                                perbaruiData()
                        elif menu_admin == '4':
                                hapusData()
                        elif menu_admin == '5':
                                keluarSistem(pengguna)
                        else:
                                print('\n')
                                print(f"{'Opsi yang Anda pilih tidak tersedia. Pilih menu yang valid dan coba lagi.':^100}")
                                print(f"{'*'*3:^100}")
                                input(f"{'Tekan Enter untuk melanjutkan..':^99}")
                
                elif pengguna == 'investor':
                        print('\n')
                        print('='*110)
                        print(f"{'SISTEM MANAJEMEN DATA SAHAM KONOHA':^100}")
                        print('='*110)

                        menu_investor = input('''
                                =====================================
                                  *** Manajemen Data Saham 2025 ***
                                =====================================
                                Daftar Menu Utama: 
                                =====================================
                                [1] Menampilkan Data Saham 
                                [2] Keluar            
                                ======================================
                                => Pilih menu yang ingin Anda akses : ''')
                        
                        if menu_investor == '1':
                                tampilkanData()

                        elif menu_investor== '2':
                                keluarSistem(pengguna)
                        else:
                                print('\n')
                                print(f"{'Opsi yang Anda pilih tidak tersedia. Pilih menu yang valid dan coba lagi.':^100}")
                                print(f"{'*'*3:^100}")
                                input(f"{'Tekan Enter untuk melanjutkan..':^99}")                             

def nominal(angka):
        if isinstance(angka, str): 
                angka = angka.replace('.', '')
        angka = int(float(angka)) 
        return f'{angka:,.0f}'.replace(',', '.')  # Format nominal ribuan

def presentase(perubahan): 
        if isinstance(perubahan, str):
                perubahan = perubahan.replace('%', '') 
        return f'{float(perubahan):.2f}%' # Format presentase

# *******************************
# ********** READ DATA **********
# *******************************

def menampilkan(): 
        print('\n')
        Tabel = PrettyTable()
        Tabel.field_names = ['Kode Saham', 'Nama Perusahaan', 'Harga Pembukaan', 'Harga Penutupan', 'Perubahan Harga', 'Nilai Transaksi']
        Tabel.title = 'RINGKASAN PASAR SAHAM KONOHA 2025'
        
        if len(dataSaham) == 0:
                Tabel.add_row(['Data Saham Kosong']*6)
                print(Tabel)
        else:
                for saham in dataSaham:  # Menampilkan semua data saham
                        if saham['hapus'] == False:  # Memastikan saham tidak dihapus
                                
                                kode_saham = saham['kode']
                                nama_perusahaan = saham['perusahaan']
                                harga_pembukaan = nominal(saham['hargaPembukaan'])
                                harga_penutupan = nominal(saham['hargaPenutupan'])
                                perubahan_harga = presentase(saham['perubahan'])
                                nilai_transaksi = nominal(saham['nilai'])

                                # Menambahkan baris ke dalam tabel
                                Tabel.add_row([kode_saham, nama_perusahaan, harga_pembukaan, harga_penutupan, perubahan_harga, nilai_transaksi])
                
                # Menampilkan tabel
                print(Tabel.get_string(sortby='Kode Saham'))

        input('=> Tekan Enter untuk melanjutkan..')

def filterKode():
        kodeSaham = input('\t\t\t=> Masukkan kode saham yang ingin ditampilkan: ').upper()
        print('\n')
        cariKode = False 

        for saham in dataSaham: # Menampilkan data berdasarkan kode saham tertentu
                if kodeSaham == saham['kode']:
                        cariKode = True
                        
                        Tabel = PrettyTable()
                        Tabel.field_names = ['Kode Saham', 'Nama Perusahaan', 'Harga Pembukaan', 'Harga Penutupan', 'Perubahan Harga', 'Nilai Transaksi']
                        Tabel.title = 'RINGKASAN PASAR SAHAM KONOHA 2025'
                        
                        kode_saham = saham['kode']
                        nama_perusahaan = saham['perusahaan']
                        harga_pembukaan = nominal(saham['hargaPembukaan'])
                        harga_penutupan = nominal(saham['hargaPenutupan'])
                        perubahan_harga = presentase(saham['perubahan'])
                        nilai_transaksi = nominal(saham['nilai'])

                        Tabel.add_row([kode_saham, nama_perusahaan, harga_pembukaan, harga_penutupan, perubahan_harga, nilai_transaksi])
                        print(Tabel)
                        input('=> Tekan Enter untuk melanjutkan..')
                        break   
        
        if not cariKode:
                print(f"{'Data dengan kode {kodeSaham} yang Anda masukkan tidak terdeteksi. Pastikan kode saham benar!':^100}")
                print(f"{'*'*3:^100}")
                input(f"{'Tekan Enter untuk melanjutkan..':^99}")

def filterHarga():
        while True: 
                try:
                        harga = int(input('\t\t\t   => Masukkan harga saham yang ingin ditampilkan: '))
                        break
                except ValueError:
                        print('\n')
                        print(f"{'Maaf, harga saham yang Anda masukkan tidak valid. Pastikan harga berupa angka dan coba lagi.':^100}")
                        print(f"{'*'*3:^100}")
        
        print('\n')
        cariHarga = False
        Tabel = PrettyTable()
        Tabel.field_names = ['Kode Saham', 'Nama Perusahaan', 'Harga Pembukaan', 'Harga Penutupan', 'Perubahan Harga', 'Nilai Transaksi']
        Tabel.title = 'RINGKASAN PASAR SAHAM KONOHA 2025'
        
        for saham in dataSaham: # Menampilkan data berdasarkan harga pembukaan atau harga penutupan saham
                if saham['hargaPembukaan'] == harga or saham['hargaPenutupan'] == harga: 
                        cariHarga = True
                        
                        kode_saham = saham['kode']
                        nama_perusahaan = saham['perusahaan']
                        harga_pembukaan = nominal(saham['hargaPembukaan'])
                        harga_penutupan = nominal(saham['hargaPenutupan'])
                        perubahan_harga = presentase(saham['perubahan'])
                        nilai_transaksi = nominal(saham['nilai'])

                        Tabel.add_row([kode_saham, nama_perusahaan, harga_pembukaan, harga_penutupan, perubahan_harga, nilai_transaksi])
        if cariHarga:
                print(Tabel)  
                input('=> Tekan Enter untuk melanjutkan..')
        
        else:
                print('\n')
                print(f"{'Pencarian tidak ditemukan. Pastikan harga pembukaan atau penutupan saham yang Anda masukkan sudah benar!':^100}")
                print(f"{'*'*3:^100}")
                input(f"{'Tekan Enter untuk melanjutkan..':^99}")

def tampilkanData():
        while True:
                print('\n')
                print('='*110)
                print(f"{'SISTEM MANAJEMEN DATA SAHAM KONOHA':^100}")
                print('='*110)

                menuCari = input('''
                        =====================================================
                                   ***  Data Saham Konoha 2025 ***
                        =====================================================
                        Daftar Menu:
                        =====================================================
                        [1] Menampilkan Semua Data Saham 
                        [2] Menampilkan Data Saham Berdasarkan Kode Saham
                        [3] Menampilkan Data Saham Berdasarkan Harga Saham
                            Pembukaan atau Penutupan Saham 
                        [4] Kembali ke Menu Utama  
                        =====================================================
                        => Pilih menu yang ingin Anda akses : ''')

                if menuCari == '1': # Menampilkan semua data saham
                        menampilkan()
                elif menuCari == '2': # Menampilkan data saham berdasarkan kode saham
                        filterKode()
                elif menuCari == '3': # Menampilkan data saham berdasarkan harga pembukaan atau penutupan saham
                        filterHarga()
                elif menuCari == '4': # Kembali ke menu utama 
                        break
                else:
                        print('\n')
                        print(f"{'Opsi yang Anda pilih tidak tersedia. Pilih menu yang valid dan coba lagi.':^100}")
                        print(f"{'*'*3:^100}")
                        input(f"{'Tekan Enter untuk melanjutkan..':^99}")

# *********************************
# ********** CREATE DATA **********
# *********************************

def cekPerusahaan():
        while True:
        # Menerima input dari user dan memastikan hanya huruf dan spasi yang dimasukkan
                perusahaan = input("Masukkan nama perusahaan\t: ").strip()
                nama = perusahaan.split()
                if len(nama) == 4 and all(kata.isalpha() for kata in nama):  
                        return perusahaan.title()
                else:
                        print('\n')
                        print("Nama perusahaan hanya boleh mengandung huruf, spasi dan harus empat kata. Silakan coba lagi.")
                        print('\n')

def konfersiKode(pt):
        kode = pt.split()
        kodeSaham = ''.join([saham[0].upper() for saham in kode])
        return kodeSaham[:4]

def cekHargaPembukaan():
        while True: 
                try:    # User menambahkan harga pembukaan saham
                        hargaPembukaan = int(input('Masukkan harga pembukaan saham\t: '))
                        if hargaPembukaan <= 0:
                                print('\n')
                                print('Maaf, harga yang Anda masukkan tidak valid. Pastikan harga lebih dari 0.')  
                                print('\n')
                        else:
                                return hargaPembukaan
                except ValueError:
                        print('\n')
                        print('Maaf, harga yang Anda masukkan tidak valid. Pastikan harga berupa angka dan coba lagi.')
                        print('\n')

def cekHargaPenutupan():
        while True:
                try:    # User menambahkan harga pembukaan saham
                        hargaPenutupan = int(input('Masukkan harga penutupan saham\t: '))
                        if hargaPenutupan <= 0:
                                print('\n')
                                print('Maaf, harga yang Anda masukkan tidak valid. Pastikan harga lebih dari 0.')  
                                print('\n')
                        else:
                                return hargaPenutupan
                except ValueError:
                        print('\n')
                        print('Maaf, harga yang Anda masukkan tidak valid. Pastikan harga berupa angka dan coba lagi.')
                        print('\n')

def cekPerubahan(hargaPembukaan, hargaPenutupan):
        if hargaPembukaan == 0: 
                return 0
        # Menghitung persentase perubahan harga saham
        perubahan = ((hargaPenutupan - hargaPembukaan) / hargaPembukaan) * 100
        return perubahan
        
def cekNilai():
        while True:
                try:    # User menambahkan nilai transaksi saham
                        nilai = int(input('Masukkan nilai transaksi saham\t: '))
                        if nilai <= 0:
                                print('\n')
                                print('Maaf, nilai transaksi saham yang Anda masukkan tidak valid. Pastikan nilai transaksi lebih dari 0.')
                                print('\n') 
                        else:
                                return nilai
                except ValueError:
                        print('\n')
                        print('Maaf, nilai transaksi saham yang Anda masukkan tidak valid. Pastikan nilai berupa angka dan coba lagi.')
                        print('\n')

def menambahkan():
        while True:
                print('\n')
                kodeSaham = input('=> Masukkan kode saham untuk cek data saham: ').upper() # User input kode untuk cek data
                if len(kodeSaham) == 4 and kodeSaham.isalpha():
                        break
                else:
                        print('\n')
                        print(f"{'Maaf, kode yang Anda masukkan tidak valid.':^100}")
                        print(f"{'*'*3:^100}")
                        print('\n')
                        tambahData()
                        
        cari = False
        for saham in dataSaham:
                if saham ['kode'] == kodeSaham:
                        cari=True
                        break 
        if cari:
                print('Data saham yang Anda masukkan sudah terdaftar:')             
                cari = True 
                
                Tabel = PrettyTable()
                Tabel.field_names = ['Kode Saham', 'Nama Perusahaan', 'Harga Pembukaan', 'Harga Penutupan', 'Perubahan Harga', 'Nilai Transaksi']
                Tabel.title = 'RINGKASAN PASAR SAHAM KONOHA 2025'
                
                kode_saham = saham['kode']
                nama_perusahaan = saham['perusahaan']
                harga_pembukaan = nominal(saham['hargaPembukaan'])
                harga_penutupan = nominal(saham['hargaPenutupan'])
                perubahan_harga = presentase(saham['perubahan'])
                nilai_transaksi = nominal(saham['nilai'])

                Tabel.add_row([kode_saham, nama_perusahaan, harga_pembukaan, harga_penutupan, perubahan_harga, nilai_transaksi])
                print(Tabel.get_string(sortby='Kode Saham'))
                return
                
        else:
                perusahaan = cekPerusahaan() # User menambahkan nama perusahaan saham tersebut 
                kode = konfersiKode(perusahaan)
                hargaPembukaan = cekHargaPembukaan() # User menambahkan harga prmbukaan saham baru
                hargaPenutupan = cekHargaPenutupan() # User menambahkan harga penutupan saham baru
                perubahanHarga = cekPerubahan(hargaPembukaan, hargaPenutupan)# Menampilkan nilai perubahan harga saham
                print(f'Pergerakan Harga\t\t: {presentase(perubahanHarga)}')
                nilai = cekNilai() # User menambahkan total nilai transaksi saham tersebut

                # Menampung & menampilkan data baru yg ditambahkan 
                print('\n') 
                print('Data Baru:')   
                Tabel = PrettyTable()
                Tabel.field_names = ['Kode Saham', 'Nama Perusahaan', 'Harga Pembukaan', 'Harga Penutupan', 'Perubahan Harga', 'Nilai Transaksi']
                Tabel.title = 'RINGKASAN PASAR SAHAM KONOHA 2025'
                
                Tabel.add_row([
                        kode, 
                        perusahaan, 
                        nominal(hargaPembukaan), 
                        nominal(hargaPenutupan), 
                        presentase(perubahanHarga), 
                        nominal(nilai)
                        ])
                print(Tabel)

                dataSaham.append({
                        'kode':kode,
                        'perusahaan':perusahaan, 
                        'hargaPembukaan':nominal(hargaPembukaan),
                        'hargaPenutupan':nominal(hargaPenutupan),
                        'perubahan':presentase(perubahanHarga), 
                        'nilai':nominal(nilai), 
                        'hapus':False
                        })
                
                simpan = input('=> Pastikan data yang Anda masukkan sudah benar.\n   Apakah Anda ingin menyimpan data baru tersebut? (Ya/Tidak): ').capitalize()
                if simpan == 'Ya':
                        print('\n')
                        print(f"{'Data saham berhasil ditambahkan.':^100}")
                        print(f"{'*'*3:^100}")
                        input(f"{'Tekan Enter untuk melanjutkan..':^99}")
                        menampilkan()
                elif simpan == 'Tidak':
                        print('\n')
                        print(f"{'Penambahan data saham dibatalkan.':^100}")
                        print(f"{'*'*3:^100}")
                        input(f"{'Tekan Enter untuk melanjutkan..':^99}")
                else:
                        print('\n')
                        print(f"{'Input masih tidak valid.':^100}")
                        print(f"{'*'*3:^100}")
                        input(f"{'Tekan Enter untuk melanjutkan..':^99}")

def tambahData():
        while True:
                print('\n')
                print('='*110)
                print(f"{'SISTEM MANAJEMEN DATA SAHAM KONOHA':^100}")
                print('='*110)

                menuTambah =   input('''
                               ======================================
                                 *** Penambahan Data Saham 2025 ***
                               ======================================
                               Daftar Menu Penambahan:
                               ======================================
                               [1] Menambahkan Data Saham  
                               [2] Kembali ke Menu Utama 
                               ======================================
                               => Pilih menu yang ingin Anda akses : ''')

                if menuTambah == '1': # Menambahkan data saham baru 
                        menambahkan() 
                elif menuTambah == '2':# Kembali ke menu utama
                        break
                else:
                        print('\n')
                        print(f"{'Opsi yang Anda pilih tidak tersedia. Pilih menu yang valid dan coba lagi.':^100}")
                        print(f"{'*'*3:^100}")
                        input(f"{'Tekan Enter untuk melanjutkan..':^99}")

# ****************************
# ********** UPDATE **********
# **************************** 

def memperbarui():
        menampilkan()
        print('\n')
        while True: 
                try:    # User input kode yang ingin diperbarui
                        kodeSaham = input('=> Masukkan kode saham yang ingin diperbarui: ').upper()
                        break
                except ValueError:
                        print('\n')
                        print(f"{'Maaf, kode yang Anda masukkan tidak valid. Pastikan kode berupa angka dan coba lagi.':^100}")
                        print(f"{'*'*3:^100}")
                        print('\n')

        cari = False
        for saham in dataSaham: 
                if kodeSaham == saham['kode']:
                        dataAsli = saham.copy()

                        # Menampilkan data saham berdasarkan kode saham yang ingin diperbarui
                        Tabel = PrettyTable()
                        Tabel.field_names = ['Kode Saham', 'Nama Perusahaan', 'Harga Pembukaan', 'Harga Penutupan', 'Perubahan Harga', 'Nilai Transaksi']
                        Tabel.title = 'RINGKASAN PASAR SAHAM KONOHA 2025'
                        
                        Tabel.add_row([
                                kodeSaham, 
                                saham['perusahaan'],  
                                nominal(saham['hargaPembukaan']), 
                                nominal(saham['hargaPenutupan']), 
                                presentase(saham['perubahan']),
                                nominal(saham['nilai'])
                                ])
                        print(Tabel)
                        cari = True
                        break

        if cari == False:
                print('\n')
                print(f"{'Data dengan kode yang Anda masukkan tidak terdeteksi. Pastikan kode benar.':^100}")
                print(f"{'*'*3:^100}")
                return
        
        if cari:
                while True:
                        try:
                                konfirmasi = input('Apakah Anda ingin melanjutkan untuk memperbarui data tersebut (Ya/Tidak)?: ').capitalize()
                                if konfirmasi == 'Ya':
                                        kolom = input('''
                                        ========================================                          
                                        Daftar kolom: 
                                        ========================================                          
                                        [1] Nama Perusahaan
                                        [2] Harga Pembukaan
                                        [3] Harga Penutupan
                                        [4] Perubahan Harga 
                                        [5] Nilai Transaksi
                                        ========================================                          
                                        => Masukkan kolom yang ingin diperbarui: ''')
                                        print('\n')
                                        
                                        if kolom == '1': # Memperbarui nama perusahaan dan kode saham baru
                                                Perusahaan = cekPerusahaan()
                                                saham['perusahaan'] = Perusahaan

                                                KodeBaru = konfersiKode(Perusahaan)
                                                saham['kode'] = KodeBaru
                                        elif kolom == '2': # Memperbarui harga pembukaan saham
                                                HargaPembukaan = cekHargaPembukaan()
                                                HargaPembukaan = nominal(HargaPembukaan)
                                                saham['hargaPembukaan'] = HargaPembukaan                    
                                        elif kolom == '3': # Memperbarui harga penutupan saham
                                                HargaPenutupan = cekHargaPenutupan()
                                                HargaPenutupan = nominal(HargaPenutupan)
                                                saham['hargaPenutupan'] = HargaPenutupan
                                        elif kolom == '4': # Memperbarui persentase perubahan harga saham
                                                hargaPembukaan = cekHargaPembukaan()
                                                hargaPenutupan = cekHargaPenutupan()
                                                perubahan = cekPerubahan(hargaPembukaan, hargaPenutupan) # Hitung perubahan harga
                                                if perubahan is not None:
                                                        # Ubah perubahan ke format persentase
                                                        perubahan = presentase(perubahan)
                                                        perubahanAngka = float(perubahan.replace('%', ''))
                                                        # Update data saham
                                                        saham['hargaPembukaan'] = hargaPembukaan
                                                        saham['hargaPenutupan'] = hargaPenutupan
                                                        saham['perubahan'] = perubahan

                                                        if perubahanAngka > 10:
                                                                print('\nHarga berubah sangat signifikan!\n')
                                                        elif perubahanAngka <= 10:
                                                                print('\nHarga berubah cukup signifikan\n')
                                                        else:
                                                                print('\nHarga tidak mengalami perubahan\n')
                                                else:
                                                        print('\nNilai perubahan tidak dapat dihitung. Pastikan Anda memasukkan data dengan benar.\n') 
                                        elif kolom == '5': # Memperbarui nilai transaksi saham
                                                Nilai = cekNilai()
                                                Nilai = nominal(Nilai)
                                                saham['nilai'] = Nilai
                                        else:
                                                print('\n')
                                                print(f"{'Kolom yang Anda pilih tidak ditemukan. Silakan pilih kolom yang valid untuk diperbarui.':^100}")
                                                print(f"{'*'*3:^100}")
                                                continue

                                        simpan = input('Apakah data tersebut mau disimpan (Ya/Tidak)?: ').capitalize()
                                        if simpan == 'Ya':
                                                print(f"Data saham PT {saham['perusahaan']} berhasil diperbarui")
                                                menampilkan()
                                        elif simpan == 'Tidak':
                                                dataSaham[dataSaham.index(saham)] = dataAsli
                                                print(f"Pembaruan data saham dibatalkan. Data tidak disimpan.")

                                        else:
                                                print(f"{'Input tidak valid.':^100}")
                                                print(f"{'*'*3:^100}")
                                                input(f"{'Tekan Enter untuk melanjutkan..':^99}")                  
                                        break
                
                                elif konfirmasi == 'Tidak':
                                        print('\n')
                                        print(f"{' Proses pembaruan data dibatalkan.':^100}")
                                        print(f"{'*'*3:^100}")
                                        break
                                else:
                                        raise ValueError ("=> Input tidak valid. Silakan pilih ya atau tidak dan coba lagi.")
                                        input('=> Tekan Enter untuk melanjutkan..')      

                        except ValueError as pesanInvalid:
                                print(pesanInvalid)
                                continue
                                
def perbaruiData():
        while True:               
                print('\n')
                print('='*110)
                print(f"{'SISTEM MANAJEMEN DATA SAHAM KONOHA':^100}")
                print('='*110)

                menuPerbarui =   input('''
                               ======================================
                                   *** Pembaruan Data Saham 2025 ***
                               ======================================
                               Daftar Menu Pembaruan:
                               ======================================
                               [1] Memperbarui Data Saham  
                               [2] Kembali ke Menu Utama 
                               ======================================
                               => Pilih menu yang ingin Anda akses : ''')
                
                if menuPerbarui == '1':
                        memperbarui() # Memperbarui data saham berdasarkan kode saham
                        break
                elif menuPerbarui == '2':
                        menu_utama('admin')
                        break
                else:
                        print('\n')
                        print(f"{'Opsi yang Anda pilih tidak tersedia. Pilih menu yang valid dan coba lagi.':^100}")
                        print(f"{'*'*3:^100}")
                        input(f"{'Tekan Enter untuk melanjutkan..':^99}")

# ****************************
# ********** DELETE **********
# ****************************

recycle_bin = [] # untuk menampung data yg dihapus

def menghapus():
        while True:
                try:    # Menghapus data saham berdasarkan kode saham (soft deleted)
                        kodeSaham = input('\t\t\t       => Masukkan kode saham yang ingin Anda hapus: ').upper()
                        break
                except ValueError:
                        print('\n')
                        print(f"{'Maaf, kode yang Anda masukkan tidak valid. Pastikan kode saham benar dan coba lagi.':^100}")
                        print(f"{'*'*3:^100}")
                        print('\n')
        cari = None
        for saham in dataSaham: 
                if saham['kode'] == kodeSaham and saham['hapus'] == False:
                        cari = saham # Menampilkan data saham berdasarkan kode saham yang ingin dihapus
                        break

        if cari == None:
                print('\n')
                print(f"{'Data dengan kode yang Anda masukkan tidak terdeteksi.':^100}")
                print(f"{'*'*3:^100}")
                return

        print('\n')
        Tabel = PrettyTable()
        Tabel.field_names = ['Kode Saham', 'Nama Perusahaan', 'Harga Pembukaan', 'Harga Penutupan', 'Perubahan Harga', 'Nilai Transaksi']
        Tabel.title = 'RINGKASAN PASAR SAHAM KONOHA 2025'

        kode_saham = cari['kode']
        nama_perusahaan = cari['perusahaan']
        harga_pembukaan = nominal(cari['hargaPembukaan'])
        harga_penutupan = nominal(cari['hargaPenutupan'])
        perubahan_harga = presentase(cari['perubahan'])
        nilai_transaksi = nominal(cari['nilai'])

        Tabel.add_row([kode_saham, nama_perusahaan, harga_pembukaan, harga_penutupan, perubahan_harga, nilai_transaksi])
        print(Tabel)

        konfirmasi = input('Apakah Anda yakin ingin menghapus data saham tersebut (Ya/Tidak)?: ').capitalize()
        if konfirmasi == 'Ya':
                saham['hapus']=True
                recycle_bin.append(cari)
                print('\n')
                print(f"{'Data saham berhasil dihapus.':^100}")
                print(f"{'*'*3:^100}")
                menampilkan()
        elif konfirmasi == 'Tidak':
                print('\n')
                print(f"{'Data saham batal dihapus.':^100}")
                print(f"{'*'*3:^100}")
                input(f"{'Tekan Enter untuk melanjutkan..':^99}")
        else:
                print('\n')
                print(f"{'Input masih tidak valid.':^100}")
                print(f"{'*'*3:^100}")
                input(f"{'Tekan Enter untuk melanjutkan..':^99}")

# menghapus data berdasarkan kode saham untuk hard deleted
def hapusPermanen():
        while True:
                try:    # Menghapus data saham berdasarkan kode saham (soft deleted)
                        kodeSaham = input('\t\t\t       => Masukkan kode saham yang ingin Anda hapus: ').upper()
                        break
                except ValueError:
                        print('\n')
                        print(f"{'Maaf, kode yang Anda masukkan tidak valid. Pastikan kode saham benar dan coba lagi.':^100}")
                        print(f"{'*'*3:^100}")
                        print('\n')
        cari = None
        for saham in dataSaham: 
                if saham['kode'] == kodeSaham and saham['hapus'] == False:
                        cari = saham # Menampilkan data saham berdasarkan kode saham yang ingin dihapus
                        
                        print('\n')
                        Tabel = PrettyTable()
                        Tabel.field_names = ['Kode Saham', 'Nama Perusahaan', 'Harga Pembukaan', 'Harga Penutupan', 'Perubahan Harga', 'Nilai Transaksi']
                        Tabel.title = 'RINGKASAN PASAR SAHAM KONOHA 2025'

                        kode_saham = saham['kode']
                        nama_perusahaan = saham['perusahaan']
                        harga_pembukaan = nominal(saham['hargaPembukaan'])
                        harga_penutupan = nominal(saham['hargaPenutupan'])
                        perubahan_harga = presentase(saham['perubahan'])
                        nilai_transaksi = nominal(saham['nilai'])

                        Tabel.add_row([kode_saham, nama_perusahaan, harga_pembukaan, harga_penutupan, perubahan_harga, nilai_transaksi])
                        print(Tabel)

                        konfirmasi = input('Apakah ingin melanjutkan menghapus data saham secara permanen (Ya/Tidak)?: ').capitalize()
                        if konfirmasi == 'Ya':
                                if saham['kode'] == kodeSaham:
                                        dataSaham.remove(cari)
                                        print('\n')
                                        print(f"{'Data saham berhasil dihapus':^100}")
                                        print(f"{'*'*3:^100}")
                                        menampilkan()
                        elif konfirmasi == 'Tidak':
                                print('\n')
                                print(f"{'Data saham batal dihapus.':^100}")
                                print(f"{'*'*3:^100}")
                                input(f"{'Tekan Enter untuk melanjutkan..':^99}")
                        else:
                                print('\n')
                                print(f"{'Input masih tidak valid.':^100}")
                                print(f"{'*'*3:^100}")
                                input(f"{'Tekan Enter untuk melanjutkan..':^99}")
                        
                        break
                
        if cari == None:
                print('\n')
                print(f"{'Data dengan kode yang Anda masukkan tidak terdeteksi.':^100}")
                print(f"{'*'*3:^100}")

# menampilkan data yg dihapus sementara
def riwayatHapus():
        print('\n')
        Tabel = PrettyTable()
        Tabel.field_names = ['Kode Saham', 'Nama Perusahaan', 'Harga Pembukaan', 'Harga Penutupan', 'Perubahan Harga', 'Nilai Transaksi']
        Tabel.title = 'RINGKASAN PASAR SAHAM KONOHA 2025'
        
        if len(recycle_bin) == 0:
                Tabel.add_row(['Data Saham Kosong']*6)
                print(Tabel)
        else:
                for saham in recycle_bin:
                        kode_saham = saham['kode']
                        nama_perusahaan = saham['perusahaan']
                        harga_pembukaan = nominal(saham['hargaPembukaan'])
                        harga_penutupan = nominal(saham['hargaPenutupan'])
                        perubahan_harga = presentase(saham['perubahan'])
                        nilai_transaksi = nominal(saham['nilai'])

                        Tabel.add_row([kode_saham, nama_perusahaan, harga_pembukaan, harga_penutupan, perubahan_harga, nilai_transaksi])

                print(Tabel.get_string(sortby='Kode Saham'))

# memulihkan data yg ada di riwayat hapus
def pulihkanData():
        if not recycle_bin:
                riwayatHapus()
                print(f"{'Data Saham Tidak Ditemukan di Riwayat Hapus':^100}")
                print(f"{'*'*3:^100}")
                input(f"{'Tekan Enter untuk melanjutkan..':^99}")
                return
        else:
                while True:
                        try:
                                kodeSaham = input('=> Masukkan kode saham yang ingin Anda pulihkan: ').upper()
                                break
                        except ValueError:
                                print('kode saham yang anda masukkan tidak valid. Pastikan kode saham benar dan coba lagi.')
                
                print('\n')
                print('Data yang ingin dipulihkan: ')                
                cari = None

                for saham in recycle_bin: 
                        if saham['kode'] == kodeSaham:
                                cari = saham # Menampilkan data saham berdasarkan kode saham yang ingin dipulihkan
                                break

                if not cari:
                        print(f"{'Data Saham Tidak Ditemukan di Riwayat Hapus':^100}")
                        print(f"{'*'*3:^100}")
                        input(f"{'Tekan Enter untuk melanjutkan..':^99}")
                        return  # Keluar jika tidak ditemukan
                
                # Menampilkan jika data ditemukan
                Tabel = PrettyTable()
                Tabel.field_names = ['Kode Saham', 'Nama Perusahaan', 'Harga Pembukaan', 'Harga Penutupan', 'Perubahan Harga', 'Nilai Transaksi']
                Tabel.title = 'RINGKASAN PASAR SAHAM KONOHA 2025'

                kode_saham = cari['kode']
                nama_perusahaan = cari['perusahaan']
                harga_pembukaan = nominal(cari['hargaPembukaan'])
                harga_penutupan = nominal(cari['hargaPenutupan'])
                perubahan_harga = presentase(cari['perubahan'])
                nilai_transaksi = nominal(cari['nilai'])

                Tabel.add_row([kode_saham, nama_perusahaan, harga_pembukaan, harga_penutupan, perubahan_harga, nilai_transaksi])
                print(Tabel)

                konfirmasi = input('Apakah ingin melanjutkan memulihkan data saham tersebut (Ya/Tidak)?: ').capitalize()
                if konfirmasi == 'Ya':
                        dataSaham.append(cari)
                        cari['hapus'] = False
                        recycle_bin.remove(cari)
                        print('\n')
                        print(f"{'Data saham berhasil dipulihkan.':^100}")
                        print(f"{'*'*3:^100}")
                        menampilkan()
                elif konfirmasi == 'Tidak':
                        print('\n')
                        print(f"{'Data saham batal dipulihkan.':^100}")
                        print(f"{'*'*3:^100}")
                        menampilkan()
                else:
                        print('\n')
                        print(f"{'Input masih tidak valid.':^100}")
                        print(f"{'*'*3:^100}")
                        input(f"{'Tekan Enter untuk melanjutkan..':^99}")

# tampilan menu untuk menghapus data  
def hapusData():
        while True:              
                print('\n')
                print('='*110)
                print(f"{'SISTEM MANAJEMEN DATA SAHAM KONOHA':^100}")
                print('='*110)

                menuHapus =    input('''
                               =======================================
                                 *** Penghapusan Data Saham 2025 ***
                               =======================================
                               Daftar Menu Penghapusan:
                               =======================================
                               [1] Hapus Sementara Data Saham  
                               [2] Hapus Permanen Data Saham
                               [3] Data Saham Terhapus
                               [4] Pemulihan Data Saham Terhapus
                               [5] Kembali ke Menu Utama 
                               =======================================
                               => Pilih menu yang ingin Anda akses : ''')
                
                if menuHapus == '1':
                        menghapus()
                elif menuHapus == '2':
                        hapusPermanen()
                elif menuHapus == '3':
                        riwayatHapus()
                elif menuHapus == '4':
                        pulihkanData()
                elif menuHapus == '5':
                        break
                else: 
                        print('\n')
                        print(f"{'Opsi yang Anda pilih tidak tersedia. Pilih menu yang valid dan coba lagi.':^100}")
                        print(f"{'*'*3:^100}")
                        input(f"{'Tekan Enter untuk melanjutkan..':^99}")

# ****************************
# ********** EXIT **********
# ****************************

# tampilan menu untuk keluar dari pemrograman
def keluarSistem (pengguna):
        bersihkan_layar()

        while True:
                print('\n')
                print('='*110)
                print(f"{'SISTEM MANAJEMEN DATA SAHAM KONOHA':^100}")
                print('='*110)
                menuKeluar =   input('''
                               ======================================
                                   Terima Kasih Telah Menggunakan
                                     Sistem Manajemen Data Saham
                               ======================================
                               Apakah Anda Yakin Ingin Keluar?
                               [1] Ya, Keluar
                               [2] Kembali ke Menu Utama
                               ======================================
                               => Pilih menu yang ingin Anda akses : ''')

                if menuKeluar == '1': 
                        print('\n')
                        print(f"{'Program Berakhir...':^100}")
                        print(f"{'*'*3:^100}")
                        print('\n')
                        exit()
                elif menuKeluar == '2':
                        menu_utama(pengguna)
                        break
                else:
                        print('\n')
                        print(f"{'Opsi yang Anda pilih tidak tersedia. Pilih menu yang valid dan coba lagi.':^100}")
                        print(f"{'*'*3:^100}")
                        input(f"{'Tekan Enter untuk melanjutkan..':^99}")

# Proses login dan menampilkan menu berdasarkan status pengguna
def user():
        pengguna = login() 

        if pengguna: 
                print(f'\nLogin berhasil! Anda adalah seorang {pengguna.capitalize()}.')
                menu_utama(pengguna)
        else:
                print('\nStatus pengguna atau kata sandi yang Anda masukkan salah. Silakan coba lagi.\n')

# user()
menu_utama('admin')

