#Nama  : Iksan Surya Winata
#NPM   : 25550661003
#Kelas : PSD-E


def menu():
    print("\n===== WARKOP RUSIA =====")
    print("1.Tampilkan Menu")
    print("2.Pesan Makanan / Minuman")
    print("3.Lihat Pesanan")
    print("4.Hitung Total")
    print("5.Keluar")


def main():
    
    menu_restoran = [
        ["Nasi Goreng", 15000],
        ["Mie Ayam", 12000],
        ["Bakso", 13000],
        ["Es Teh", 5000],
        ["Jus Jeruk", 8000],
        ["Kopi Hitam", 7000]
    ]

    pesanan = []

    while True:
        menu()
        choice = input("Pilih menu: ")

     
        if choice == "1":
            print("\n===== DAFTAR MENU =====")
            for i in range(len(menu_restoran)):
                print(i + 1, ".", menu_restoran[i][0], "- Rp", menu_restoran[i][1])


        elif choice == "2":
            print("\n===== PILIH MENU =====")
            for i in range(len(menu_restoran)):
                print(i + 1, ".", menu_restoran[i][0], "- Rp", menu_restoran[i][1])

            data = input("Masukkan nomor menu (pisahkan koma, contoh 1,3,5): ")
            pilihan = data.split(",")

            for item in pilihan:
                try :
                    nomor = int(item)
                    if 1 <= nomor <= len(menu_restoran):
                        pesanan.append(menu_restoran[nomor - 1])
                        print(menu_restoran[nomor - 1][0], "berhasil ditambahkan ke pesanan")
                    else:
                        print("Menu tidak ada, silahkan pilih kembali")

                except ValueError:
                    print("Menu tidak ada, silahkan pilih kembali")
                    

        elif choice == "3":
            print("\n===== PESANAN =====")

            if len(pesanan) == 0:
                print("Anda belum memesan, silahkan pesan makanan / minuman terlebih dahulu")
            else:
                for i in range(len(pesanan)):
                    print(i + 1, ".", pesanan[i][0], "- Rp", pesanan[i][1])


        elif choice == "4":
            total = 0

            for i in range(len(pesanan)):
                total += pesanan[i][1]

            print("\nTotal Bayar = Rp", total)


        elif choice == "5":
            print("Terima kasih telah berkunjung ke WARKOP RUSIA")
            break

        else:
            print("Pilihan tidak tersedia, silahkan pilih kembali")


if __name__ == "__main__":
    main()