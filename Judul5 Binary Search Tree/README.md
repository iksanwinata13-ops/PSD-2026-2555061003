Tugas Akhir Percobaan 5

Judul Program : Sistem Pengelolaan Data Mahasiswa

Program ini berfungsi sebagai sistem pengelolaan data mahasiswa yang dirancang untuk memudahkan pengguna dalam menyimpan, mencari, dan menampilkan data mahasiswa berdasarkan NPM. Program menyediakan fitur utama berupa penambahan data mahasiswa, pencarian data mahasiswa, penampilan data mahasiswa secara terurut, serta perhitungan jumlah mahasiswa yang tersimpan pada sistem. Dengan adanya fitur-fitur tersebut, proses pengelolaan data menjadi lebih terstruktur dan efisien.

<img width="1508" height="4130" alt="llllo" src="https://github.com/user-attachments/assets/bf9faa43-60b6-485f-aa7c-f59f0e5b1cf9" />

Penjelasan Kode :

Berikut lanjutan **nomor 1–101 lengkap**, dengan nomor yang barisnya kosong tetap ditampilkan tanpa keterangan.

1. Mendefinisikan class `Node` yang digunakan untuk merepresentasikan setiap node pada Binary Search Tree.
2.Mendefinisikan constructor `__init__` untuk class Node.
**3.** Menyimpan data yang dimasukkan ke dalam atribut `key`.
**4.** Menginisialisasi child kiri dengan nilai `None`.
**5.** Menginisialisasi child kanan dengan nilai `None`.
**6.**
**7.**
**8.** Mendefinisikan class `BSTDasar`.
**9.** Mendefinisikan constructor untuk class BSTDasar.
**10.** Menginisialisasi root BST dengan nilai `None`.
**11.**
**12.** Mendefinisikan fungsi `insert_node()` untuk menambahkan node baru.
**13.** Memeriksa apakah root kosong.
**14.** Membuat node baru jika root kosong.
**15.** Memeriksa apakah nilai lebih kecil dari root.
**16.** Menyisipkan data ke subtree kiri secara rekursif.
**17.** Memeriksa apakah nilai lebih besar dari root.
**18.** Menyisipkan data ke subtree kanan secara rekursif.
**19.** Mengembalikan root.
**20.**
**21.** Mendefinisikan fungsi `insert()`.
**22.** Memanggil fungsi `insert_node()` untuk menambahkan data ke BST.
**23.**
**24.** Mendefinisikan fungsi `search_node()`.
**25.** Memeriksa apakah node kosong.
**26.** Mengembalikan nilai False jika data tidak ditemukan.
**27.** Memeriksa apakah nilai node sama dengan data yang dicari.
**28.** Mengembalikan nilai True jika data ditemukan.
**29.** Memeriksa apakah nilai yang dicari lebih kecil dari root.
**30.** Melakukan pencarian pada subtree kiri.
**31.** Melakukan pencarian pada subtree kanan.
**32.**
**33.** Mendefinisikan fungsi `search()`.
**34.** Memanggil fungsi `search_node()`.
**35.**
**36.** Mendefinisikan fungsi traversal inorder.
**37.** Memeriksa apakah node kosong.
**38.** Menghentikan proses jika node kosong.
**39.** Menelusuri subtree kiri.
**40.** Menampilkan nilai node.
**41.** Menelusuri subtree kanan.
**42.**
**43.** Mendefinisikan fungsi `count_nodes()`.
**44.** Memeriksa apakah node kosong.
**45.** Mengembalikan nilai 0 jika node kosong.
**46.** Menghitung jumlah node secara rekursif.
**47.**
**48.**
**49.** Mendefinisikan fungsi `main()`.
**50.** Membuat objek BST dari class `BSTDasar`.
**51.** Menginisialisasi variabel `pilih` dengan nilai 0.
**52.**
**53.** Memulai perulangan selama pengguna belum memilih menu keluar.
**54.** Menampilkan judul program.
**55.** Menampilkan menu tambah data mahasiswa.
**56.** Menampilkan menu cari data mahasiswa.
**57.** Menampilkan menu tampilkan data mahasiswa.
**58.** Menampilkan menu hitung jumlah mahasiswa.
**59.** Menampilkan menu keluar.
**60.**
**61.** Memulai blok `try`.
**62.** Meminta pengguna memasukkan pilihan menu.
**63.** Menangkap error jika input bukan angka.
**64.** Menampilkan pesan input tidak valid.
**65.** Mengulangi perulangan ke menu utama.
**66.**
**67.** Memeriksa apakah pengguna memilih menu 1.
**68.** Memulai blok `try`.
**69.** Meminta pengguna memasukkan NPM mahasiswa.
**70.** Menambahkan NPM ke dalam BST.
**71.** Menampilkan pesan bahwa data berhasil ditambahkan.
**72.** Menangkap error jika input tidak valid.
**73.** Menampilkan pesan input tidak valid.
**74.**
**75.** Memeriksa apakah pengguna memilih menu 2.
**76.** Memulai blok `try`.
**77.** Meminta pengguna memasukkan NPM yang dicari.
**78.** Memeriksa apakah data ditemukan di BST.
**79.** Menampilkan pesan data mahasiswa ditemukan.
**80.** Jika data tidak ditemukan.
**81.** Menampilkan pesan data mahasiswa tidak ditemukan.
**82.** Menangkap error jika input tidak valid.
**83.** Menampilkan pesan input tidak valid.
**84.**
**85.** Memeriksa apakah pengguna memilih menu 3.
**86.** Menampilkan judul daftar NPM mahasiswa.
**87.** Menjalankan traversal inorder untuk menampilkan data secara terurut.
**88.** Pindah ke baris baru setelah data ditampilkan.
**89.**
**90.** Memeriksa apakah pengguna memilih menu 4.
**91.** Menampilkan jumlah mahasiswa yang tersimpan dalam BST.
**92.**
**93.** Memeriksa apakah pengguna memilih menu 5.
**94.** Menampilkan pesan program selesai.
**95.**
**96.** Jika pilihan menu tidak tersedia.
**97.** Menampilkan pesan pilihan tidak valid.
**98.**
**99.**
**100.** Memastikan fungsi `main()` hanya dijalankan saat file dieksekusi langsung.
**101.** Memanggil fungsi `main()` untuk menjalankan program.
