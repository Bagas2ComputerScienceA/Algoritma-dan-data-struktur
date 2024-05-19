def main():
    # Input data siswa
    print("PROGRAM HITUNG NILAI RATA-RATA SISWA")
    nim = input("Nim Siswa : ")
    nama = input("Nama Siswa : ")
    nilai_tugas1 = float(input("Nilai Tugas I : "))
    nilai_tugas2 = float(input("Nilai Tugas II : "))
    nilai_tugas3 = float(input("Nilai Tugas III : "))

    # Menghitung nilai rata-rata
    nilai_rata_rata = (nilai_tugas1 + nilai_tugas2 + nilai_tugas3) / 3

    # Output hasil
    print("\nNim", nim, "Siswa yang bernama", nama)
    print("Memperoleh nilai rata-rata", nilai_rata_rata, "dari hasil tugas yang diikutinya.")

    # Menahan tampilan hasil program agar tidak langsung kembali
    input("\nPress any key to exit...")

if __name__ == "__main__":
    main()
