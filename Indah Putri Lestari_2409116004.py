#Login sederhana menggunakan Nama, NIM, Fakultas, PIN
print('--------------------------PROGRAM INDAH-----------------------------')
print('                 Selamat Datang di Program INDAH              ')
print('====================================================================')
print('Silahkan Login Terlebih Dahulu')
#Memasukkan Nama
nama = str(input('Masukkan Nama Anda: '))

#Memasukkan NIM wajib pakai angka
while True:
    nim = (input('Masukkan NIM Anda: '))
    if nim.isdigit():
        break #Karena memasukkan NIM angka
    else:
        print('NIM tidak benar, harap memasukkan NIM dengan angka ')

#Memasukkan nama fakultas
fakultas = str(input('Masukkan Fakultas Anda: '))

#Memasukkan PIN 4 angka
while True:
    PIN = (input('Masukkan PIN Anda: '))
    if len(PIN) != 4 or not PIN.isdigit(): #Mengecek PIN sudah sesuai atau belum
        print('PIN yang anda masukkan salah, Silahkan coba lagi dan masukkan 4 digit angka')
    else:
        print('Login Success!')
        break
print(f'Haloo!, Welcome {nama}') #Berhasil login dan sapaan kepada penggune
print('\n')
print('==================MENGHITUNG TOTAL HARGA BARANG=====================')
def Menghitung_jumlah_harga():
    #Masukkan harga barang dan jumlah pembelian
    harga_barang = int(input('Masukkan Harga Barang: Rp. '))
    jumlah_pembelian = int(input('Masukkan Jumlah Pembelian: '))

    total_harga_barang = harga_barang * jumlah_pembelian #Menghitung total harga sebelum diskon dengan perkalian
    print(f'Total Harga Barang: {total_harga_barang}')
    #Jika total harga lebih dari Rp.250000 maka dapat diskon 25%
    if total_harga_barang >=250000:
        diskon_25 = 0.25 #25% diubah ke bilangan desimal
        harga_diskon = total_harga_barang * diskon_25
        harga_setelah_diskon = total_harga_barang - harga_diskon
        print('\nSelamat Anda Mendapatkan Potongan Diskon Sebesar 25%')
    else: 
        total_harga_barang <=250000
        harga_setelah_diskon = total_harga_barang #Ini tidak dapat diskon karena total harga kurang dari Rp.250000
        print('\nMaaf, Anda Tidak Mendapatkan Diskon Karena Tidak Mencapai Minimal Total Harga')
    
    print('------------------------------------------------------')
    #Menampilkan total harga yang harus dibayar setelah diskon
    print(f'Total harga yang harus dibayar: Rp. {harga_setelah_diskon}')
    tunai = int(input('\nMasukkan Tunai: Rp. ')) #Melakukkan pembayaran tunai
    kembalian = tunai - harga_setelah_diskon 
    print(f'Kembalian: Rp. {kembalian}')

    hemat = total_harga_barang - harga_setelah_diskon #potongan harga dari diskon sehingga pembeli hemat uang
    print(f'Anda Hemat: Rp. {hemat}') #Potongan diskon dari total harga (harga diskon)
    print('------------------------------------------------------')
#Perulangan
while True:
    Menghitung_jumlah_harga()
    Pilihan = str(input('Apakah ingin menghitung total harga lagi? (YA/TIDAK): '))
    if Pilihan == 'TIDAK':
        break #memberhentikan program
print(f'Terima kasih telah menggunakan program INDAH, {nama}.')
print('==============================SELESAI===============================')