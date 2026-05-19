Tugas Akhir Percobaan 4

Judul Program : Sistem Antrian Kasir Minimarket

Program ini berfungsi sebagai sistem manajemen antrian kasir yang dirancang untuk memudahkan pengelolaan antrean pelanggan di minimarket secara terstruktur dan efisien. Dengan menyediakan fitur utama seperti penambahan pelanggan ke antrian, pelayanan pelanggan secara berurutan, tampilan daftar antrian aktif, serta penghapusan seluruh antrian sekaligus, program ini membantu meningkatkan efisiensi operasional kasir dalam melayani pelanggan secara adil dan tertib.

<img width="1478" height="5042" alt="99999999" src="https://github.com/user-attachments/assets/0dacf746-86e7-4ad1-a58f-cbf95712970e" />

Penjelasan kode : 

1. Mendefinisikan class bernama QueueArray sebagai struktur data antrian berbasis array sirkular.
2. Mendefinisikan method konstruktor dengan parameter max_size (default 100) untuk inisialisasi antrian.
3. Menyimpan nilai max_size ke atribut self.MAXN sebagai kapasitas maksimal antrian.
4. Membuat list self.q berisi None sebanyak self.MAXN sebagai wadah penyimpanan elemen antrian.
5. Menginisialisasi self.front_idx dengan nilai -1 sebagai penanda posisi depan antrian (kosong).
6. Menginisialisasi self.rear_idx dengan nilai -1 sebagai penanda posisi belakang antrian (kosong).
7.
8. Mendefinisikan method is_empty untuk mengecek apakah antrian dalam keadaan kosong.
9. Mengembalikan nilai True jika front_idx bernilai -1, yang berarti antrian kosong.
10.
11. Mendefinisikan method is_full untuk mengecek apakah antrian sudah penuh.
12. Mengembalikan True jika posisi setelah rear_idx (secara sirkular) sama dengan front_idx, artinya antrian penuh.
13.
14. Mendefinisikan method is_exist untuk mengecek apakah nilai x sudah ada di dalam antrian.
15. Mengecek apakah antrian kosong; jika iya, langsung kembalikan False.
16. Mengembalikan nilai False karena antrian kosong, sehingga elemen tidak mungkin ada.
17.
18. Menyimpan posisi front_idx ke variabel i sebagai titik awal penelusuran.
19. Memulai perulangan tanpa henti untuk menelusuri semua elemen antrian.
20. Mengecek apakah elemen pada posisi i sama dengan nilai x yang dicari.
21. Mengembalikan True jika nilai x ditemukan di antrian.
22.
23. Mengecek apakah indeks i sudah mencapai posisi rear_idx (elemen terakhir).
24. Menghentikan perulangan karena seluruh antrian sudah ditelusuri.
25.
26. Memindahkan indeks i ke posisi berikutnya secara sirkular menggunakan operasi modulo.
27.
28. Mengembalikan False karena nilai x tidak ditemukan setelah seluruh antrian ditelusuri.
29.
30. Mendefinisikan method enqueue untuk menambahkan elemen x ke belakang antrian.
31. Mengecek apakah antrian sudah penuh sebelum menambahkan elemen baru.
32. Mencetak pesan peringatan bahwa antrian kasir sudah penuh jika kondisi terpenuhi.
33. Menghentikan eksekusi method enqueue jika antrian penuh.
34.
35. Mengecek apakah elemen x sudah ada di dalam antrian menggunakan method is_exist.
36. Mencetak pesan peringatan bahwa nomor pelanggan tersebut sudah berada di antrian.
37. Menghentikan eksekusi method jika elemen sudah ada (mencegah duplikasi).
38.
39. Mengecek apakah antrian sedang kosong untuk menentukan cara menambahkan elemen pertama.
40. Mengatur front_idx ke posisi 0 sebagai posisi awal antrian saat elemen pertama dimasukkan.
41. Mengatur rear_idx ke posisi 0 sebagai posisi belakang antrian saat elemen pertama dimasukkan.
42. Jika antrian tidak kosong, jalankan blok else untuk penambahan elemen selanjutnya.
43. Memindahkan rear_idx ke posisi berikutnya secara sirkular menggunakan operasi modulo.
44.
45. Menyimpan nilai x ke dalam array self.q pada posisi rear_idx yang baru.
46. Mencetak konfirmasi bahwa pelanggan dengan nomor x berhasil masuk ke antrian.
47.
48. Mendefinisikan method dequeue untuk menghapus dan melayani elemen paling depan antrian.
49. Mengecek apakah antrian kosong sebelum mencoba melakukan dequeue.
50. Mencetak pesan bahwa tidak ada pelanggan dalam antrian jika antrian kosong.
51. Menghentikan eksekusi method jika antrian kosong.
52.
53. Mencetak nomor pelanggan yang sedang dilayani, yaitu elemen pada posisi front_idx.
54.
55. Mengecek apakah elemen yang dilayani adalah satu-satunya elemen (front sama dengan rear).
56. Mengatur kembali front_idx ke -1 menandakan antrian menjadi kosong setelah dequeue.
57. Mengatur kembali rear_idx ke -1 menandakan antrian menjadi kosong setelah dequeue.
58. Jika masih ada elemen lain, jalankan blok else.
59. Memindahkan front_idx ke posisi berikutnya secara sirkular menggunakan operasi modulo.
60.
61. Mendefinisikan method clear_queue untuk mengosongkan seluruh antrian sekaligus.
62. Mengatur front_idx kembali ke -1 sebagai tanda antrian dikosongkan.
63. Mengatur rear_idx kembali ke -1 sebagai tanda antrian dikosongkan.
64. Mencetak konfirmasi bahwa semua antrian berhasil dihapus.
65.
66. Mendefinisikan method display untuk menampilkan semua elemen antrian saat ini ke layar.
67. Mengecek apakah antrian kosong sebelum menampilkan isi antrian.
68. Mencetak pesan bahwa antrian kasir sedang kosong jika tidak ada elemen.
69. Menghentikan eksekusi method jika antrian kosong.
70.
71. Mencetak label "Daftar antrian kasir: " tanpa baris baru agar elemen tercetak sejajar.
72.
73. Menyimpan posisi front_idx ke variabel i sebagai titik awal penelusuran tampilan.
74. Memulai perulangan tanpa henti untuk mencetak semua elemen antrian satu per satu.
75. Mencetak elemen pada posisi i diikuti spasi tanpa pindah baris ke layar.
76.
77. Mengecek apakah indeks i sudah mencapai posisi rear_idx (elemen terakhir).
78. Menghentikan perulangan karena semua elemen antrian sudah ditampilkan.
79.
80. Memindahkan indeks i ke posisi berikutnya secara sirkular menggunakan operasi modulo.
81.
82. Mencetak baris baru setelah semua elemen antrian selesai ditampilkan.
83.
84. Mendefinisikan fungsi utama main() sebagai tempat seluruh logika program berjalan.
85. Membuat objek antrian baru dari class QueueArray dan menyimpannya di variabel queue.
86. Menginisialisasi variabel pilih dengan nilai 0 sebagai nilai awal sebelum loop dimulai.
87.
88. Memulai perulangan utama yang terus berjalan selama pilih tidak sama dengan 5.
89. Mencetak judul sistem antrian kasir minimarket ke layar dengan baris baru di awal.
90. Mencetak opsi pertama menu: Tambah Pelanggan.
91. Mencetak opsi kedua menu: Layani Pelanggan.
92. Mencetak opsi ketiga menu: Tampilkan Antrian.
93. Mencetak opsi keempat menu: Hapus Semua Antrian.
94. Mencetak opsi kelima menu: Keluar dari program.
95.
96. Memulai blok penanganan error agar program tidak crash jika user salah input.
97. Mengambil input pilihan menu dari user dan mengubahnya menjadi bilangan bulat (integer).
98. Menangkap error jika user memasukkan sesuatu yang bukan angka (misal: huruf).
99. Mencetak pesan peringatan "Input tidak valid!" jika terjadi ValueError.
100. Mengulang perulangan dari awal menu jika terjadi error input.
101.
102. Mengecek jika user memilih menu nomor 1 (Tambah Pelanggan).
103. Memulai blok try untuk menangani kemungkinan error saat input nomor pelanggan.
104. Mengambil input nomor pelanggan dari user dan mengubahnya menjadi integer.
105. Memanggil method enqueue untuk menambahkan nomor pelanggan ke antrian.
106. Menangkap error ValueError jika user memasukkan bukan angka sebagai nomor pelanggan.
107. Mencetak pesan "Input tidak valid!" jika terjadi error pada input nomor pelanggan.
108.
109. Mengecek jika user memilih menu nomor 2 (Layani Pelanggan).
110. Memanggil method dequeue untuk melayani dan menghapus pelanggan paling depan antrian.
111.
112. Mengecek jika user memilih menu nomor 3 (Tampilkan Antrian).
113. Memanggil method display untuk menampilkan seluruh isi antrian ke layar.
114.
115. Mengecek jika user memilih menu nomor 4 (Hapus Semua Antrian).
116. Memanggil method clear_queue untuk mengosongkan seluruh antrian sekaligus.
117.
118. Mengecek jika user memilih menu nomor 5 (Keluar).
119. Mencetak pesan "Program selesai." dan mengakhiri loop karena pilih bernilai 5.
120.
121. Menangani kondisi jika user memasukkan angka yang tidak ada dalam pilihan menu.
122. Mencetak pesan "Menu tidak tersedia!" sebagai peringatan pilihan tidak valid.
123.
124. Baris standar Python untuk memastikan fungsi main() hanya berjalan jika file dieksekusi langsung.
125. Memanggil fungsi main() untuk menjalankan seluruh program.
