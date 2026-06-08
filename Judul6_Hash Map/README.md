Tugas Akhir Percobaan 6

Judul Program : Sistem Pencarian Buku Perpustakaan

Program ini berfungsi sebagai sistem pencarian buku perpustakaan yang menggunakan struktur data Hash Map dengan metode Separate Chaining. Sistem dapat menyimpan data buku berdasarkan kode buku dan judul buku, menampilkan seluruh data buku yang tersimpan pada hash table, serta melakukan pencarian buku berdasarkan kode buku yang dimasukkan oleh pengguna.

<img width="1388" height="3978" alt="kbnkj" src="https://github.com/user-attachments/assets/28e7cc95-8dbe-43b4-80c8-8ced2301381d" />

Penjelasan Kode : 
1. Mendefinisikan class Node.
2. Mendefinisikan constructor untuk class Node.
3. Menyimpan kode_buku ke atribut key.
4. Menyimpan judul_buku ke atribut value.
5. Menginisialisasi pointer next dengan nilai None.
6.
7.
8. Mendefinisikan class HashMapPerpustakaan.
9. Mendefinisikan constructor untuk class HashMapPerpustakaan.
10. Menyimpan ukuran hash table ke variabel SIZE.
11. Membuat hash table berupa list yang berisi None.
12.
13. Mendefinisikan fungsi hash_function().
14. Menghitung indeks hash menggunakan operasi modulo.
15.
16. Mendefinisikan fungsi tambah_buku().
17. Menghitung indeks penyimpanan buku menggunakan hash_function().
18. Mengambil node pertama pada indeks tersebut.
19.
20. Melakukan perulangan selama current tidak bernilai None.
21. Memeriksa apakah kode buku sudah ada.
22. Memperbarui judul buku jika kode buku ditemukan.
23. Menghentikan proses penambahan data.
24. Berpindah ke node berikutnya.
25.
26. Membuat node baru untuk data buku.
27. Menghubungkan node baru ke linked list yang sudah ada.
28. Menyimpan node baru pada indeks hash table.
29.
30. Mendefinisikan fungsi cari_buku().
31. Menghitung indeks pencarian menggunakan hash_function().
32. Mengambil node pertama pada indeks tersebut.
33.
34. Melakukan perulangan selama current tidak bernilai None.
35. Memeriksa apakah kode buku yang dicari ditemukan.
36. Mengembalikan node yang ditemukan.
37. Berpindah ke node berikutnya.
38.
39. Mengembalikan None jika data tidak ditemukan.
40.
41. Mendefinisikan fungsi hapus_buku().
42. Menghitung indeks data yang akan dihapus.
43. Mengambil node pertama pada indeks tersebut.
44. Membuat variabel prev dengan nilai None.
45.
46. Melakukan perulangan selama current tidak bernilai None.
47. Memeriksa apakah kode buku ditemukan.
48. Memeriksa apakah node yang dihapus berada di awal linked list.
49. Menghubungkan hash table langsung ke node berikutnya.
50. Menjalankan blok else jika node bukan node pertama.
51. Menghubungkan node sebelumnya ke node setelah current.
52. Mengembalikan True jika penghapusan berhasil.
53.
54. Memindahkan prev ke node saat ini.
55. Berpindah ke node berikutnya.
56.
57. Mengembalikan False jika data tidak ditemukan.
58.
59. Mendefinisikan fungsi tampilkan_buku().
60. Menampilkan judul data buku perpustakaan.
61. Melakukan perulangan untuk setiap indeks hash table.
62. Menampilkan nomor indeks.
63. Mengambil node pertama pada indeks tersebut.
64.
65. Melakukan perulangan selama current tidak bernilai None.
66. Menampilkan key dan value dari node saat ini.
67. Berpindah ke node berikutnya.
68.
69. Menampilkan NULL jika sudah mencapai akhir linked list.
70.
71.
72. Mendefinisikan fungsi main().
73. Membuat objek HashMapPerpustakaan.
74.
75. Menambahkan buku dengan kode 101 dan judul "Algoritma dan Pemrograman".
76. Menambahkan buku dengan kode 111 dan judul "Struktur Data".
77. Menambahkan buku dengan kode 121 dan judul "Rekayasa Perangkat Lunak".
78. Menambahkan buku dengan kode 102 dan judul "Pengenalan Pemrograman".
79. Menambahkan buku dengan kode 112 dan judul "Matematika".
80.
81.
82. Menampilkan seluruh data buku yang tersimpan pada hash table.
83.
84. Meminta pengguna memasukkan kode buku yang ingin dicari.
85.
86. Memanggil fungsi cari_buku() berdasarkan kode yang dimasukkan.
87.
88. Memeriksa apakah buku ditemukan.
89. Menampilkan pesan bahwa buku ditemukan.
90. Menampilkan kode buku yang ditemukan.
91. Menampilkan judul buku yang ditemukan.
92. Menjalankan blok else jika buku tidak ditemukan.
93. Menampilkan pesan buku tidak ditemukan.
94.
95.
96. Memastikan fungsi main() hanya dijalankan ketika file dieksekusi langsung.
97. Memanggil fungsi main().

Output :

<img width="1007" height="381" alt="Screenshot 2026-06-08 221853" src="https://github.com/user-attachments/assets/ff97babd-c82d-4595-9242-d28e7a7ce9f8" />

<img width="1003" height="336" alt="Screenshot 2026-06-08 224753" src="https://github.com/user-attachments/assets/3352bc03-74cb-4334-91a0-f2f972a1d62a" />

Link : https://youtu.be/Hg63GK1NdAE?si=9c9nUpr4mJtbSZNQ
