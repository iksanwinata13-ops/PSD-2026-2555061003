Tugas Akhir Percobaan 1

Sistem Pemesanan Warkop Rusia

Program ini berfungsi sebagai sistem pemesanan makanan dan minuman sederhana yang dirancang untuk memudahkan pelanggan dalam melihat daftar menu, melakukan pemesanan, melihat daftar pesanan, serta menghitung total pembayaran secara otomatis. Program ini membantu meningkatkan efisiensi pelayanan di restoran atau warung kopi karena proses pemesanan menjadi lebih cepat, terstruktur, dan mudah digunakan.

<img width="1742" height="3142" alt="kk" src="https://github.com/user-attachments/assets/d2a4ff33-ea9e-413c-ac97-510f01aa8d02" />


Penjelasan Kode :
1. Mendefinisikan fungsi bernama menu() untuk membungkus kode yang menampilkan daftar pilihan menu utama
2. Menampilkan judul sistem WARKOP RUSIA dengan baris baru di awal
3. Menampilkan pilihan menu nomor 1
4. Menampilkan pilihan menu nomor 2
5. Menampilkan pilihan menu nomor 3
6. Menampilkan pilihan menu nomor 4
7. Menampilkan pilihan menu nomor 5
8. 
9. Mendefinisikan fungsi utama main() sebagai pusat logika program
10. Membuat List 2D bernama menu_restoran untuk menyimpan data menu dan harga
11. Menyimpan data menu pertama yaitu Nasi Goreng
12. Menyimpan data menu kedua yaitu Mie Ayam
13. Menyimpan data menu ketiga yaitu Bakso
14. Menyimpan data menu keempat yaitu Es Teh
15. Menyimpan data menu kelima yaitu Jus Jeruk
16. Menyimpan data menu keenam yaitu Kopi Hitam
17. Menutup list menu_restoran
18. 
19. Membuat list kosong pesanan untuk menyimpan menu yang dipesan pelanggan
20. 
21. Membuat perulangan utama while True agar program terus berjalan sampai user memilih keluar
22. Memanggil fungsi menu() untuk menampilkan menu utama
23. Meminta input pilihan menu dari user dan menyimpannya ke variabel choice
24. 
25. Mengecek jika user memilih menu nomor 1
26. Menampilkan judul daftar menu
27. Melakukan perulangan untuk menampilkan seluruh daftar menu
28. Menampilkan nomor menu, nama makanan/minuman, dan harga
29. 
30. Mengecek jika user memilih menu nomor 2
31. Menampilkan judul pilih menu
32. Melakukan perulangan untuk menampilkan semua daftar menu kembali
33. Menampilkan daftar menu yang bisa dipilih
34. 
35. Meminta input nomor menu dari user, dapat lebih dari satu dipisahkan koma
36. Memecah input menggunakan split(",")
37. 
38. Melakukan perulangan untuk membaca setiap item pilihan
39. Menggunakan blok try untuk mencegah program error
40. Mengubah input menjadi bilangan bulat menggunakan int()
41. Mengecek apakah nomor menu valid
42. Jika valid, menu dimasukkan ke list pesanan
43. Menampilkan pesan berhasil ditambahkan ke pesanan
44. Jika nomor menu tidak tersedia
45. Menampilkan pesan kesalahan
46. 
47. Jika input bukan angka
48. Menampilkan pesan kesalahan input
49. 
50. Mengecek jika user memilih menu nomor 3
51. Menampilkan judul daftar pesanan
52. 
53. Mengecek apakah list pesanan kosong
54. Jika kosong, tampilkan pesan belum memesan
55. Jika ada pesanan
56. Melakukan perulangan untuk menampilkan semua pesanan
57. Menampilkan nomor pesanan, nama menu, dan harga
58. 
59. Mengecek jika user memilih menu nomor 4
60. Membuat variabel total = 0
61. 
62. Melakukan perulangan untuk menjumlahkan harga seluruh pesanan
63. Menambahkan harga menu ke variabel total
64. 
65. Menampilkan total pembayaran
66. 
67. Mengecek jika user memilih menu nomor 5
68. Menampilkan ucapan terima kasih
69. Menggunakan break untuk keluar dari program
70. 
71. Jika user memasukkan pilihan selain menu yang tersedia
72. Menampilkan pesan kesalahan pilihan
73. 
74. memastikan program berjalan jika file dieksekusi langsung
75. Memanggil fungsi main() untuk menjalankan program

Output : 
Tampilan menu utama
<img width="271" height="167" alt="Screenshot 2026-04-28 222312" src="https://github.com/user-attachments/assets/e15d4849-dc1e-44e5-94e2-5697d964435d" />

Menu 1
<img width="283" height="167" alt="Screenshot 2026-04-28 222455" src="https://github.com/user-attachments/assets/72c4c7d8-8e86-4cbd-9da1-e2846464da8c" />

Menu 2
<img width="431" height="93" alt="Screenshot 2026-04-28 222636" src="https://github.com/user-attachments/assets/c7ad71b1-15e5-4c6a-b714-5cfff59352d9" />

Menu 3
<img width="281" height="102" alt="Screenshot 2026-04-28 222746" src="https://github.com/user-attachments/assets/705f88f7-7864-4195-b0ee-97fd45372166" />

Menu 4
<img width="259" height="34" alt="Screenshot 2026-04-28 222911" src="https://github.com/user-attachments/assets/f211ef48-bf59-496b-b2af-70e0399f377b" />

Menu 5
<img width="427" height="23" alt="Screenshot 2026-04-28 222932" src="https://github.com/user-attachments/assets/43e3d6ee-f95c-41b2-846a-c6f035d1b6ec" />

Link : 
