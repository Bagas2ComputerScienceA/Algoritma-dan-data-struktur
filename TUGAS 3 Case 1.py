def hitung_rata_rata(nama, nilai1, nilai2, nilai3):
    rata_rata = (nilai1 + nilai2 + nilai3) / 3
    return rata_rata

def tentukan_juara(rata_rata):
    if rata_rata > 80:
        return "I"
    elif rata_rata > 75:
        return "II"
    elif rata_rata > 65:
        return "III"
    else:
        return "Tidak Juara"

print("PROGRAM HITUNG NILAI RATA-RATA")
nama_siswa = input("Nama Siswa: ")
nilai_pertandingan1 = float(input("Nilai Pertandingan I: "))
nilai_pertandingan2 = float(input("Nilai Pertandingan II: "))
nilai_pertandingan3 = float(input("Nilai Pertandingan III: "))

rata_rata_nilai = hitung_rata_rata(nama_siswa, nilai_pertandingan1, nilai_pertandingan2, nilai_pertandingan3)
juara = tentukan_juara(rata_rata_nilai)

print("\nLayar Keluaran\n")
print("Siswa yang bernama", nama_siswa)
print("Memperoleh nilai rata-rata", round(rata_rata_nilai, 2), "dan menjadi juara ke-" + juara, "dari hasil perlombaan yang diikutinya.")
