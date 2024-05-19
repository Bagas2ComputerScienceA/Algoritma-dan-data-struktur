def hitung_nilai_akhir(nama, nilai_keaktifan, nilai_tugas, nilai_ujian):
    nilai_murni_keaktifan = nilai_keaktifan * 0.20
    nilai_murni_tugas = nilai_tugas * 0.30
    nilai_murni_ujian = nilai_ujian * 0.50
    nilai_akhir = nilai_murni_keaktifan + nilai_murni_tugas + nilai_murni_ujian
    return nilai_akhir

def tentukan_grade(nilai_akhir):
    if nilai_akhir > 80:
        return "A"
    elif nilai_akhir > 70:
        return "B"
    elif nilai_akhir > 56:
        return "C"
    elif nilai_akhir > 46:
        return "D"
    else:
        return "E"

print("PROGRAM HITUNG NILAI AKHIR")
nama_siswa = input("Nama Siswa: ")
nilai_keaktifan = float(input("Nilai Keaktifan: "))
nilai_tugas = float(input("Nilai Tugas: "))
nilai_ujian = float(input("Nilai Ujian: "))

nilai_akhir = hitung_nilai_akhir(nama_siswa, nilai_keaktifan, nilai_tugas, nilai_ujian)
grade = tentukan_grade(nilai_akhir)

print("\nLayar Keluaran\n")
print("Siswa yang bernama", nama_siswa)
print("Dengan Nilai Persentasi Yang dihasilkan.")
print("Nilai Keaktifan * 20%:", nilai_keaktifan * 20, "%")
print("Nilai Tugas * 30%:", nilai_tugas * 30, "%")
print("Nilai Ujian * 50%:", nilai_ujian * 50, "%")
print("Jadi Siswa yang bernama", nama_siswa, "memperoleh nilai akhir sebesar", round(nilai_akhir, 2), "dengan grade", grade)
