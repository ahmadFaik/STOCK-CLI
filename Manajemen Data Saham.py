from prettytable import PrettyTable

dataSaham = {}
dataSaham = { 
        1 :     {'kode':'AADI',
                'perusahaan':'Adaro Andalan Indonesia Tbk.', 
                'hargaPembukaan':6550,
                'hargaPenutupan':6800,
                'perubahan':3.82, 
                'nilai':44460882500, 
                'hapus':False},

        2 :     {'kode':'AALI',
                'perusahaan':'Astra Agro Lestari Tbk.', 
                'hargaPembukaan':5675,
                'hargaPenutupan':5550,
                'perubahan':2.20, 
                'nilai':3764012500, 
                'hapus':False},

        3 :     {'kode':'BBCA',
                'perusahaan':'Bank Central Asia Tbk.',
                'hargaPembukaan':8275,
                'hargaPenutupan':7900,
                'perubahan':-4.53,
                'nilai':736670570000,
                'hapus':False},

        4:      {'kode':'BBRI',
                'perusahaan':'Bank Rakyat Indonesia (Persero) Tbk.', 
                'hargaPembukaan':3930,
                'hargaPenutupan':5550,
                'perubahan':41.23, 
                'nilai':941219074000, 
                'hapus':False},
                
        5 :     {'kode':'BRIS',
                'perusahaan':'Bank Syariah Indonesia Tbk.', 
                'hargaPembukaan':2610,
                'hargaPenutupan':5550,
                'perubahan':112.22, 
                'nilai':85977800000, 
                'hapus':False},

        6 :     {'kode':'BMRI',
                'perusahaan':'Bank Mandiri (Persero) Tbk.', 
                'hargaPembukaan':4870,
                'hargaPenutupan':5550,
                'perubahan':13.97, 
                'nilai':570806151000, 
                'hapus':False},
        
        7 :     {'kode':'GOTO',
                'perusahaan':'GoTo Gojek Tokopedia Tbk.', 
                'hargaPembukaan':81,
                'hargaPenutupan':81,
                'perubahan':0.00, 
                'nilai':436906658200, 
                'hapus':False},

        8 :     {'kode':'TLKM',
                'perusahaan':'Telkom Indonesia (Persero) Tbk.', 
                'hargaPembukaan':2430,
                'hargaPenutupan':5550,
                'perubahan':128.57, 
                'nilai':439964438000, 
                'hapus':False}}

# tampilan menu utama 
def menu_utama():
        while True:
                print('\n')
                print('='*110)
                print(f'{'SISTEM MANAJEMEN DATA SAHAM KONOHA':^100}')
                print('='*110)
                
                Menu_Utama = input('''
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

                if Menu_Utama == '1':
                        tampilkanData()
                elif Menu_Utama == '2':
                        tambahData()
                elif Menu_Utama == '3':
                        ubahData()
                elif Menu_Utama == '4':
                        hapusData()
                elif Menu_Utama == '5':
                        keluarProgram()
                else:
                        print('\n')
                        print(f'{'Silahkan pilih menu yang ingin dijalankan':^100}')
                        print(f'{'*'*3:^100}')
                        input(f'{'Tekan Enter untuk melanjutkan..':^99}')

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

def filter_id():
        while True: 
                try:
                        idSaham = int(input('\t\t\t=> Masukkan ID saham yang ingin ditampilkan: '))
                        break
                except ValueError: 
                        print('\n')
                        print(f"{'Maaf, ID yang Anda masukkan tidak valid. Pastikan ID berupa angka dan coba lagi.':^100}")
                        print(f'{'*'*3:^100}')
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
                print('\n')
                print(f"{'Data dengan ID yang Anda masukkan tidak terdeteksi. Pastikan ID benar.':^100}")
                print(f'{'*'*3:^100}')
                input(f'{'Tekan Enter untuk melanjutkan..':^99}')

def filter_kode():
        kodeSaham = input('\t\t\t=> Masukkan kode saham yang ingin ditampilkan: ').upper()
        
        print('\n')
        cari_kode = False 
        for i, data in dataSaham.items(): # Menampilkan data berdasarkan kode saham tertentu
                if kodeSaham in data.values(): 
                        cari_kode = True
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
        
        if cari_kode == False: 
                print(f'Data dengan kode {kodeSaham} yang Anda masukkan tidak terdeteksi. Pastikan kode saham benar.')

        input('=> Tekan Enter untuk melanjutkan..')

def filter_harga():
        while True: 
                try:
                        harga = int(input('\t\t\t=> Masukkan harga saham yang ingin ditampilkan: '))
                        break
                except ValueError:
                        print('\n')
                        print(f"{'Maaf, harga saham yang Anda masukkan tidak valid. Pastikan harga berupa angka dan coba lagi.':^100}")
                        print(f'{'*'*3:^100}')
        print('\n')
        cari_harga = False
        for i, data in dataSaham.items(): # Menampilkan data berdasarkan harga saham tertentu, baik harga pembukaan maupun penutupan.
                if data['hargaPembukaan'] == harga or data['hargaPenutupan'] == harga: #problem: kalo ada beberapa data yg ditemukan, maka akan ditampilkan datanya di tabel yg berbeda
                        cari_harga = True
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
        
        if cari_harga == False:
                print('\n')
                print(f"{'Pencarian tidak ditemukan. Pastikan harga pembukaan atau penutupan saham yang Anda masukkan sudah benar':^100}")
                print(f'{'*'*3:^100}')
                input(f'{'Tekan Enter untuk melanjutkan..':^99}')

def tampilkanData():
        while True:
                print('\r\n')
                print('='*110)
                print(f'{'SISTEM MANAJEMEN DATA SAHAM KONOHA':^100}')
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
                                print(f'{'\nData Saham Tidak Ditemukan':^100}')
                                print(f'{'*'*3:^100}')
                elif menuCari == '2': # Menampilkan data saham berdasarkan ID saham
                        filter_id()
                elif menuCari == '3': # Menampilkan data saham berdasarkan kode saham
                        filter_kode()
                elif menuCari == '4': # Menampilkan data saham berdasarkan harga pembukaan/penutupan saham
                        filter_harga()
                elif menuCari == '5': # Kembali ke menu utama 
                        menu_utama()
                else:
                        print('\n')
                        print(f"{'Opsi yang Anda pilih tidak tersedia. Pilih menu yang valid dan coba lagi.':^100}")
                        print(f'{'*'*3:^100}')
                        input(f'{'Tekan Enter untuk melanjutkan..':^99}')

# *********************************
# ********** CREATE DATA **********
# *********************************
def cekKode():
        while True:    # User menambahkan kode saham baru 
                Kode = input('Masukkan kode saham\t\t: ').upper() 
                if Kode.isalpha(): 
                        return Kode
                else: 
                        print('Input yang Anda berikan tidak valid. Silakan periksa dan coba lagi.')

def cekHargaPembukaan():
        while True: 
                try:    # User menambahkan harga pembukaan saham
                        hargaPembukaan = int(input('Masukkan harga pembukaan saham\t: '))
                        if hargaPembukaan <= 0:
                                print('\nMaaf, harga yang Anda masukkan tidak valid. Pastikan harga lebih dari 0.\n')  
                        else:
                                return hargaPembukaan
                except IndexError:
                        print('\nMaaf, harga yang Anda masukkan tidak valid. Pastikan harga berupa angka dan coba lagi.\n')
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
                except IndexError:
                        print('\nMaaf, harga yang Anda masukkan tidak valid. Pastikan harga berupa angka dan coba lagi.\n')
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
                except IndexError:
                        print('\nMaaf, nilai transaksi saham yang Anda masukkan tidak valid. Pastikan nilai berupa angka dan coba lagi.\n')
                except ValueError:
                        print('\nNilai transaksi saham yang anda masukkan tidak valid\n')

def menambahkan():
        while True:
                try:    # User menambahkan ID saham baru 
                        ID = int(input('\nMasukkan ID saham baru\t\t: ')) 
                        if ID <= 0:
                                raise IndexError('\nMaaf, ID yang Anda masukkan tidak valid.\n') 
                        break
                except IndexError:
                        print('\nMaaf, ID yang Anda masukkan tidak valid. Pastikan ID berupa angka dan coba lagi.\n')
                except ValueError:
                        print('\nMaaf, ID yang Anda masukkan tidak valid. Pastikan ID berupa angka dan coba lagi.\n')
        
        if ID in dataSaham: 
                print('\nID yang Anda masukkan sudah terdaftar dalam data. Silahkan coba ID baru.\n')
                saham = dataSaham[ID]
                Tabel = PrettyTable()
                Tabel.field_names = ['ID', 'Kode Saham', 'Nama Perusahaan', 'Harga Pembukaan', 'Harga Penutupan', 'Perubahan Harga', 'Nilai Transaksi']
                Tabel.title = 'RINGKASAN PASAR SAHAM KONOHA 2025'
                harga_pembukaan = nominal(saham['hargaPembukaan'])
                harga_penutupan = nominal(saham['hargaPenutupan'])
                perubahan_harga = presentase(saham['perubahan'])
                nilai_transaksi = nominal(saham['nilai'])
                Tabel.add_row([ID, saham['kode'], saham['perusahaan'], harga_pembukaan, harga_penutupan, perubahan_harga, nilai_transaksi])
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
                        perusahaan = input('Masukkan Nama Perusahaan\t: ').title()
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
                                perubahanHarga = cekPerubahan(hargaPembukaan, hargaPenutupan) # Menampilkan nilai perubahan harga saham
                                nilai = cekNilai() # User menambahkan total nilai transaksi saham tersebut
                                # Menampung & menampilkan data baru yg ditambahkan 
                                print('\nData Baru:')
                                dataSaham[ID] = {
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
                                Tabel.add_row([ID, kode, perusahaan, harga_pembukaan, harga_penutupan, perubahan_harga, nilai_transaksi])
                                print(Tabel)
                                        
                                simpan = input('\nPastikan data yang Anda masukkan sudah benar. \nApakan Anda ingin menyimpan data baru tersebut? (Ya/Tidak): ').capitalize()
                                if simpan == 'Ya':
                                        print(f"Data saham berhasil ditambahkan.")
                                        menampilkan()
                                else:
                                        print(f"Penambahan data saham dibatalkan.\n")
                                        tambahData()

        input('=> Tekan Enter untuk melanjutkan..')

def tambahData():
        while True:
                print('\r\n')
                print('='*110)
                print(f'{'SISTEM MANAJEMEN DATA SAHAM KONOHA':^100}')
                print('='*110)

                menuTambah = input('''
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
                        if len(dataSaham) > 0:
                                menambahkan() 
                        else:
                                print(f'{'Data Saham Tidak Ditemukan':^100}')
                                print(f'{'*'*3:^100}')
                elif menuTambah == '2':
                        menu_utama()
                else:
                        print('\n')
                        print(f"{'Opsi yang Anda pilih tidak tersedia. Pilih menu yang valid dan coba lagi.':^100}")
                        print(f'{'*'*3:^100}')

                input(f'{'Tekan Enter untuk melanjutkan..':^99}')

# ****************************
# ********** UPDATE **********
# **************************** 
def memperbarui():
        while True: 
                try:    # User input ID yang ingin diperbarui
                        ID = int(input('Masukkan ID saham yang ingin diperbarui: '))
                        break
                except ValueError:
                        print('\n')
                        print(f"{'Maaf, ID yang Anda masukkan tidak valid. Pastikan ID berupa angka dan coba lagi.':^100}")
                        print(f'{'*'*3:^100}')
                        print('\n')

        if ID in dataSaham:
                print('\n')
                saham = dataSaham[ID] # Menampilkan data saham berdasarkan ID yang ingin diperbarui
                Tabel = PrettyTable()
                Tabel.field_names = ['ID', 'Kode Saham', 'Nama Perusahaan', 'Harga Pembukaan', 'Harga Penutupan', 'Perubahan Harga', 'Nilai Transaksi']
                Tabel.title = 'RINGKASAN PASAR SAHAM KONOHA 2025'
                harga_pembukaan = nominal(saham['hargaPembukaan'])
                harga_penutupan = nominal(saham['hargaPenutupan'])
                perubahan_harga = presentase(saham['perubahan'])
                nilai_transaksi = nominal(saham['nilai'])
                Tabel.add_row([ID, saham['kode'], saham['perusahaan'], harga_pembukaan, harga_penutupan, perubahan_harga, nilai_transaksi])
                print(Tabel)  

                konfirmasi = input('Apakah Anda ingin melanjutkan untuk memperbarui data tersebut (Ya/Tidak)?: ').capitalize()
                if konfirmasi == 'Ya':
                        kolom = input('''
                        Daftar kolom: 
                        [1] Kode Saham
                        [2] Nama Perusahaan
                        [3] Harga Pembukaan
                        [4] Harga Penutupan
                        [5] Perubahan Harga 
                        [6] Nilai Transaksi  
                        => Masukkan kolom yang ingin diperbarui: ''')
                        
                        if kolom == '1': # Memperbarui kode saham  
                                Kode = cekKode()
                                dataSaham[ID]['kode'] = Kode
                        elif kolom == '2': # Memperbarui nama perusahaan
                                Perusahaan = input('Masukkan nama perusahaan: ').title()
                                dataSaham[ID]['perusahaan'] = Perusahaan
                        elif kolom == '3': # Memperbarui harga pembukaan saham
                                HargaPembukaan = cekHargaPembukaan()
                                HargaPembukaan = nominal(HargaPembukaan)
                                dataSaham[ID]['hargaPembukaan'] = HargaPembukaan
                        elif kolom == '4': # Memperbarui harga penutupan saham
                                HargaPenutupan = cekHargaPenutupan()
                                HargaPenutupan = nominal(HargaPenutupan)
                                dataSaham[ID]['hargaPenutupan'] = HargaPenutupan
                        elif kolom == '5': # Memperbarui persentase perubahan harga saham
                                hargaPembukaan = cekHargaPembukaan()
                                hargaPenutupan = cekHargaPenutupan()
                                perubahan = cekPerubahan(hargaPembukaan, hargaPenutupan) # Hitung perubahan harga
                                if perubahan is not None:
                                        # Ubah perubahan ke format persentase
                                        perubahan = presentase(perubahan)
                                        # Update data saham
                                        dataSaham[ID]['hargaPembukaan'] = hargaPembukaan
                                        dataSaham[ID]['hargaPenutupan'] = hargaPenutupan
                                        dataSaham[ID]['perubahan'] = perubahan

                                        # if perubahan > 10:
                                        #         print('\nHarga berubah sangat signifikan!\n')
                                        # elif perubahan <= 10:
                                        #         print('\nHarga berubah cukup signifikan\n')
                                        # else:
                                        #         print('\nHarga tidak mengalami perubahan\n')
                                else:
                                        print("Nilai perubahan tidak dapat dihitung. Pastikan Anda memasukkan data dengan benar.")
                        elif kolom == '6': # Memperbarui nilai transaksi saham
                                Nilai = cekNilai()
                                Nilai = nominal(Nilai)
                                dataSaham[ID]['nilai'] = Nilai
                        else:
                                print('\n')
                                print(f'{'Kolom yang Anda pilih tidak ditemukan. Silakan pilih kolom yang valid untuk diperbarui.':^100}')
                                print(f'{'*'*3:^100}')
                                memperbarui()

                        simpan = input('Apakah data tersebut mau disimpan (Ya/Tidak)?: ').capitalize()
                        if simpan == 'Ya':
                                print(f"\nData saham {dataSaham[ID]['perusahaan']} berhasil diperbarui\n")
                        else:
                                print(f"\nPembaruan data saham {dataSaham[ID]['perusahaan']} dibatalkan. Tidak ada perubahan yang dilakukan.\n")
                                ubahData()
                else:
                        ubahData()
                
        else:
                print(f"{'Data dengan ID yang Anda masukkan tidak terdeteksi. Pastikan ID benar.':^100}")
                print(f'{'*'*3:^100}')

        input(f'{'Tekan Enter untuk melanjutkan..':^99}')

def ubahData():
        while True:
                print('\r\n')
                print('='*110)
                print(f'{'SISTEM MANAJEMEN DATA SAHAM KONOHA':^100}')
                print('='*110)

                menuUpdate = input('''
                        =====================================
                          *** Pembaruan Data Saham 2025 ***
                        =====================================
                        Daftar Menu Pembaruan:
                        =====================================
                        [1] Memperbarui Data Saham  
                        [2] Kembali ke Menu Utama 
                        =====================================
                        => Pilih menu yang ingin Anda akses : ''')
                
                if menuUpdate == '1':
                        memperbarui() # Memperbarui data saham berdasarkan ID saham
                        menampilkan()
                elif menuUpdate == '2':
                        menu_utama()
                else:
                        print('\n')
                        print(f"{'Opsi yang Anda pilih tidak tersedia. Pilih menu yang valid dan coba lagi.':^100}")
                        print(f'{'*'*3:^100}')
                        input(f'{'Tekan Enter untuk melanjutkan..':^99}')

# ****************************
# ********** DELETE **********
# ****************************
recycle_bin = {} # untuk menampung data yg dihapus
def menghapus():
        while True:
                try:    # Menghapus data saham berdasarkan ID saham (soft deleted)
                        id = int(input('\t\t\t=> "Masukkan ID saham yang ingin Anda pilih untuk dihapus: '))
                        break
                except ValueError:
                        print('\n')
                        print(f"{'Maaf, ID yang Anda masukkan tidak valid. Pastikan ID berupa angka dan coba lagi.':^100}")
                        print(f'{'*'*3:^100}')
                        print('\n')

        if id in dataSaham:
                print('\n')
                saham = dataSaham[id]
                Tabel = PrettyTable()
                Tabel = PrettyTable()
                Tabel.field_names = ['ID', 'Kode Saham', 'Nama Perusahaan', 'Harga Pembukaan', 'Harga Penutupan', 'Perubahan Harga', 'Nilai Transaksi']
                Tabel.title = 'RINGKASAN PASAR SAHAM KONOHA 2025'
                harga_pembukaan = nominal(saham['hargaPembukaan'])
                harga_penutupan = nominal(saham['hargaPenutupan'])
                perubahan_harga = presentase(saham['perubahan'])
                nilai_transaksi = nominal(saham['nilai'])
                Tabel.add_row([id, saham['kode'], saham['perusahaan'], harga_pembukaan, harga_penutupan, perubahan_harga, nilai_transaksi])                
                print(Tabel)

                konfirmasi = input('Apakah Anda yakin ingin menghapus data saham tersebut (Ya/Tidak)?: ').capitalize()
                if konfirmasi == 'Ya':
                        recycle_bin[id] = dataSaham[id]
                        dataSaham[id]['hapus'] = True
                        del dataSaham[id]
                        print('\n')
                        print(f'{'Data saham berhasil dihapus':^100}')
                        print(f'{'*'*3:^100}')
                        menampilkan()
                else:
                        print('\n')
                        print(f'{'Data saham batal dihapus':^100}')
                        print(f'{'*'*3:^100}')
                        menu_utama()
        else:
                print('\n')
                print(f'{'Data Saham Tidak Ditemukan':^100}')
                print(f'{'*'*3:^100}')

        input(f'{'Tekan Enter untuk melanjutkan..':^99}')

# menghapus data berdasarkan id untuk hard deleted
def hapusPermanen():
        while True:
                try:
                        id = int(input('\t\t\t=> Masukkan id yang ingin dihapus: '))
                        break
                except ValueError:
                        print('\n')
                        print(f"{'Maaf, ID yang Anda masukkan tidak valid. Pastikan ID berupa angka dan coba lagi.':^100}")
                        print(f'{'*'*3:^100}')
                        print('\n')
                        
        if id in dataSaham:
                print('\n')
                saham = dataSaham[id]
                Tabel = PrettyTable()
                Tabel.field_names = ['ID', 'Kode Saham', 'Nama Perusahaan', 'Harga Pembukaan', 'Harga Penutupan', 'Perubahan Harga', 'Nilai Transaksi']
                Tabel.title = 'RINGKASAN PASAR SAHAM KONOHA 2025'
                harga_pembukaan = nominal(saham['hargaPembukaan'])
                harga_penutupan = nominal(saham['hargaPenutupan'])
                perubahan_harga = presentase(saham['perubahan'])
                nilai_transaksi = nominal(saham['nilai'])
                Tabel.add_row([id, saham['kode'], saham['perusahaan'], harga_pembukaan, harga_penutupan, perubahan_harga, nilai_transaksi])
                print(Tabel)  

                konfirmasi = input('Apakah ingin melanjutkan menghapus data saham (Ya/Tidak)?: ').capitalize()
                if konfirmasi == 'Ya':
                        del dataSaham[id]
                        menampilkan()
                        print('\n')
                        print(f'{'Data saham batal dihapus':^100}')
                        print(f'{'*'*3:^100}')
                else:
                        print('\n')
                        print(f'{'Data saham batal dihapus':^100}')
                        print(f'{'*'*3:^100}')
                        menu_utama()
        else:
                print(f'{'Data Saham Tidak Ditemukan':^100}')
                print(f'{'*'*3:^100}')

        input(f'{'Tekan Enter untuk melanjutkan..':^99}')

# menampilkan data yg soft deleted
def riwayat_hapus():
        print('\n')
        Tabel = PrettyTable()
        Tabel.field_names = ['ID', 'Kode Saham', 'Nama Perusahaan', 'Harga Pembukaan', 'Harga Penutupan', 'Perubahan Harga', 'Nilai Transaksi']

        # cari = False
        for id, saham in recycle_bin.items():
                # if saham['hapus'] == True:
                        # cari = True
                        Tabel = PrettyTable()
                        Tabel.field_names = ['ID', 'Kode Saham', 'Nama Perusahaan', 'Harga Pembukaan', 'Harga Penutupan', 'Perubahan Harga', 'Nilai Transaksi']
                        Tabel.title = 'RINGKASAN PASAR SAHAM KONOHA 2025'
                        harga_pembukaan = nominal(saham['hargaPembukaan'])
                        harga_penutupan = nominal(saham['hargaPenutupan'])
                        perubahan_harga = presentase(saham['perubahan'])
                        nilai_transaksi = nominal(saham['nilai'])
                        Tabel.add_row([id, saham['kode'], saham['perusahaan'], harga_pembukaan, harga_penutupan, perubahan_harga, nilai_transaksi])
        
        if not recycle_bin: 
                print(f"{'Data saham di riwayat hapus kosong':^100}")
                print(f"{'*'*3:^100}")
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
                                id = int(input('\t\t\t=> Masukkan id yang ingin dihapus: '))
                                break
                        except ValueError:
                                print('Id saham yang anda masukkan tidak valid, id harus berupa angka.')
                                
                if id in recycle_bin:
                        dataSaham[id] = recycle_bin[id]
                        konfirmasi = input('Apakah anda yakin ingin memulihkan data saham tersebut(Ya/Tidak)?: ').capitalize()
                        if konfirmasi == 'Ya':
                                dataSaham[id]['hapus'] = False
                                del recycle_bin[id]
                                print('\nData Saham Berhasil Dipulihkan')
                                menampilkan()  # Menampilkan data yang sudah dipulihkan
                                input('=> Tekan Enter untuk melanjutkan..')
                                
                        else:
                                print(f'{'\nData Saham Batal Dipulihkan':^100}')
                                print(f'{'*'*3:^100}')
                                menu_utama() # Panggil menu utama jika tidak jadi dipulihkan
                        
                else:
                        print(f'{'Data Saham Tidak Ditemukan':^100}')
                        print(f'{'*'*3:^100}')

        input(f'{'Tekan Enter untuk melanjutkan..':^99}')

# tampilan menu untuk menghapus data  
def hapusData():
        while True:
                print('\r\n')
                print('='*110)
                print(f'{'SISTEM MANAJEMEN DATA SAHAM KONOHA':^100}')
                print('='*110)

                menuHapus = input('''
                        ===================================
                        *** Penghapusan Data Saham 2025 ***
                        ===================================
                        Daftar Menu Penghapusan:
                        ===================================
                        [1] Menghapus Data Saham  
                        [2] Hapus Permanen Data Saham
                        [3] Data Saham Terhapus
                        [4] Pemulihkan Data Saham Terhapus
                        [5] Kembali ke Menu Utama 
                        ===================================
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
                        menu_utama()
                else: 
                        print('\n')
                        print(f'{'Silahkan pilih menu yang ingin dijalankan':^100}')
                        print(f'{'*'*3:^100}')
                        input(f'{'Tekan Enter untuk melanjutkan..':^99}')

# ****************************
# ********** EXIT **********
# ****************************
# tampilan menu untuk keluar dari pemrograman
def keluarProgram ():
                menuKeluar = input('''
                        =====================================
                            Terima Kasih Telah Menggunakan
                                Sistem Manajemen Saham
                        =====================================
                        Apakah Anda Yakin Ingin Keluar?
                        [1] Ya, Keluar
                        [2] Kembali ke Menu Utama
                        =====================================
                        => Pilih menu yang ingin Anda akses : ''')

                if menuKeluar == '1': 
                        print('\n')
                        print(f'{'TERIMA KASIH...😊':^80}')
                        print(f'{'*'*3:^80}')
                        print('\n')
                        exit()
                elif menuKeluar == '2':
                        menu_utama()
                else:
                        print('\n')
                        print(f'{'Pilihan Anda tidak valid.':^100}')
                        print(f'{'*'*3:^100}')
                        input(f'{'Tekan Enter untuk melanjutkan..':^99}')

menu_utama()
