def hitung_nilai_akhir(nama, nilai_keaktifan, nilai_tugas, nilai_ujian):
    # Menghitung nilai murni dari masing-masing nilai
    nilai_murni_keaktifan = nilai_keaktifan * 0.20
    nilai_murni_tugas = nilai_tugas * 0.50
    nilai_murni_ujian = nilai_ujian * 0.30

    # Menghitung nilai akhir
    nilai_akhir = nilai_murni_keaktifan + nilai_murni_tugas + nilai_murni_ujian

    # Output hasil
    print("\nSiswa yang bernama", nama)
    print("Dengan Nilai Persentasi Yang dihasilkan:")
    print("Nilai Keaktifan * 20% :", nilai_murni_keaktifan)
    print("Nilai Tugas * 50% :", nilai_murni_tugas)
    print("Nilai Ujian * 30% :", nilai_murni_ujian)
    print("Jadi Siswa yang bernama", nama, "memperoleh nilai akhir sebesar", nilai_akhir)

def main():
    # Input data siswa
    print("PROGRAM HITUNG NILAI AKHIR")
    nama_siswa = input("Nama Siswa : ")
    nilai_keaktifan = float(input("Nilai Keaktifan : "))
    nilai_tugas = float(input("Nilai Tugas : "))
    nilai_ujian = float(input("Nilai Ujian : "))

    # Memanggil fungsi untuk menghitung nilai akhir
    hitung_nilai_akhir(nama_siswa, nilai_keaktifan, nilai_tugas, nilai_ujian)

if __name__ == "__main__":
    main()
