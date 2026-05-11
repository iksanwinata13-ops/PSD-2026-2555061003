def interpolation_search(data, n, target):
    low = 0
    high = n - 1
    while target >= data[low] and target <= data[high] and low <= high:
        if data[high] == data[low]:
            if data[low] == target:
                return low
            break
        pos = low + int(((target - data[low]) / (data[high] - data[low])) * (high - low))
        print(f"Posisi estimasi: {pos}, nilai: {data[pos]}")
        if target > data[pos]:
            low = pos + 1
        elif target < data[pos]:
            high = pos - 1
        else:
            return pos
    if low < n and data[low] == target:
        return low
    return -1

def main():
    data = [1001, 1005, 1010, 1015, 1020, 1025, 1030, 1035, 1040]
    n = len(data)
    print(f"Data array: {data}")
    while True:
        try:
            target = int(input("Masukkan ID buku yang ingin dicari: "))
            break
        except ValueError:
            print("Input tidak valid, silakan masukkan angka!")
    pos = interpolation_search(data, n, target)
    if pos != -1:
        print(f"ID Buku ditemukan pada indeks ke-{pos}")
    else:
        print("ID Buku tidak ditemukan")

if __name__ == "__main__":
    main()
