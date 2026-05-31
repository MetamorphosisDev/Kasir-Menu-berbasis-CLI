import time

list_menuMakanMinum = [["Bakso Malang",12000], ["Mie Bakso",15000], ["Bakso Jumbo",25000], 
                       ["Mie Ayam", 10000], ["Mie Ayam Bakso", 15000], ["Mie Ayam Bakso Jumbo", 30000], 
                       ["Ayam Bakar Madu", 20000], ["Ayam Bakar padang", 18000], ["Ayam goreng", 15000],
                       ["Ayam betutu", 20000], ["Nasi Goreng", 15000], ["Nasi Goreng spesial", 20000], 
                       ["Nasi Biasa", 5000], ["kerupuk pangsit", 7000], ["kerupuk Udang", 1500], 
                       ["Teh Manis(Dingin/Hangat)", 5000], ["Air Putih", 3000], ["Jeruk(Dingin/Hangat)", 5000], 
                       ]
pesanan = []
riwayatPesanan = []
total = 0
diskon = 0

nama_Pelanggan = ""
No_Telp_Pelanggan = ""

def TampilanmenuKasir():
    print("\n")
    print("==================================")
    print("             MENU KASIR")
    print("==================================")
    print("1. Lihat Menu Makanan Minuman")
    print("2. Pesanan")
    print("3. Cetak Struk")
    print("4. Clear Data")
    print("5. Riwayat Pemesanan")
    print("0. Keluar")
    print("==================================")
    

def tampilanPesanan():
    print("\n")
    print("==================================")
    print("             PESANAN")
    print("==================================")
    print("1. Tambah Pesanan")
    print("2. Hapus Pesanan")
    print("3. List Pesanan")
    print("0. Keluar dari halaman ini")
    print("==================================")

def menu_Makanan_Minuman():
    No_number_first = 1
    print("="*45)
    print("|          Menu Makanan dan Minuman        |")
    print("="*45)
    for makanminum, harga in list_menuMakanMinum:
        print(f"|  {str(No_number_first):2}.{makanminum:<25} Rp{harga:<6}  |")
        No_number_first += 1
    print("="*45)

def tambahPesanan():
    global nama_Pelanggan, No_Telp_Pelanggan
    nama_Pelanggan = input("Masukan Nama Pelanggan  : ")
    No_Telp_Pelanggan = input("Masukan Nomor Telepon   : ")
    if (nama_Pelanggan == "" or No_Telp_Pelanggan == ""):
        print("Nama atau Nomor tidak boleh kosong!")
    else:
        while True:
            global total
            No_number_second = 1
            pilihmenu = int(input("Pilih Menu(1-18 | 0 - Stop): "))
            if pilihmenu == 0:
                break
            elif pilihmenu > 19 or pilihmenu < 0:
                print("Masukan Nilai yang benar")
            else:
                jumlah = int(input("Masukan Jumlah: "))
                nama_Menu, harga = list_menuMakanMinum[pilihmenu-1]
                subtotal = harga * jumlah
                pesanan.append([nama_Menu, harga, jumlah, subtotal])
                print("="*65                                        )
                print("|                          Pesanan Anda                         |")
                print("="*65)
                print(f" Nama: {nama_Pelanggan},  No.Telp: {No_Telp_Pelanggan}")
                print("="*65)
                for nama, harga, jumlah, subtotal in pesanan:
                    print(f"|  {No_number_second:2}.{nama:<25} {jumlah:>3} x Rp{harga:<8} | Rp{subtotal}")
                    No_number_second+=1
                    total += subtotal
                print("="*65)

def hapusPesan():
    while True:
        tampilanPesanan()
        if (pesanan == []):
            print("Pesanan Kosong")
        else :
            tampilkanPesan()
            inputHapusPesanan = int(input(f"Masukan Nomor (0-Stop | 1-{len(pesanan)}): "))
            if inputHapusPesanan == 0:
                break
            elif (inputHapusPesanan < -1 or inputHapusPesanan > len(pesanan)):
                print("Nomor tidak Valid")
                time.sleep(1.5)
            else :
                item_hapus = pesanan.pop(inputHapusPesanan-1)
                print(f"{item_hapus[0]} Berhasil Dihapus")


def tampilkanPesan():
    if (pesanan == []):
        print("Pesanan Tidak Ada")
    else: 
            No_number_third = 1
            print("="*65                                        )
            print("|                          Pesanan Anda                         |")
            print("="*65)
            print(f" Nama: {nama_Pelanggan},  No.Telp: {No_Telp_Pelanggan}")
            print("="*65)
            for nama, harga, jumlah, _ in pesanan:
                print(f"|  {No_number_third:2}.{nama:<25} {jumlah:>3} x Rp{harga:<8}")
                No_number_third+=1
            print("="*65)
        

def cetakStruk(): 
    global diskon
    print("Starting: Struk...")
    time.sleep(2)
    print("Process: Make Struk...")
    if pesanan == []:
        print("Process: Struk Gagal - Pesanan tidak ada")
        time.sleep(2)
    else: 
        if (total >= 1000000):
            diskon = 100000
            noteHarga = "Rp1.000.000"
        elif (total >= 500000):
            diskon = 50000
            noteHarga = "Rp500.000"
        time.sleep(2)
        print("Succes: Struk")
        time.sleep(2)
        print("")
        number_struk = 1
        print("=" * 65)
        print("                         STRUK PEMBELIAN")
        print("=" * 65)
        print(f" Nama: {nama_Pelanggan},  No.Telp: {No_Telp_Pelanggan}")
        print("=" * 65)
        for nama, harga, jumlah, subtotal in pesanan:
            print(f"{number_struk:<4}{nama:<25}{jumlah:<6}{harga:<12}Rp{subtotal}")
            number_struk+=1

        print("-" * 65)
        if (diskon == 0):
            print(f"Total Pembayaran: R{total-diskon}")
        else:
            print(f"{"Diskon pembelian sebesar:":<38}{noteHarga}")
            print(f"{'Total + Diskon':<38}:Rp{total}, Diskon: {diskon} ")
            print(f"{"Total Pembayaran:":<38} Rp{total-diskon}")
        print("=" * 65)


def clearData():
    global diskon, total
    global nama_Pelanggan, No_Telp_Pelanggan
    print("Starting: Clear Data...")
    time.sleep(1)
    print("Process: Clear Data...")
    time.sleep(2.5)
    if pesanan == []:
        print("Process: Tidak ada Data")
        time.sleep(2)
    else: 
        time.sleep(2)
        riwayatPesanan.append({"namaPelanggan":nama_Pelanggan,"Telp":No_Telp_Pelanggan, "Pesanan":pesanan.copy()})
        pesanan.clear()

        total = 0
        diskon = 0
        nama_Pelanggan = ""
        No_Telp_Pelanggan = ""
        print("Succes: Clear Data")


def riwayatPesanan_data():
    print(riwayatPesanan)

def main():
    while True:
            TampilanmenuKasir()
            pilihMenuKasir = int(input("Masukan Inputan : "))
            if (pilihMenuKasir == 1):
                menu_Makanan_Minuman()
            elif (pilihMenuKasir == 2): 
                tampilanPesanan()
                inputpesan = int(input("Masukan Inputan: "))
                if (inputpesan == 1):
                    tambahPesanan()
                elif (inputpesan == 2):
                    hapusPesan()
                elif (inputpesan == 3):
                    tampilkanPesan()
                else:
                    print("Masukan nilai yang benar")
            elif (pilihMenuKasir == 3):
                cetakStruk()
            elif (pilihMenuKasir == 4):
                clearData()
            elif (pilihMenuKasir == 5):
                riwayatPesanan_data()
            elif (pilihMenuKasir == 0):
                break
            elif (pilihMenuKasir == 100):
                print(type(riwayatPesanan))
                print(type(pesanan))
            else: 
                print("Daftar tidak ada")
main()
