import time
import datetime
from Data.Data_makan_minum import list_menuMakanMinum

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
    print("3. Edit Pesanan")
    print("4. List Pesanan")
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

def editPesanan():
    if pesanan == []:
        print("Pesanan Tidak Ada")
        return
    tampilkanPesan()
    index = int(input(f"Pilih nomor pesanan yang ingin diedit (1-{len(pesanan)}): "))
    if index < 1 or index > len(pesanan):
        print("Nomor tidak valid")
        return
    
    menu_Makanan_Minuman()
    pilih_menu = int(input("Pilih menu baru: "))
    if pilih_menu < 1 or pilih_menu > len(list_menuMakanMinum):
        print("Menu tidak valid")
        return

    jumlah_baru = int(input("Masukkan jumlah baru: "))
    nama_baru, harga_baru = list_menuMakanMinum[pilih_menu - 1]
    subtotal_baru = harga_baru * jumlah_baru
    pesanan[index - 1] = [
        nama_baru,
        harga_baru,
        jumlah_baru,
        subtotal_baru
    ]
    print(f"Pesanan berhasil diubah menjadi {nama_baru} x{jumlah_baru}")

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
        riwayatPesanan.append({
        "waktu": datetime.datetime.now(),
        "nama": nama_Pelanggan,
        "telp": No_Telp_Pelanggan,
        "items": pesanan.copy(),
        "total": total,
        "diskon": diskon,
        "bayar": total - diskon
    })
        pesanan.clear()

        total = 0
        diskon = 0
        nama_Pelanggan = ""
        No_Telp_Pelanggan = ""
        print("Succes: Clear Data")


def riwayatPesanan_data():
    if not riwayatPesanan:
        print("Belum ada riwayat transaksi.")
        return
    print("\n" + "="*70)
    print("                RIWAYAT PEMESANAN")
    print("="*70)
    no_transaksi = 1
    for trx in riwayatPesanan:
        print(f"\nTransaksi #{no_transaksi}")
        no_transaksi += 1

        print(f"Waktu : {trx['waktu']}")
        print(f"Nama  : {trx['nama']}")
        print(f"Telp  : {trx['telp']}")
        print("-"*70)

        no_item = 1
        for item in trx["items"]:
            nama, harga, qty, subtotal = item
            print(f"{no_item}. {nama} {qty} x Rp{harga} = Rp{subtotal}")
            no_item += 1

        print("-"*70)
        print(f"Total  : Rp{trx['total']}")
        print(f"Diskon : Rp{trx['diskon']}")
        print(f"Bayar  : Rp{trx['bayar']}")
        print("="*70)

def main():
    while True:
            TampilanmenuKasir()
            pilihMenuKasir = int(input("Masukan Inputan : "))
            if (pilihMenuKasir == 1):
                menu_Makanan_Minuman()
            elif (pilihMenuKasir == 2):
                while True:
                    tampilanPesanan()
                    inputpesan = int(input("Masukan Inputan: "))
                    if inputpesan == 1:
                        tambahPesanan()
                    elif inputpesan == 2:
                        hapusPesan()
                    elif inputpesan == 3:
                        editPesanan()
                    elif inputpesan == 4:
                        tampilkanPesan()
                    elif inputpesan == 0:
                        break
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
