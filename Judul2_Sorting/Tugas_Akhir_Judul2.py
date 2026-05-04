def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

def input_jumlah(pesan):
    while True:
        try:
            nilai = int(input(pesan))
            if nilai <= 0:
                print("Jumlah kendaraan harus lebih dari 0!")
            else:
                return nilai
        except ValueError:
            print("Jumlah kendaraan harus berupa angka!")

def input_jarak(pesan):
    while True:
        try:
            nilai = int(input(pesan))
            if nilai < 0:
                print("Jarak tidak boleh negatif!")
            else:
                return nilai
        except ValueError:
            print("Jarak tempuh harus berupa angka!")

def main():
    jarak = []

    jumlah = input_jumlah("Masukkan jumlah kendaraan: ")

    for i in range(jumlah):
        data = input_jarak(f"Masukkan jarak tempuh kendaraan ke-{i+1} (km): ")
        jarak.append(data)

    bubble_sort(jarak)

    print("\nJarak tempuh kendaraan:", jarak)

if __name__ == "__main__":
    main()
