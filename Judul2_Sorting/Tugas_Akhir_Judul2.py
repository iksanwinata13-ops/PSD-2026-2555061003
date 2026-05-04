def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                tukar(arr, j, j + 1)

def main():
    try:
        n = int(input("Masukkan jumlah kendaraan: "))
        if n <= 0:
            print("Jumlah kendaraan harus lebih dari 0!")
            return
    except ValueError:
        print("Jumlah kendaraan harus berupa angka!")
        return

    arr = []
    print("Masukkan jarak tempuh kendaraan:")

    for i in range(n):
        while True:
            try:
                nilai = int(input(f"Kendaraan ke-{i+1} (km): "))
                if nilai < 0:
                    print("Jarak tidak boleh negatif!")
                else:
                    arr.append(nilai)
                    break
            except ValueError:
                print("Jarak tempuh harus berupa angka!")

    bubble_sort(arr, n)

    print("Jarak tempuh kendaraan:", end=" ")
    for i in range(n):
        print(arr[i], end=" ")
    print()

if __name__ == "__main__":
    main()