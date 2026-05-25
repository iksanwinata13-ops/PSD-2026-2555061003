class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BSTDasar:
    def __init__(self):
        self.root = None

    def insert_node(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert_node(root.left, key)
        elif key > root.key:
            root.right = self.insert_node(root.right, key)
        return root

    def insert(self, key):
        self.root = self.insert_node(self.root, key)

    def search_node(self, root, key):
        if root is None:
            return False
        if root.key == key:
            return True
        if key < root.key:
            return self.search_node(root.left, key)
        return self.search_node(root.right, key)

    def search(self, key):
        return self.search_node(self.root, key)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.key, end=" ")
        self.inorder(root.right)

    def count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)


def main():
    bst = BSTDasar()
    pilih = 0

    while pilih != 5:
        print("\n=== Sistem Pengelolaan Data Mahasiswa ===")
        print("1. Tambah Data Mahasiswa")
        print("2. Cari Data Mahasiswa")
        print("3. Tampilkan Data Mahasiswa")
        print("4. Hitung Jumlah Mahasiswa")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            try:
                x = int(input("Masukkan NPM Mahasiswa: "))
                bst.insert(x)
                print(f"NIM {x} berhasil ditambahkan")
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 2:
            try:
                x = int(input("Masukkan NPM yang dicari: "))
                if bst.search(x):
                    print("Data mahasiswa ditemukan")
                else:
                    print("Data mahasiswa tidak ditemukan")
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 3:
            print("Daftar NPM Mahasiswa: ", end="")
            bst.inorder(bst.root)
            print()

        elif pilih == 4:
            print(f"Jumlah Mahasiswa: {bst.count_nodes(bst.root)}")

        elif pilih == 5:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()