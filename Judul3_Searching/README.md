Tugas Akhir Percobaan 3

Judul Program : Sistem Pencarian ID Buku Perpustakaan

Program ini berfungsi sebagai sistem pencarian ID buku perpustakaan menggunakan algoritma Interpolation Search. Program dirancang untuk membantu petugas perpustakaan menemukan posisi buku dengan cepat pada data yang sudah tersusun secara terurut. User dapat memasukkan ID buku yang ingin dicari, kemudian sistem akan memperkirakan posisi data menggunakan rumus interpolasi hingga data ditemukan atau dinyatakan tidak ditemukan.
<img width="1680" height="1774" alt="llll" src="https://github.com/user-attachments/assets/08dc1b9c-254d-4ad8-bdf0-1bdbb37e7c8d" />
Penjelasan kode :

1. Mendefinisikan fungsi interpolation_search(data, n, target) untuk melakukan pencarian data menggunakan algoritma Interpolation Search.

2. Membuat variabel low dengan nilai awal 0 sebagai indeks awal array.

3. Membuat variabel high dengan nilai n - 1 sebagai indeks akhir array.

4. Melakukan perulangan selama target masih berada dalam rentang data dan indeks masih valid.

5. Mengecek apakah nilai data pada indeks high dan low sama.

6. Mengecek apakah data pada indeks low sama dengan target.

7. Jika benar, fungsi mengembalikan indeks low

8. Menghentikan proses perulangan menggunakan break

9. Menghitung posisi estimasi menggunakan rumus interpolation search.

10. Menampilkan posisi estimasi beserta nilai data pada posisi tersebut.

11. Mengecek apakah target lebih besar dari data pada posisi estimasi.

12. Jika benar, nilai low digeser ke kanan pos + 1

13. Mengecek apakah target lebih kecil dari data pada posisi estimasi.

14. Jika benar, nilai high digeser ke kiri pos - 1

15.

16. Jika data ditemukan, fungsi mengembalikan posisi data.

17. Mengecek kembali apakah indeks low masih berada dalam batas array dan data sesuai target.

18. Jika benar, fungsi mengembalikan indeks low

19. Jika data tidak ditemukan, fungsi mengembalikan nilai -1

20.

21. Mendefinisikan fungsi main() sebagai fungsi utama program.

22. Membuat list berisi data ID buku perpustakaan yang sudah terurut.

23. Menghitung jumlah data menggunakan fungsi len()

24. Menampilkan seluruh data array ke layar.

25. Memulai perulangan input agar user memasukkan data yang valid.

26. Memulai blok try untuk menangani kesalahan input.

27. Meminta user memasukkan ID buku yang ingin dicari.

28. Jika input valid, perulangan dihentikan menggunakan break

29. Menangkap error jika user memasukkan selain angka.

30. Menampilkan pesan input tidak valid.

31. Memanggil fungsi interpolation_search untuk mencari data.

32. Mengecek apakah hasil pencarian tidak sama dengan -1

33. Jika data ditemukan, program menampilkan indeks data.

34.

35. Jika data tidak ditemukan, program menampilkan pesan “ID Buku tidak ditemukan”

36.

37. Baris standar Python untuk memastikan fungsi main() hanya dijalankan ketika file dieksekusi langsung.

38. Memanggil fungsi main() untuk menjalankan program.

Output :
<img width="615" height="111" alt="Screenshot 2026-05-11 221155" src="https://github.com/user-attachments/assets/40e599de-25d0-460b-af5c-a6df642f0e9e" />
<img width="615" height="61" alt="Screenshot 2026-05-11 221224" src="https://github.com/user-attachments/assets/9d9e9015-3385-46b5-8a52-21d0adef18de" />

