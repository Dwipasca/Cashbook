import csv

name_file = "dummy.csv"


def hitungSaldo (list):
    balance = 0
    for idx, ts in enumerate(list, start=1) :
        print(f"{idx}. {ts["date"]} | {ts["ket"]} | {ts["amount"]} ({ts["type"]})")
        
        if ts["type"] == "pemasukan" :
            balance = balance + ts["amount"]
        elif ts["type"] == "pengeluaran" :
            balance = balance - ts["amount"]
    return balance

def tampilkanTransaksi():
    print("[Daftar Transaksi]")
    print("-------------------------------------------")  
    
    with open(name_file, mode="r", encoding="utf-8") as file :
        read_csv = csv.DictReader(file)
        
        for baris in read_csv :
            print(f"{baris["tanggal"]:<10} | {baris["keterangan"]:<20} | {baris["jumlah"]:<10} | {baris["jenis"]}")
    print("-------------------------------------------")  


while True:
    print("=== MENU UTAMA ===")
    print("1. Tambah")
    print("2. Lihat")
    print("3. Keluar")

    menuSelection = input("Pilih menu (1/2/3): ")

    if menuSelection == "1":
        print("\n---> Anda memilih menu Tambah\n")

        print("[Input Transaksi Baru]\n")
        
        newTransaction = {}
        print("Jenis transaksi: ")
        print("1. Pemasukkan")
        print("2. Pengeluaran")
        
        typeSelection = input("Pilih jenis transaksi (1/2): ")
        if typeSelection == "1":
            print("Jenis: pemasukan")
            newTransaction["type"] = "pemasukan"
        elif typeSelection == "2":
            print("Jenis: pengeluaran")
            newTransaction["type"] = "pengeluaran"

        newTransaction["date"] = input("Tanggal: ")
        newTransaction["ket"] = input("Keterangan: ")
        
        newTransaction["amount"] = int(input("Jumlah: "))  
        transactions.append(newTransaction)
        print("\nData telah disimpan di memori\n")

    elif menuSelection == "2":
        print("\n---> Anda memilih menu Lihat\n")
        tampilkanTransaksi()

    elif menuSelection == "3":
        print("\nProgram Selesai\n")
        break

    else :
        print("\nYang anda pilih tidak ada di menu\n")
