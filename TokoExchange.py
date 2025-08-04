items1 = {"nama": "BITCOIN", "stock": 10, "harga": 119}
items2 = {"nama": "ETHEREUM", "stock": 20, "harga": 36}
items3 = {"nama": "SOLANA", "stock": 10, "harga": 125}
items4 = {"nama": "Dodgecoin", "stock": 10, "harga": 123}
items5 = {"nama": "Memecoin", "stock": 10, "harga": 132}

items = [items1, items2, items3, items4, items5]

def display_items():
    print("No\tCoin\tStock\tHarga")
    for i in range(len(items)):
        print(i + 1, "\t", items[i]["nama"], "\t", items[i]["stock"], "\t", items[i]["harga"])

def tambah():
    nama = str(input("Masukkan Nama Coin Yang DiTambahkan: "))
    stock = int(input("Masukkan Stock Coin: "))  
    harga = int(input("Masukkan Harga coin: "))
    items.append({"nama": nama, "stock": stock, "harga": harga}) 
    print("Coin berhasil ditambahkan!")
    display_items() 

def menu():
    while True:
        print("\nMenu")
        print("1. Tampilkan semua coin")
        print("2. Tambah coin")
        print("3. Keluar")
        Pilih = input("Pilih menu (1/2/3): ")
        
        if Pilih == '1':
            display_items()
        elif Pilih == '2':
            tambah()
        elif Pilih == '3':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
menu()
