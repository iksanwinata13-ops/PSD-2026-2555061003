class Node:
    def __init__(self, kode_buku, judul_buku):
        self.key = kode_buku
        self.value = judul_buku
        self.next = None


class HashMapPerpustakaan:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, kode_buku):
        return (kode_buku % self.SIZE + self.SIZE) % self.SIZE

    def tambah_buku(self, kode_buku, judul_buku):
        index = self.hash_function(kode_buku)
        current = self.table[index]

        while current is not None:
            if current.key == kode_buku:
                current.value = judul_buku
                return
            current = current.next

        buku_baru = Node(kode_buku, judul_buku)
        buku_baru.next = self.table[index]
        self.table[index] = buku_baru

    def cari_buku(self, kode_buku):
        index = self.hash_function(kode_buku)
        current = self.table[index]

        while current is not None:
            if current.key == kode_buku:
                return current
            current = current.next

        return None

    def hapus_buku(self, kode_buku):
        index = self.hash_function(kode_buku)
        current = self.table[index]
        prev = None

        while current is not None:
            if current.key == kode_buku:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return True

            prev = current
            current = current.next

        return False

    def tampilkan_buku(self):
        print("\nData Buku Perpustakaan:")
        for i in range(self.SIZE):
            print(f"Index {i}: ", end="")
            current = self.table[i]

            while current is not None:
                print(f"({current.key}, {current.value}) -> ", end="")
                current = current.next

            print("NULL")


def main():
    perpustakaan = HashMapPerpustakaan()

    perpustakaan.tambah_buku(101, "Algoritma dan Pemrograman")
    perpustakaan.tambah_buku(111, "Struktur Data")
    perpustakaan.tambah_buku(121, "Rekayasa Perangkat Lunak")
    perpustakaan.tambah_buku(102, "Pengenalan Pemrograman")
    perpustakaan.tambah_buku(112, "Matematika")


    perpustakaan.tampilkan_buku()

    kode_cari = int(input("\nMasukkan kode buku yang ingin dicari: "))

    hasil = perpustakaan.cari_buku(kode_cari)

    if hasil is not None:
        print(f"\nBuku ditemukan")
        print(f"Kode Buku: {hasil.key}")
        print(f"Judul Buku: {hasil.value}")
    else:
        print("\nBuku tidak ditemukan")


if __name__ == "__main__":
    main()