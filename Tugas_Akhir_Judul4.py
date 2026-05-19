class QueueArray:
    def __init__(self, max_size=100):
        self.MAXN = max_size
        self.q = [None] * self.MAXN
        self.front_idx = -1
        self.rear_idx = -1

    def is_empty(self):
        return self.front_idx == -1

    def is_full(self):
        return (self.rear_idx + 1) % self.MAXN == self.front_idx

    def is_exist(self, x):
        if self.is_empty():
            return False

        i = self.front_idx
        while True:
            if self.q[i] == x:
                return True

            if i == self.rear_idx:
                break

            i = (i + 1) % self.MAXN

        return False

    def enqueue(self, x):
        if self.is_full():
            print("Antrian kasir sudah penuh")
            return

        if self.is_exist(x):
            print(f"Nomor pelanggan {x} sudah ada dalam antrian")
            return

        if self.is_empty():
            self.front_idx = 0
            self.rear_idx = 0
        else:
            self.rear_idx = (self.rear_idx + 1) % self.MAXN

        self.q[self.rear_idx] = x
        print(f"Pelanggan nomor {x} berhasil masuk antrian")

    def dequeue(self):
        if self.is_empty():
            print("Tidak ada pelanggan dalam antrian")
            return

        print(f"Pelanggan nomor {self.q[self.front_idx]} selesai dilayani")

        if self.front_idx == self.rear_idx:
            self.front_idx = -1
            self.rear_idx = -1
        else:
            self.front_idx = (self.front_idx + 1) % self.MAXN

    def clear_queue(self):
        self.front_idx = -1
        self.rear_idx = -1
        print("Semua antrian berhasil dihapus")

    def display(self):
        if self.is_empty():
            print("Antrian kasir kosong")
            return

        print("Daftar antrian kasir: ", end="")

        i = self.front_idx
        while True:
            print(self.q[i], end=" ")

            if i == self.rear_idx:
                break

            i = (i + 1) % self.MAXN

        print()

def main():
    queue = QueueArray()
    pilih = 0

    while pilih != 5:
        print("\n=== SISTEM ANTRIAN KASIR MINIMARKET ===")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Tampilkan Semua Antrian")
        print("4. Hapus Semua Antrian")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            try:
                val = int(input("Masukkan nomor pelanggan: "))
                queue.enqueue(val)
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 2:
            queue.dequeue()

        elif pilih == 3:
            queue.display()

        elif pilih == 4:
            queue.clear_queue()

        elif pilih == 5:
            print("Program selesai.")

        else:
            print("Menu tidak tersedia!")

if __name__ == "__main__":
    main()