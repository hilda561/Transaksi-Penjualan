# PROGRAM TRANSAKSI SEDERHANA PENJUALAN PINANG DI PAPUA

import json
import os
from datetime import datetime as dt # from d import datetime

temp_list = [] # Variabel untuk menampung keseluruhan data pada file json, agar data tersimpan di sini
file_name = "mydata.json"   # Nama file json disimpan di variabel agar menjalankan program sampai akhir

def clear_screen(): # function clear screen
    os.system("cls")

def get_login():    # function login
    print("Halaman Login")
    username = input("Masukan username anda: ") # menginput username, username = admin
    password = input("Masukan password anda: ") # menginput password, password = adminpass
    if username == "admin" and password == "adminpass":
        print("login berhasil...\n\n")
    else:
        print("login gagal coba lagi...")
        get_login()

def baca_file(): #  function membaca file untuk ditampung sehingga dapat dipanggil saat menu
    with open(file_name,"r") as json_file: #    untuk dapat menampilkan data maka menggunakan mode 'r' yaitu read
        reader = json.load(json_file)
        print("{0:^80}".format("TRANSAKSI"))
        print("-"*80)
        print("Tanggal \t Pembeli \t Item \t Jumlah(kg) \t Harga /kg \t Total")
        print("-"*80)
        for isi in reader: # menggunakan for untuk mencetak setiap data dalam read berdasarkan barisnya
            print(f'{isi["Tanggal"]} \t {isi["Nama Pembeli"]} \t {isi["Nama Item"]} \t {isi["Jumlah Item(kg)"]} \t\t {isi["Harga /kg"]} \t\t {isi["Total Harga"]}')
        print("\n")
        
def input_file():   # function input, untuk menginputkan data
    tanggal = dt.today().strftime("%d-%m-%y")
    print("===================================")
    print("====== S T R U K   B E L I ========")
    print("===================================")
    nama_pembeli = input("Nama Pembeli: ")  # menginput nama pembelinya
    nama_barang = input("Nama Item   : ")   # menginput nama itemnya
    jumlah = int(input("Jumlah(kg)  : "))   # menginput jumalahnya satuan kg
    harga = int(input("Harga /kg   : Rp.")) # menginput harga /kg
    total = jumlah*harga
    print("Total Harga : Rp.{}".format(total))  # Menampilkan total harga
    bayar = int(input("Pembayaran  : Rp.")) # menginput uang pembayaran
    kurang = total - bayar
    kembalian = bayar - total
    if bayar > total:
        print("Kembalian   : Rp.{}".format(kembalian))    # Menampilkan kembalian dari transaksi
    elif bayar == total:
        print("Uang anda pas, terimakasih...")
    # jika uang pembeli kurang, maka akan menampilkan jumlah kekurangannya
    else:
        print("Kekurangan  : Rp.{}".format(kurang))
        print("Maaf uang anda kurang...")
    print("===================================")
    print("===================================\n")

    item_baru = dict()
    item_baru["Nama Pembeli"] = nama_pembeli
    item_baru["Tanggal"] = tanggal
    item_baru["Nama Item"] = nama_barang 
    item_baru["Jumlah Item(kg)"] = jumlah
    item_baru["Harga /kg"] = harga
    item_baru["Total Harga"] = total
    temp_list.append(item_baru) 
    with open (file_name,"w") as json_file: # untuk dapat menulis dapat menambahkan gunakan mode 'w' yaitu write
        json.dump(temp_list, json_file, indent=4)   # data di python, dimasukkan ke json

def hapus_item(): # function hapus
    temp_list = list()
    hapus = input("Nama pembeli yang ingin dihapus: ")
    with open (file_name,"r") as json_file: # untuk dapat menampilkan data maka menggunakan mode 'r' yaitu read
        reader = json.load(json_file)
        for data in reader: # menggunakan for untuk mencetak setiap data dalam read berdasarkan barisnya
            if data["Nama Pembeli"] == hapus:
                continue
            else:
                temp_list.append(data)
    with open(file_name, "w") as json_file: # untuk dapat menulis dapat menambahkan gunakan mode 'w' yaitu write
        json.dump(temp_list, json_file, indent=4)   # data di python, dimasukkan ke json

def menu(): # function menu
    print("{0:^80}".format("WELCOME"))
    print("{0:^80}".format("TRANSAKSI PENJUALAN BUAH PINANG KHAS PAPUA"))
    print("\n")
    print("{0:^80}".format("ITEM YANG DIJUAL"))
    print("-"*80)
    print("> Pinang\n> Buah Sirih\n")   # menampilkan item yang dijual
    print("================================= DAFTAR MENU =================================")
    print("[1] Tambah Data\n[2] Hapus Data\n[3] Baca Data\n[4] Keluar")  # menampilkan menu-menu program
    print("="*80)
    pilihan = int(input("PILIH MENU > "))   # untuk menginput pilihan 1,2,3,atau 4
    print("\n")
    if pilihan == 1:
        input_file()    # memanggil function input
    elif pilihan == 2:
        hapus_item()    # memanggil function hapus
        print("Berhasil dihapus!\n")
    elif pilihan == 3:
        baca_file() # memanggil function baca
    elif pilihan == 4:
        print("Program Exit")
        print("="*80)
        exit()
    else:
        print("Inputan anda salah!\n")
# Tampilan Awal
clear_screen()  # memanggil function Clear Screen
print("="*80)
get_login()
print("\n")
menu()   # memanggil function menu agar dapat ditampilkan

while True:
    ulang = input("Apakah ingin melakukan transaksi kembali? [y]/[n] ") # menginput yes(y) atau no(n)
    if ulang == "y":
        print("\n")
        clear_screen()  # memanggil function clear screen
        menu()  # memanggil function menu agar dapat ditampilkan
    elif ulang == "n":
        break
    else:
        print("Inputan anda salah!")