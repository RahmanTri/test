# Algoritma
# inisialisasi variabel berupa daftar list untuk setiap toping, crust dan size
toping = ["Frankfurter BBQ", "Meat Monsta", "Super Supreme", "Super Supreme Chiken"]
crust = ["Pan", "Stuffed Crust Sausage", "Stuffed Crust Cheese", "Cheesy Bites", "Crown Crust"]
size = ["Personal", "Regular", "Large"]

# Akan menampilkan tampilan awal dan konfirmasi pesanan
print('''
=======================================================
            SELAMAT DATANG DI LAYANAN KAMI
        ======================================
        PEMESANAN PIZZA BY : KELOMPOK 12 MI23F  
=======================================================
Apakah Anda ingin memesan pizza? (y/n)
''')
konfirmasi = input('(y/n) : ').lower()

# jika buyyer mengonfirmasi 'y', maka program akan melanjutkan 
if konfirmasi == "y":

# Akan menaampilkan daftar menu toping    
    print("""
==============================================
      Berikut merupakan daftar menu kami :
==============================================
          """)
    for i, daftar_menu in enumerate(toping):
        print (i+1, daftar_menu)
    pilihan_toping = int(input('Masukkan Pilihan anda (1-4) : '))
