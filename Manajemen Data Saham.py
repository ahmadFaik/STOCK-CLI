from prettytable import PrettyTable
import os

dataSaham = {}
dataSaham = { 
        1 : {'kode':'AADI',
             'perusahaan':'Adaro Andalan Indonesia Tbk.', 
             'hargaPembukaan':6550,
             'hargaPenutupan':6800,
             'perubahan':3.82, 
             'nilai':44460882500, 
             'hapus':False},

        2 : {'kode':'AALI',
             'perusahaan':'Astra Agro Lestari Tbk.', 
             'hargaPembukaan':5675,
             'hargaPenutupan':5550,
             'perubahan':2.20, 
             'nilai':3764012500, 
             'hapus':False},

        3 : {'kode':'BBCA',
             'perusahaan':'Bank Central Asia Tbk.',
             'hargaPembukaan':8275,
             'hargaPenutupan':7900,
             'perubahan':-4.53,
             'nilai':736670570000,
             'hapus':False},

        4: {'kode':'BBRI',
            'perusahaan':'Bank Rakyat Indonesia (Persero) Tbk.', 
            'hargaPembukaan':3930,
            'hargaPenutupan':5550,
            'perubahan':41.23, 
            'nilai':941219074000, 
            'hapus':False},
                
        5 : {'kode':'BRIS',
             'perusahaan':'Bank Syariah Indonesia Tbk.', 
             'hargaPembukaan':2610,
             'hargaPenutupan':5550,
             'perubahan':112.22, 
             'nilai':85977800000, 
             'hapus':False},

        6 : {'kode':'BMRI',
             'perusahaan':'Bank Mandiri (Persero) Tbk.', 
             'hargaPembukaan':4870,
             'hargaPenutupan':5550,
             'perubahan':13.97, 
             'nilai':570806151000, 
             'hapus':False},
        
        7 : {'kode':'GOTO',
             'perusahaan':'GoTo Gojek Tokopedia Tbk.', 
             'hargaPembukaan':81,
             'hargaPenutupan':81,
             'perubahan':0.00, 
             'nilai':436906658200, 
             'hapus':False},

        8 : {'kode':'TLKM',
             'perusahaan':'Telkom Indonesia (Persero) Tbk.', 
             'hargaPembukaan':2430,
             'hargaPenutupan':5550,
             'perubahan':128.57, 
             'nilai':439964438000, 
             'hapus':False}}

def bersihkan_layar():
        if os.name == 'nt':
                os.system('cls') # Windows
        else:
                os.system('clear') # Linux/macOS

def login():
        bersihkan_layar()
        while True:
                print('\n')
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

# Proses login dan menampilkan menu berdasarkan status pengguna
def user():
        pengguna = login() 

        if pengguna: 
                print(f'\nLogin berhasil! Anda adalah seorang {pengguna.capitalize()}.')
                menu_utama(pengguna)
        else:
                print('\nStatus pengguna atau kata sandi yang Anda masukkan salah. Silakan coba lagi.\n')

# tampilan menu utama 
def menu_utama(pengguna):
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
                                ubahData()
                        elif menu_admin == '4':
                                hapusData()
                        elif menu_admin == '5':
                                keluarSistem()
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
                                [1] Menampilkan Data Saham 
                                [2] Keluar            
                                ======================================
                                => Pilih menu yang ingin Anda akses : ''')
                        
                        if menu_investor == '1':
                                tampilkanData()

                        elif menu_investor== '2':
                                keluarSistem()
                        else:
                                print('\n')
                                print(f"{'Opsi yang Anda pilih tidak tersedia. Pilih menu yang valid dan coba lagi.':^100}")
                                print(f"{'*'*3:^100}")
                                input(f"{'Tekan Enter untuk melanjutkan..':^99}")                             

def nominal(angka):
        if isinstance(angka, str): 
                angka = angka.replace(',', '') 
        return f'{float(angka):,.2f}' # Format nominal ribuan

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
        Tabel.field_names = ['ID', 'Kode Saham', 'Nama Perusahaan', 'Harga Pembukaan', 'Harga Penutupan', 'Perubahan Harga', 'Nilai Transaksi']

        for id, saham in dataSaham.items(): # Menampilkan semua data saham
                if isinstance(saham, dict) and 'hapus' in saham:
                        if saham['hapus'] == False:
                                Tabel.title = 'RINGKASAN PASAR SAHAM KONOHA 2025'
                                harga_pembukaan = nominal(saham['hargaPembukaan'])
                                harga_penutupan = nominal(saham['hargaPenutupan'])
                                perubahan_harga = presentase(saham['perubahan'])
                                nilai_transaksi = nominal(saham['nilai'])
                                Tabel.add_row([id, saham['kode'], saham['perusahaan'], harga_pembukaan, harga_penutupan, perubahan_harga, nilai_transaksi])
        print(Tabel)
        input('=> Tekan Enter untuk melanjutkan..')

def filterId():
        while True: 
                try:
                        idSaham = int(input('\t\t\t   => Masukkan ID saham yang ingin ditampilkan: '))
                        break
                except ValueError: 
                        print('\n')
                        print(f"{'Maaf, ID yang Anda masukkan tidak valid. Pastikan ID berupa angka dan coba lagi.':^100}")
                        print(f"{'*'*3:^100}")
                        print('\n')
        print('\n')
        if idSaham in dataSaham: # Menampilkan data berdasarkan id saham tertentu
                saham = dataSaham[idSaham]
                Tabel = PrettyTable()
                Tabel.field_names = ['ID', 'Kode Saham', 'Nama Perusahaan', 'Harga Pembukaan', 'Harga Penutupan', 'Perubahan Harga', 'Nilai Transaksi']
                Tabel.title = 'RINGKASAN PASAR SAHAM KONOHA 2025'
                harga_pembukaan = nominal(saham['hargaPembukaan'])
                harga_penutupan = nominal(saham['hargaPenutupan'])
                perubahan_harga = presentase(saham['perubahan'])
                nilai_transaksi = nominal(saham['nilai'])
                Tabel.add_row([idSaham, saham['kode'], saham['perusahaan'], harga_pembukaan, harga_penutupan, perubahan_harga, nilai_transaksi])
                print(Tabel)
                input('=> Tekan Enter untuk melanjutkan..')
        else:
                print(f"{'Data dengan ID yang Anda masukkan tidak terdeteksi. Pastikan ID benar.':^100}")
                print(f"{'*'*3:^100}")
                input(f"{'Tekan Enter untuk melanjutkan..':^99}")

def filterKode():
        kodeSaham = input('\t\t\t   => Masukkan kode saham yang ingin ditampilkan: ').upper()
        print('\n')
        cariKode = False 
        for i, data in dataSaham.items(): # Menampilkan data berdasarkan kode saham tertentu
                if kodeSaham in data.values(): 
                        cariKode = True
                        Tabel = PrettyTable()
                        Tabel.field_names = ['ID', 'Kode Saham', 'Nama Perusahaan', 'Harga Pembukaan', 'Harga Penutupan', 'Perubahan Harga', 'Nilai Transaksi']
                        Tabel.title = 'RINGKASAN PASAR SAHAM KONOHA 2025'
                        harga_pembukaan = nominal(data['hargaPembukaan'])
                        harga_penutupan = nominal(data['hargaPenutupan'])
                        perubahan_harga = presentase(data['perubahan'])
                        nilai_transaksi = nominal(data['nilai'])
                        Tabel.add_row([i, data['kode'], data['perusahaan'], harga_pembukaan, harga_penutupan, perubahan_harga, nilai_transaksi])
                        print(Tabel)
                        break   
        
        if cariKode == False: 
                print(f'Data dengan kode {kodeSaham} yang Anda masukkan tidak terdeteksi. Pastikan kode saham benar.')

        input('=> Tekan Enter untuk melanjutkan..')

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
        for i, data in dataSaham.items(): # Menampilkan data berdasarkan harga pembukaan atau harga penutupan saham
                if data['hargaPembukaan'] == harga or data['hargaPenutupan'] == harga: 
                        cariHarga = True
                        Tabel = PrettyTable()
                        Tabel.field_names = ['ID', 'Kode Saham', 'Nama Perusahaan', 'Harga Pembukaan', 'Harga Penutupan', 'Perubahan Harga', 'Nilai Transaksi']
                        Tabel.title = 'RINGKASAN PASAR SAHAM KONOHA 2025'
                        harga_pembukaan = nominal(data['hargaPembukaan'])
                        harga_penutupan = nominal(data['hargaPenutupan'])
                        perubahan_harga = presentase(data['perubahan'])
                        nilai_transaksi = nominal(data['nilai'])
                        Tabel.add_row([i, data['kode'], data['perusahaan'], harga_pembukaan, harga_penutupan, perubahan_harga, nilai_transaksi])
                        print(Tabel)  
                        input('=> Tekan Enter untuk melanjutkan..')
        
        if cariHarga == False:
                print('\n')
                print(f"{'Pencarian tidak ditemukan. Pastikan harga pembukaan atau penutupan saham yang Anda masukkan sudah benar':^100}")
                print(f"{'*'*3:^100}")
                input(f"{'Tekan Enter untuk melanjutkan..':^99}")

def tampilkanData():
        while True:
                bersihkan_layar()
                print('\r\n')
                print('='*110)
                print(f"{'SISTEM MANAJEMEN DATA SAHAM KONOHA':^100}")
                print('='*110)

                menuCari = input('''
                           =============================================
                                  ***  Data Saham Konoha 2025 ***
                           =============================================
                           Daftar Menu:
                           ============================================= 
                           [1] Menampilkan Semua Data Saham 
                           [2] Menampilkan Data Saham Berdasarkan ID
                           [3] Menampilkan Data Saham Berdasarkan Kode
                           [4] Menampilkan Data Saham Berdasarkan harga
                           [5] Kembali ke Menu Utama  
                           ============================================= 
                           => Pilih menu yang ingin Anda akses : ''')

                if menuCari == '1': # Menampilkan semua data saham
                        if len(dataSaham) > 0: 
                                menampilkan()
                        else:
                                print(f"{'\nData Saham Tidak Ditemukan':^100}")
                                print(f"{'*'*3:^100}")
                elif menuCari == '2': # Menampilkan data saham berdasarkan ID saham
                        filterId()
                elif menuCari == '3': # Menampilkan data saham berdasarkan kode saham
                        filterKode()
                elif menuCari == '4': # Menampilkan data saham berdasarkan harga pembukaan atau penutupan saham
                        filterHarga()
                elif menuCari == '5': # Kembali ke menu utama 
                        break
                else:
                        print('\n')
                        print(f"{'Opsi yang Anda pilih tidak tersedia. Pilih menu yang valid dan coba lagi.':^100}")
                        print(f"{'*'*3:^100}")
                        input(f"{'Tekan Enter untuk melanjutkan..':^99}")

# *********************************
# ********** CREATE DATA **********
# *********************************
def cekKode():
        while True:    # User menambahkan kode saham baru 
                kode = input('Masukkan kode saham\t\t: ').upper() 
                if kode.isalpha():
                        if len(kode) == 4: 
                                return kode
                        else:
                                print('\nMaaf, kode yang Anda berikan tidak valid. Silakan periksa dan coba lagi.\n')
                else: 
                        print('\nMaaf, kode yang Anda berikan tidak valid. Silakan periksa dan coba lagi.\n')

def cekHargaPembukaan():
        while True: 
                try:    # User menambahkan harga pembukaan saham
                        hargaPembukaan = int(input('Masukkan harga pembukaan saham\t: '))
                        if hargaPembukaan <= 0:
                                print('\nMaaf, harga yang Anda masukkan tidak valid. Pastikan harga lebih dari 0.\n')  
                        else:
                                return hargaPembukaan
                except ValueError:
                        print('\nMaaf, harga yang Anda masukkan tidak valid. Pastikan harga berupa angka dan coba lagi.\n')

def cekHargaPenutupan():
        while True:
                try:    # User menambahkan harga pembukaan saham
                        hargaPenutupan = int(input('Masukkan harga penutupan saham\t: '))
                        if hargaPenutupan <= 0:
                                print('\nMaaf, harga yang Anda masukkan tidak valid. Pastikan harga lebih dari 0.\n')  
                        else:
                                return hargaPenutupan
                except ValueError:
                        print('\nMaaf, harga yang Anda masukkan tidak valid. Pastikan harga berupa angka dan coba lagi.\n')

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
                                print('\nMaaf, nilai transaksi saham yang Anda masukkan tidak valid. Pastikan nilai transaksi lebih dari 0.\n') 
                        else:
                                return nilai
                except ValueError:
                        print('\nMaaf, nilai transaksi saham yang Anda masukkan tidak valid. Pastikan nilai berupa angka dan coba lagi.\n')

def menambahkan():
        while True:
                try:    # User menambahkan ID saham baru 
                        idSaham = int(input('\nMasukkan ID saham baru\t\t: ')) 
                        if idSaham <= 0:
                                raise IndexError('\nMaaf, ID yang Anda masukkan tidak valid.\n') 
                        break
                except IndexError:
                        print('\nMaaf, ID yang Anda masukkan tidak valid. Pastikan ID berupa angka dan coba lagi.\n')
                except ValueError:
                        print('\nMaaf, ID yang Anda masukkan tidak valid. Pastikan ID berupa angka dan coba lagi.\n')
        
        if idSaham in dataSaham: 
                print('\nID yang Anda masukkan sudah terdaftar dalam data. Silahkan coba ID baru.\n')
                saham = dataSaham[idSaham]
                Tabel = PrettyTable()
                Tabel.field_names = ['ID', 'Kode Saham', 'Nama Perusahaan', 'Harga Pembukaan', 'Harga Penutupan', 'Perubahan Harga', 'Nilai Transaksi']
                Tabel.title = 'RINGKASAN PASAR SAHAM KONOHA 2025'
                harga_pembukaan = nominal(saham['hargaPembukaan'])
                harga_penutupan = nominal(saham['hargaPenutupan'])
                perubahan_harga = presentase(saham['perubahan'])
                nilai_transaksi = nominal(saham['nilai'])
                Tabel.add_row([idSaham, saham['kode'], saham['perusahaan'], harga_pembukaan, harga_penutupan, perubahan_harga, nilai_transaksi])
                print(Tabel)
        else:   # User menambahkan kode saham baru
                kode = cekKode()
                cari = False
                for i, data in dataSaham.items():
                        if kode in data.values():
                                cari = True
                                break
                if cari:
                        print('\nKode saham yang Anda masukkan sudah terdaftar dalam data. Silahkan coba kode saham baru.\n')
                        cari = True 
                        Tabel = PrettyTable()
                        Tabel.field_names = ['ID', 'Kode Saham', 'Nama Perusahaan', 'Harga Pembukaan', 'Harga Penutupan', 'Perubahan Harga', 'Nilai Transaksi']
                        Tabel.title = 'RINGKASAN PASAR SAHAM KONOHA 2025'
                        harga_pembukaan = nominal(data['hargaPembukaan'])
                        harga_penutupan = nominal(data['hargaPenutupan'])
                        perubahan_harga = presentase(data['perubahan'])
                        nilai_transaksi = nominal(data['nilai'])
                        Tabel.add_row([i, data['kode'], data['perusahaan'], harga_pembukaan, harga_penutupan, perubahan_harga, nilai_transaksi])
                        print(Tabel)
                        
                else:   # User menambahkan nama perusahaan saham tersebut
                        perusahaan = input('Masukkan nama perusahaan\t: ').title()
                        cari = False
                        for i, data in dataSaham.items():
                                if perusahaan in data.values():
                                        cari=True
                                        break 
                        if cari:
                                print('\nNama perusahaan yang Anda masukkan sudah terdaftar dalam data.\n')
                                cari = True 
                                Tabel = PrettyTable()
                                Tabel.field_names = ['ID', 'Kode Saham', 'Nama Perusahaan', 'Harga Pembukaan', 'Harga Penutupan', 'Perubahan Harga', 'Nilai Transaksi']
                                Tabel.title = 'RINGKASAN PASAR SAHAM KONOHA 2025'
                                harga_pembukaan = nominal(data['hargaPembukaan'])
                                harga_penutupan = nominal(data['hargaPenutupan'])
                                perubahan_harga = presentase(data['perubahan'])
                                nilai_transaksi = nominal(data['nilai'])
                                Tabel.add_row([i, data['kode'], data['perusahaan'], harga_pembukaan, harga_penutupan, perubahan_harga, nilai_transaksi])
                                print(Tabel)
                        else:        
                                hargaPembukaan = cekHargaPembukaan() # User menambahkan harga prmbukaan saham baru
                                hargaPenutupan = cekHargaPenutupan() # User menambahkan harga penutupan saham baru
                                perubahanHarga = cekPerubahan(hargaPembukaan, hargaPenutupan)# Menampilkan nilai perubahan harga saham
                                print(f'Pergerakan Harga\t\t: {presentase(perubahanHarga)}')
                                nilai = cekNilai() # User menambahkan total nilai transaksi saham tersebut

                                # Menampung & menampilkan data baru yg ditambahkan 
                                print('\nData Baru:')
                                dataSaham[idSaham] = {
                                        'kode':kode,
                                        'perusahaan':perusahaan, 
                                        'hargaPembukaan':nominal(hargaPembukaan),
                                        'hargaPenutupan':nominal(hargaPenutupan),
                                        'perubahan':presentase(perubahanHarga), 
                                        'nilai':nominal(nilai), 
                                        'hapus':False}
                                Tabel = PrettyTable()
                                Tabel.field_names = ['ID', 'Kode Saham', 'Nama Perusahaan', 'Harga Pembukaan', 'Harga Penutupan', 'Perubahan Harga', 'Nilai Transaksi']
                                Tabel.title = 'RINGKASAN PASAR SAHAM KONOHA 2025'
                                harga_pembukaan = nominal(hargaPembukaan)
                                harga_penutupan = nominal(hargaPenutupan)
                                perubahan_harga = presentase(perubahanHarga)
                                nilai_transaksi = nominal(nilai)
                                Tabel.add_row([idSaham, kode, perusahaan, harga_pembukaan, harga_penutupan, perubahan_harga, nilai_transaksi])
                                print(Tabel)
                                        
                                simpan = input('=> Pastikan data yang Anda masukkan sudah benar.\n   Apakah Anda ingin menyimpan data baru tersebut? (Ya/Tidak): ').capitalize()
                                if simpan == 'Ya':
                                        print(f"=> Data saham berhasil ditambahkan.")
                                        menampilkan()
                                else:
                                        print(f"=> Penambahan data saham dibatalkan.\n")
                                        tambahData()

def tambahData():
        while True:
                bersihkan_layar()
                print('\r\n')
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
                elif menuTambah == '2':
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
        while True: 
                try:    # User input ID yang ingin diperbarui
                        idSaham = int(input('\t\t\t       => Masukkan ID saham yang ingin diperbarui: '))
                        break
                except ValueError:
                        print('\n')
                        print(f"{'Maaf, ID yang Anda masukkan tidak valid. Pastikan ID berupa angka dan coba lagi.':^100}")
                        print(f"{'*'*3:^100}")
                        print('\n')

        if idSaham in dataSaham:
                saham = dataSaham[idSaham] # Menampilkan data saham berdasarkan ID yang ingin diperbarui
                Tabel = PrettyTable()
                Tabel.field_names = ['ID', 'Kode Saham', 'Nama Perusahaan', 'Harga Pembukaan', 'Harga Penutupan', 'Perubahan Harga', 'Nilai Transaksi']
                Tabel.title = 'RINGKASAN PASAR SAHAM KONOHA 2025'
                harga_pembukaan = nominal(saham['hargaPembukaan'])
                harga_penutupan = nominal(saham['hargaPenutupan'])
                perubahan_harga = presentase(saham['perubahan'])
                nilai_transaksi = nominal(saham['nilai'])
                Tabel.add_row([idSaham, saham['kode'], saham['perusahaan'], harga_pembukaan, harga_penutupan, perubahan_harga, nilai_transaksi])
                print(Tabel)  

                konfirmasi = input('Apakah Anda ingin melanjutkan untuk memperbarui data tersebut (Ya/Tidak)?: ').capitalize()
                if konfirmasi == 'Ya':
                        kolom = input('''
                               ========================================                          
                               Daftar kolom: 
                               ========================================                          
                               [1] Kode Saham
                               [2] Nama Perusahaan
                               [3] Harga Pembukaan
                               [4] Harga Penutupan
                               [5] Perubahan Harga 
                               [6] Nilai Transaksi
                               ========================================                          
                               => Masukkan kolom yang ingin diperbarui: ''')
                        print('\n')
                        if kolom == '1': # Memperbarui kode saham  
                                Kode = cekKode()
                                dataSaham[idSaham]['kode'] = Kode
                        elif kolom == '2': # Memperbarui nama perusahaan
                                Perusahaan = input('Masukkan nama perusahaan\t: ').title()
                                dataSaham[idSaham]['perusahaan'] = Perusahaan
                        elif kolom == '3': # Memperbarui harga pembukaan saham
                                HargaPembukaan = cekHargaPembukaan()
                                HargaPembukaan = nominal(HargaPembukaan)
                                dataSaham[idSaham]['hargaPembukaan'] = HargaPembukaan                    
                        elif kolom == '4': # Memperbarui harga penutupan saham
                                HargaPenutupan = cekHargaPenutupan()
                                HargaPenutupan = nominal(HargaPenutupan)
                                dataSaham[idSaham]['hargaPenutupan'] = HargaPenutupan
                        elif kolom == '5': # Memperbarui persentase perubahan harga saham
                                hargaPembukaan = cekHargaPembukaan()
                                hargaPenutupan = cekHargaPenutupan()
                                perubahan = cekPerubahan(hargaPembukaan, hargaPenutupan) # Hitung perubahan harga
                                if perubahan is not None:
                                        # Ubah perubahan ke format persentase
                                        perubahan = presentase(perubahan)
                                        perubahanAngka = float(perubahan.replace('%', ''))
                                        # Update data saham
                                        dataSaham[idSaham]['hargaPembukaan'] = hargaPembukaan
                                        dataSaham[idSaham]['hargaPenutupan'] = hargaPenutupan
                                        dataSaham[idSaham]['perubahan'] = perubahan

                                        if perubahanAngka > 10:
                                                print('\nHarga berubah sangat signifikan!\n')
                                        elif perubahanAngka <= 10:
                                                print('\nHarga berubah cukup signifikan\n')
                                        else:
                                                print('\nHarga tidak mengalami perubahan\n')
                                else:
                                        print('\nNilai perubahan tidak dapat dihitung. Pastikan Anda memasukkan data dengan benar.\n') 
                        elif kolom == '6': # Memperbarui nilai transaksi saham
                                Nilai = cekNilai()
                                Nilai = nominal(Nilai)
                                dataSaham[idSaham]['nilai'] = Nilai
                        else:
                                print('\n')
                                print(f"{'Kolom yang Anda pilih tidak ditemukan. Silakan pilih kolom yang valid untuk diperbarui.':^100}")
                                print(f"{'*'*3:^100}")
                                memperbarui()

                        simpan = input('Apakah data tersebut mau disimpan (Ya/Tidak)?: ').capitalize()
                        if simpan == 'Ya':
                                print(f"\nData saham {dataSaham[idSaham]['perusahaan']} berhasil diperbarui\n")
                        else:
                                print(f"\nPembaruan data saham {dataSaham[idSaham]['perusahaan']} dibatalkan. Tidak ada perubahan yang dilakukan.\n")
                                ubahData()
                else:
                        ubahData()
                
        else:
                print('\n')
                print(f"{'Data dengan ID yang Anda masukkan tidak terdeteksi. Pastikan ID benar.':^100}")
                print(f"{'*'*3:^100}")

        input(f"{'Tekan Enter untuk melanjutkan..':^99}")

def ubahData():
        bersihkan_layar()
        while True:               
                print('\r\n')
                print('='*110)
                print(f"{'SISTEM MANAJEMEN DATA SAHAM KONOHA':^100}")
                print('='*110)

                menuPerbarui =   input('''
                               =======================================
                                  *** Pembaruan Data Saham 2025 ***
                               =======================================
                               Daftar Menu Pembaruan:
                               =======================================
                               [1] Memperbarui Data Saham  
                               [2] Kembali ke Menu Utama 
                               =======================================
                               => Pilih menu yang ingin Anda akses : ''')
                
                if menuPerbarui == '1':
                        memperbarui() # Memperbarui data saham berdasarkan ID saham
                        menampilkan()
                elif menuPerbarui == '2':
                        break
                else:
                        print('\n')
                        print(f"{'Opsi yang Anda pilih tidak tersedia. Pilih menu yang valid dan coba lagi.':^100}")
                        print(f"{'*'*3:^100}")
                        input(f"{'Tekan Enter untuk melanjutkan..':^99}")

# ****************************
# ********** DELETE **********
# ****************************
recycle_bin = {} # untuk menampung data yg dihapus
def menghapus():
        while True:
                try:    # Menghapus data saham berdasarkan ID saham (soft deleted)
                        idSaham = int(input('\t\t\t       => Masukkan ID saham yang ingin Anda hapus: '))
                        break
                except ValueError:
                        print('\n')
                        print(f"{'Maaf, ID yang Anda masukkan tidak valid. Pastikan ID berupa angka dan coba lagi.':^100}")
                        print(f"{'*'*3:^100}")
                        print('\n')

        if idSaham in dataSaham:
                print('\n')
                saham = dataSaham[idSaham]
                Tabel = PrettyTable()
                Tabel = PrettyTable()
                Tabel.field_names = ['ID', 'Kode Saham', 'Nama Perusahaan', 'Harga Pembukaan', 'Harga Penutupan', 'Perubahan Harga', 'Nilai Transaksi']
                Tabel.title = 'RINGKASAN PASAR SAHAM KONOHA 2025'
                harga_pembukaan = nominal(saham['hargaPembukaan'])
                harga_penutupan = nominal(saham['hargaPenutupan'])
                perubahan_harga = presentase(saham['perubahan'])
                nilai_transaksi = nominal(saham['nilai'])
                Tabel.add_row([idSaham, saham['kode'], saham['perusahaan'], harga_pembukaan, harga_penutupan, perubahan_harga, nilai_transaksi])                
                print(Tabel)

                konfirmasi = input('Apakah Anda yakin ingin menghapus data saham tersebut (Ya/Tidak)?: ').capitalize()
                if konfirmasi == 'Ya':
                        recycle_bin[idSaham] = dataSaham[idSaham]
                        dataSaham[idSaham]['hapus'] = True
                        del dataSaham[idSaham]
                        print('\n')
                        print(f"{'Data saham berhasil dihapus':^100}")
                        print(f"{'*'*3:^100}")
                        menampilkan()
                else:
                        print('\n')
                        print(f"{'Data saham batal dihapus':^100}")
                        print(f"{'*'*3:^100}")

        else:
                print('\n')
                print(f"{'Data Saham Tidak Ditemukan':^100}")
                print(f"{'*'*3:^100}")
                input(f"{'Tekan Enter untuk melanjutkan..':^99}")

# menghapus data berdasarkan id untuk hard deleted
def hapusPermanen():
        while True:
                try:
                        idSaham = int(input('\t\t\t       => Masukkan ID saham yang ingin Anda hapus: '))
                        break
                except ValueError:
                        print('\n')
                        print(f"{'Maaf, ID yang Anda masukkan tidak valid. Pastikan ID berupa angka dan coba lagi.':^100}")
                        print(f"{'*'*3:^100}")
                        print('\n')
                        
        if idSaham in dataSaham:
                print('\n')
                saham = dataSaham[idSaham]
                Tabel = PrettyTable()
                Tabel.field_names = ['ID', 'Kode Saham', 'Nama Perusahaan', 'Harga Pembukaan', 'Harga Penutupan', 'Perubahan Harga', 'Nilai Transaksi']
                Tabel.title = 'RINGKASAN PASAR SAHAM KONOHA 2025'
                harga_pembukaan = nominal(saham['hargaPembukaan'])
                harga_penutupan = nominal(saham['hargaPenutupan'])
                perubahan_harga = presentase(saham['perubahan'])
                nilai_transaksi = nominal(saham['nilai'])
                Tabel.add_row([idSaham, saham['kode'], saham['perusahaan'], harga_pembukaan, harga_penutupan, perubahan_harga, nilai_transaksi])
                print(Tabel)  

                konfirmasi = input('Apakah ingin melanjutkan menghapus data saham secara permanen (Ya/Tidak)?: ').capitalize()
                if konfirmasi == 'Ya':
                        del dataSaham[idSaham]
                        print('\n')
                        print(f"{'Data saham berhasil dihapus':^100}")
                        print(f"{'*'*3:^100}")
                        menampilkan()
                else:
                        print('\n')
                        print(f"{'Data saham batal dihapus':^100}")
                        print(f"{'*'*3:^100}")
        else:
                print(f"{'Data Saham Tidak Ditemukan':^100}")
                print(f"{'*'*3:^100}")
                input(f"{'Tekan Enter untuk melanjutkan..':^99}")

# menampilkan data yg soft deleted
def riwayat_hapus():
        print('\n')
        Tabel = PrettyTable()
        Tabel.field_names = ['ID', 'Kode Saham', 'Nama Perusahaan', 'Harga Pembukaan', 'Harga Penutupan', 'Perubahan Harga', 'Nilai Transaksi']

        # cari = False
        for idSaham, saham in recycle_bin.items():
                # if saham['hapus'] == True:
                        # cari = True
                        Tabel = PrettyTable()
                        Tabel.field_names = ['ID', 'Kode Saham', 'Nama Perusahaan', 'Harga Pembukaan', 'Harga Penutupan', 'Perubahan Harga', 'Nilai Transaksi']
                        Tabel.title = 'RIWAYAT HAPUS DATA SAHAM KONOHA 2025'
                        harga_pembukaan = nominal(saham['hargaPembukaan'])
                        harga_penutupan = nominal(saham['hargaPenutupan'])
                        perubahan_harga = presentase(saham['perubahan'])
                        nilai_transaksi = nominal(saham['nilai'])
                        Tabel.add_row([idSaham, saham['kode'], saham['perusahaan'], harga_pembukaan, harga_penutupan, perubahan_harga, nilai_transaksi])
        
        if not recycle_bin: 
                print(f"{'Data saham di riwayat hapus kosong':^100}")
                print(f"{'*'*3:^100}")
                input(f"{'Tekan Enter untuk melanjutkan..':^99}")
        else:        
                print(Tabel)
                input('=> Tekan Enter untuk melanjutkan..')

# memulihkan data yg ada di riwayat hapus
def pulihkanData():
        if not recycle_bin:
                return
        else:
                while True:
                        try:
                                idSaham = int(input('=> Masukkan ID saham yang ingin Anda pulihkan: '))
                                break
                        except ValueError:
                                print('Id saham yang anda masukkan tidak valid, id harus berupa angka.')
                                
                if idSaham in recycle_bin:
                        dataSaham[idSaham] = recycle_bin[idSaham]
                        konfirmasi = input('Apakah anda yakin ingin memulihkan data saham tersebut(Ya/Tidak)?: ').capitalize()
                        if konfirmasi == 'Ya':
                                dataSaham[idSaham]['hapus'] = False
                                del recycle_bin[idSaham]
                                print('\nData Saham Berhasil Dipulihkan')
                                menampilkan()  # Menampilkan data yang sudah dipulihkan
                                
                        else:
                                print(f"{'\nData Saham Batal Dipulihkan':^100}")
                                print(f"{'*'*3:^100}")
                        
                else:
                        print(f"{'Data Saham Tidak Ditemukan':^100}")
                        print(f"{'*'*3:^100}")
                        input(f"{'Tekan Enter untuk melanjutkan..':^99}")

# tampilan menu untuk menghapus data  
def hapusData():
        bersihkan_layar() 
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
                               [1] Menghapus Data Saham  
                               [2] Hapus Permanen Data Saham
                               [3] Data Saham Terhapus
                               [4] Pemulihkan Data Saham Terhapus
                               [5] Kembali ke Menu Utama 
                               =======================================
                               => Pilih menu yang ingin Anda akses : ''')
                
                if menuHapus == '1':
                        menghapus()
                elif menuHapus == '2':
                        hapusPermanen()
                elif menuHapus == '3':
                        riwayat_hapus()
                elif menuHapus == '4':
                        riwayat_hapus()
                        pulihkanData()
                elif menuHapus == '5':
                        break
                else: 
                        print('\n')
                        print(f"{'Silahkan pilih menu yang ingin dijalankan':^100}")
                        print(f"{'*'*3:^100}")
                        input(f"{'Tekan Enter untuk melanjutkan..':^99}")

# ****************************
# ********** EXIT **********
# ****************************
# tampilan menu untuk keluar dari pemrograman
def keluarSistem ():
        while True:
                bersihkan_layar()
                print('\n')
                print('='*110)
                print(f"{'SISTEM MANAJEMEN DATA SAHAM KONOHA':^100}")
                print('='*110)
                menuKeluar =   input('''
                               ======================================
                                   Terima Kasih Telah Menggunakan
                                       Sistem Manajemen Saham
                               ======================================
                               Apakah Anda Yakin Ingin Keluar?
                               [1] Ya, Keluar
                               [2] Kembali ke Menu Utama
                               ======================================
                               => Pilih menu yang ingin Anda akses : ''')

                if menuKeluar == '1': 
                        print('\n')
                        print(f"{'TERIMA KASIH...':^100}")
                        print(f"{'*'*3:^100}")
                        print('\n')
                        exit()
                elif menuKeluar == '2':
                        break
                else:
                        print('\n')
                        print(f"{'Pilihan Anda tidak valid.':^100}")
                        print(f"{'*'*3:^100}")
                        input(f"{'Tekan Enter untuk melanjutkan..':^99}")

user()

