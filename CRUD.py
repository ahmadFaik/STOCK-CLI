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

def nominal(angka):
        if isinstance(angka, str): 
                angka = angka.replace(',', '') 
        return f'{float(angka):,.2f}' # Format nominal ribuan

def presentase(perubahan): 
        if isinstance(perubahan, str):
                perubahan = perubahan.replace('%', '') 
        return f'{float(perubahan):.2f}%' # Format dalam bentuk presentase

# *******************************
# ********** READ DATA **********
# *******************************
def menampilkan(): 
        print('\n')
        Tabel = PrettyTable()
        Tabel.field_names = ['ID', 'Kode Saham', 'Nama Perusahaan', 'Harga Pembukaan', 'Harga Penutupan', 'Perubahan Harga', 'Nilai Transaksi']

        for id, saham in dataSaham.items(): # Menampilkan semua data saham
                if saham['hapus'] == False: 
                        Tabel.title = 'RINGKASAN PASAR SAHAM KONOHA 2025'
                        harga_pembukaan = nominal(saham['hargaPembukaan'])
                        harga_penutupan = nominal(saham['hargaPenutupan'])
                        perubahan_harga = presentase(saham['perubahan'])
                        nilai_transaksi = nominal(saham['nilai'])
                        Tabel.add_row([id, saham['kode'], saham['perusahaan'], harga_pembukaan, harga_penutupan, perubahan_harga, nilai_transaksi])
        print(Tabel)

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
        else:
                print(f"{'Data dengan ID yang Anda masukkan tidak terdeteksi. Pastikan ID benar.':^100}")
                print(f'{'*'*3:^100}')

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
                print(f'{'Data dengan kode {kodeSaham} yang Anda masukkan tidak terdeteksi. Pastikan ID benar.':^100}')
                print(f'{'*'*3:^100}')

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
                        
        if cari_harga == False:
                print(f"{'\nPencarian tidak ditemukan. Pastikan harga pembukaan atau penutupan saham yang Anda masukkan sudah benar':^100}")
                print(f'{'*'*3:^100}')

def read():
        while True:
                print('\r\n')
                print('='*110)
                print(f'{'SISTEM MANAJEMEN DATA SAHAM KONOHA':^100}')
                print('='*110)

                menuRead = input('''
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

                if menuRead == '1': # Menampilkan semua data saham
                        if len(dataSaham) > 0: 
                                menampilkan()
                        else:
                                print(f'{'\nData Saham Tidak Ditemukan':^100}')
                                print(f'{'*'*3:^100}')
                elif menuRead == '2': # Menampilkan data saham berdasarkan ID saham
                        filter_id()
                elif menuRead == '3': # Menampilkan data saham berdasarkan kode saham
                        filter_kode()
                elif menuRead == '4': # Menampilkan data saham berdasarkan harga pembukaan/penutupan saham
                        filter_harga()
                elif menuRead == '5': # Kembali ke menu utama 
                        menu_utama()
                else:
                        print('\n')
                        print(f"{'Opsi yang Anda pilih tidak tersedia. Pilih menu yang valid dan coba lagi.':^100}")
                        print(f'{'*'*3:^100}')

# *********************************
# ********** CREATE DATA **********
# *********************************
def cekKode():
        while True:    # User menambahkan kode saham baru 
                Kode = input('Masukkan kode saham: ').upper() 
                if Kode.isalpha():
                        break
                else: 
                        print('Input yang Anda berikan tidak valid. Silakan periksa dan coba lagi.')

def cekHargaPembukaan():
        while True: 
                try:    # User menambahkan harga pembukaan saham
                        hargaPembukaan = int(input('Masukkan harga pembukaan saham: '))
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
                        hargaPenutupan = int(input('Masukkan harga penutupan saham: '))
                        if hargaPenutupan <= 0:
                                print('\nMaaf, harga yang Anda masukkan tidak valid. Pastikan harga lebih dari 0.\n')  
                        else:
                                return hargaPenutupan
                except IndexError:
                        print('\nMaaf, harga yang Anda masukkan tidak valid. Pastikan harga berupa angka dan coba lagi.\n')
                except ValueError:
                        print('\nMaaf, harga yang Anda masukkan tidak valid. Pastikan harga berupa angka dan coba lagi.\n')


def cekperubahan(hargaPembukaan, hargaPenutupan):
        if hargaPembukaan == 0: 
                return 0
        # Menghitung persentase perubahan harga saham
        perubahan = ((hargaPenutupan - hargaPembukaan) / hargaPembukaan) * 100
        return perubahan

def cekNilai():
        while True:
                try:    # User menambahkan nilai transaksi saham
                        nilai = int(input('Masukkan nilai transaksi saham: '))
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
                        ID = int(input('Masukkan ID saham baru\t\t: ')) 
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
                kode = input('Masukkan Kode Saham\t\t: ').upper()
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
                                perubahan = cekperubahan(hargaPembukaan, hargaPenutupan) # Menampilkan nilai perubahan harga saham
                                nilai = cekNilai() # User menambahkan total nilai transaksi saham tersebut
                                # menampung value baru yg ditambahkan 
                                dataSaham[ID] = {'kode':kode,
                                                'perusahaan':perusahaan, 
                                                'hargaPembukaan':nominal(hargaPembukaan),
                                                'hargaPenutupan':nominal(hargaPenutupan),
                                                'perubahan':presentase(perubahan), 
                                                'nilai':nominal(nilai), 
                                                'hapus':False}
                                simpan = input('\nPastikan data yang Anda masukkan sudah benar. \nApakan Anda ingin menyimpan data baru tersebut? (Ya/Tidak): ').capitalize()
                                if simpan == 'Ya':
                                        menampilkan()
                                else:
                                        menambahkan()   

def create():
        while True:
                print('\r\n')
                print('='*110)
                print(f'{'SISTEM MANAJEMEN DATA SAHAM KONOHA':^100}')
                print('='*110)

                menuCreate = input('''
                        ===================================
                        *** Penambahan Data Saham 2025 ***
                        ===================================
                        Daftar Menu Penambahan:
                        =================================== 
                        [1] Menambahkan Data Saham  
                        [2] Kembali ke Menu Utama 
                        ===================================
                        => Pilih menu yang ingin Anda akses : ''')

                if menuCreate == '1':
                        if len(dataSaham) > 0:
                                menambahkan() 
                        else:
                                print('Data Saham Tidak Ditemukan')
                elif menuCreate == '2':
                        menu_utama()
                else:
                        print('\n')
                        print(f"{'Opsi yang Anda pilih tidak tersedia. Pilih menu yang valid dan coba lagi.':^100}")
                        print(f'{'*'*3:^100}')

# ****************************
# ********** UPDATE **********
# **************************** 
def memperbarui():
        while True:
                try:
                        ID = int(input('Masukkan id yang ingin diperbarui: '))
                        break
                except:
                        print('Id yang anda masukkan tidak valid')

        if ID in dataSaham:
                print('\n')
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
                konfirmasi = input('Apakah anda ingin melanjutkan untuk memperbarui data (Ya/Tidak)? ').capitalize()
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
                        if kolom == '1':
                                Kode = cekKode()
                                dataSaham[ID]['kode'] = Kode
                        elif kolom == '2':
                                Perusahaan = input('Masukkan nama perusahaan: ').title()
                                dataSaham[ID]['perusahaan'] = Perusahaan
                        elif kolom == '3':
                                HargaPembukaan = cekHargaPembukaan()
                                HargaPembukaan = nominal(HargaPembukaan)
                                dataSaham[ID]['hargaPembukaan'] = HargaPembukaan
                        elif kolom == '4':
                                HargaPenutupan = cekHargaPenutupan()
                                HargaPenutupan = nominal(HargaPenutupan)
                                dataSaham[ID]['hargaPenutupan'] = HargaPenutupan
                        elif kolom == '5':
                                # Ambil harga pembukaan dan harga penutupan baru
                                hargaPembukaan = cekHargaPembukaan()
                                hargaPenutupan = cekHargaPenutupan()

                                # Hitung perubahan harga
                                perubahan = cekperubahan(hargaPembukaan, hargaPenutupan)

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
                                        print("Perubahan tidak dapat dihitung karena harga pembukaan 0.")

                        elif kolom == '6':
                                Nilai = cekNilai()
                                Nilai = nominal(Nilai)
                                dataSaham[ID]['nilai'] = Nilai
                        else:
                                print('\n')
                                print(f'{'Silahkan pilih kolom yang ingin dijalankan':^100}')
                                print(f'{'*'*3:^100}')
                                memperbarui()

                        simpan = input('Apakah data tersebut mau disimpan (Ya/Tidak)? ').capitalize()
                        if simpan == 'Ya':
                                print(f"\nData saham {dataSaham[ID]['perusahaan']} berhasil diperbarui\n")
                        else:
                                print(f"\nData saham {dataSaham[ID]['perusahaan']} tidak berhasil diperbarui\n")
                                update()
                else:
                        update()
                        
        else:
                print('Data yang anda cari tidak terdaftar')

# tampilan menu untuk memperbarui data
def update():
        while True:
                print('\r\n')
                print('='*110)
                print(f'{'SISTEM MANAJEMEN DATA SAHAM KONOHA':^100}')
                print('='*110)

                user = input('''
                        ===================================
                         *** Pembaruan Data Saham 2025 ***
                        ===================================
                        Daftar Menu Pembaruan:
                        ===================================
                        [1] Memperbarui Data Saham  
                        [2] Kembali ke Menu Utama 
                        ===================================
                        => Pilih menu yang ingin Anda akses : ''')
                
                if user == '1':
                        memperbarui()
                        menampilkan()
                elif user == '2':
                        menu_utama()
                else:
                        print('\n')
                        print(f'{'Silahkan pilih menu yang ingin dijalankan':^100}')
                        print(f'{'*'*3:^100}')

# ****************************
# ********** DELETE **********
# ****************************
recycle_bin = {} # untuk menampung data yg dihapus
# menghapus data berdasarkan id untuk soft deleted
def menghapus():
        while True:
                try:
                        id = int(input('\t\t\t=> Masukkan id yang ingin dihapus: '))
                        break
                except ValueError:
                        print('\n')
                        print(f'{'Id yang anda masukkan tidak valid':^100}')
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
                konfirmasi = input('Apakah ingin melanjutkan menghapus data saham (Ya/Tidak)? ').capitalize()
                if konfirmasi == 'Ya':
                        recycle_bin[id] = dataSaham[id]
                        dataSaham[id]['hapus'] = True
                        del dataSaham[id]
                        menampilkan()
                        print('Data saham berhasil dihapus')
                else:
                        print('\n')
                        print(f'{'Data saham batal dihapus':^100}')
                        print(f'{'*'*3:^100}')
                        menu_utama()
        else:
                print('\n')
                print(f'{'Data Saham Tidak Ditemukan':^100}')
                print(f'{'*'*3:^100}')

# menghapus data berdasarkan id untuk hard deleted
def hard_delete():
        while True:
                try:
                        id = int(input('\t\t\t=> Masukkan id yang ingin dihapus: '))
                        break
                except ValueError:
                        print('Id yang anda masukkan tidak valid')
                        
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
                konfirmasi = input('Apakah ingin melanjutkan menghapus data saham (Ya/Tidak)? ').capitalize()
                if konfirmasi == 'Ya':
                        del dataSaham[id]
                        menampilkan()
                        print('Data saham berhasil dihapus')
                else:
                        print('\n')
                        print(f'{'Data saham batal dihapus':^100}')
                        print(f'{'*'*3:^100}')
                        menu_utama()
        else:
                print(f'{'Data Saham Tidak Ditemukan':^100}')
                print(f'{'*'*3:^100}')

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

# memulihkan data yg ada di riwayat hapus
def restore():
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
                        konfirmasi = input('Apakah anda yakin ingin memulihkan data saham tersebut(Ya/Tidak)? ').capitalize()
                        if konfirmasi == 'Ya':
                                dataSaham[id]['hapus'] = False
                                del recycle_bin[id]
                                print(f"{'\nData Saham Berhasil Dipulihkan':^100}")
                                print(f"{'*'*3:^100}")
                                menampilkan()  # Menampilkan data yang sudah dipulihkan
                        else:
                                print(f'{'\nData Saham Batal Dipulihkan':^100}')
                                print(f'{'*'*3:^100}')
                                menu_utama() # Panggil menu utama jika tidak jadi dipulihkan
                        
                else:
                        print(f'{'Data Saham Tidak Ditemukan':^100}')
                        print(f'{'*'*3:^100}')

# tampilan menu untuk menghapus data  
def delete():
        while True:
                print('\r\n')
                print('='*110)
                print(f'{'SISTEM MANAJEMEN DATA SAHAM KONOHA':^100}')
                print('='*110)

                user = input('''
                        ===================================
                        *** Penghapusan Data Saham 2025 ***
                        ===================================
                        Daftar Menu Penghapusan:
                        ===================================
                        [1] Menghapus Data Saham  
                        [2] Hapus Permanen Data Saham
                        [3] Data Saham Terhapus
                        [4] Pemulihan Data Saham Terhapus
                        [5] Kembali ke Menu Utama 
                        ===================================
                        => Pilih menu yang ingin Anda akses : ''')
                
                if user == '1':
                        menghapus()
                elif user == '2':
                        hard_delete()
                elif user == '3':
                        riwayat_hapus()
                elif user == '4':
                        riwayat_hapus()
                        restore()
                elif user == '5':
                        menu_utama()
                else: 
                        print('\n')
                        print(f'{'Silahkan pilih menu yang ingin dijalankan':^100}')
                        print(f'{'*'*3:^100}')

# ****************************
# ********** EXIT **********
# ****************************
# tampilan menu untuk keluar dari pemrograman
def exit_menu():
                user = input('''
                        =================================
                         Terima Kasih Telah Menggunakan
                             Sistem Manajemen Saham
                        =================================
                        Apakah Anda Yakin Ingin Keluar?
                        [1] Ya, Keluar
                        [2] Kembali ke Menu Utama
                        =================================
                        => Pilih menu yang ingin Anda akses : ''')

                if user == '1': 
                        print('\n')
                        print(f'{'TERIMA KASIH...😊':^80}')
                        print(f'{'*'*3:^80}')
                        print('\n')
                        exit()

                elif user == '2':
                        menu_utama()
                else:
                        print('Pilihan anda tidak valid')

# tampilan menu utama 
def menu_utama():
        while True:
                print('\n')
                print('='*110)
                print(f'{'SISTEM MANAJEMEN DATA SAHAM KONOHA':^100}')
                print('='*110)
                
                menu = input('''
                        =================================
                        *** Manajemen Data Saham 2025 ***
                        =================================
                        Daftar Menu Utama: 
                        [1] Menampilkan Data Saham 
                        [2] Menambah Data Saham 
                        [3] Memperbarui Data Saham 
                        [4] Menghapus Data Saham           
                        [5] Keluar   
                        =================================
                        => Pilih menu yang ingin Anda akses : ''')

                if menu == '1':
                        read()
                elif menu == '2':
                        create()
                elif menu == '3':
                        update()
                elif menu == '4':
                        delete()
                elif menu == '5':
                        exit_menu()
                else:
                        print('\n')
                        print(f'{'Silahkan pilih menu yang ingin dijalankan':^100}')
                        print(f'{'*'*3:^100}')

menu_utama()
