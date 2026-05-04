Tugas Akhir Percobaan 2

Judul Program : Program mengurutkan jarak tempuh kendaraan

Program ini berfungsi untuk mengelola data jarak tempuh kendaraan dengan tujuan mengurutkan data tersebut dari nilai terkecil hingga terbesar secara otomatis. Program ini membantu pengguna dalam menyusun data jarak tempuh kendaraan agar lebih terstruktur dan mudah dianalisis. Dengan adanya validasi input, program ini juga mampu mencegah kesalahan saat memasukkan data, sehingga hasil yang diperoleh lebih akurat dan dapat diandalkan. Algoritma yang digunakan dalam program ini adalah Bubble Sort, yaitu metode pengurutan sederhana yang bekerja dengan cara membandingkan dua elemen yang berdekatan dan menukarnya jika posisinya tidak sesuai.

<img width="1510" height="2002" alt="kkkk" src="https://github.com/user-attachments/assets/557ecb46-561f-4532-8e89-01e91bca54c9" />

Penjelasan kode : 
1. Mendefinisikan fungsi bubble_sort untuk mengurutkan data.
2. Mengambil panjang data menggunakan len().
3. Memulai perulangan pertama untuk proses sorting.
4. Memulai perulangan kedua untuk membandingkan elemen.
5. Mengecek apakah data lebih besar dari sebelahnya.
6. Menukar posisi jika tidak sesuai urutan.
7. 
8. Mendefinisikan fungsi input_jumlah untuk input jumlah kendaraan.
9. Menggunakan perulangan while True agar input terus diminta.
10. Menggunakan try untuk mencoba konversi ke integer.
11. Mengecek apakah nilai kurang dari atau sama dengan 0.
12. Menampilkan pesan error jika tidak valid.
13. Mengembalikan nilai jika sudah benar.
14. Menangkap error jika input bukan angka.
15. Menampilkan pesan kesalahan input.
16.
17. Mendefinisikan fungsi input_jarak untuk input jarak tempuh.
18. Menggunakan perulangan agar input valid.
19. Menggunakan try-except untuk error handling.
20. Mengecek apakah nilai negatif.
21. Menampilkan pesan jika jarak tidak valid.
22. Mengembalikan nilai jika valid.
23. Menangkap error jika input bukan angka.
24. Menampilkan pesan error.
25. 
26. Mendefinisikan fungsi utama main.
27. Membuat list kosong untuk menyimpan data.
28. Memanggil fungsi input_jumlah.
29. Memulai perulangan untuk input data kendaraan.
30. Mengambil input jarak tempuh tiap kendaraan.
31. Menyimpan data ke dalam list.
32. 
33. Memanggil fungsi bubble_sort untuk mengurutkan data.
34. Menampilkan hasil pengurutan dalam bentuk array.
35. 
36. Mengecek apakah file dijalankan langsung.
37. Memanggil fungsi main untuk menjalankan program.

Output :
