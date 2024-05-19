def hitung_gaji(gaji_pokok, golongan, pendidikan, jam_kerja):
    # Hitung tunjangan jabatan
    if golongan == 1:
        tunjangan_jabatan = 0.05 * gaji_pokok
    elif golongan == 2:
        tunjangan_jabatan = 0.10 * gaji_pokok
    else:  # Golongan 3
        tunjangan_jabatan = 0.15 * gaji_pokok

    # Hitung tunjangan pendidikan
    if pendidikan == "SMA":
        tunjangan_pendidikan = 0.025 * gaji_pokok
    elif pendidikan == "D1":
        tunjangan_pendidikan = 0.05 * gaji_pokok
    elif pendidikan == "D3":
        tunjangan_pendidikan = 0.20 * gaji_pokok
    else:  # S1
        tunjangan_pendidikan = 0.30 * gaji_pokok

    # Hitung honor lembur
    if jam_kerja > 8:
        honor_lembur = (jam_kerja - 8) * 3500
    else:
        honor_lembur = 0

    # Total gaji
    total_gaji = gaji_pokok + tunjangan_jabatan + tunjangan_pendidikan + honor_lembur

    return tunjangan_jabatan, tunjangan_pendidikan, honor_lembur, total_gaji

print("PROGRAM HITUNG GAJI KARYAWAN KONTRAK")
nama_karyawan = input("Nama Karyawan: ")
golongan_jabatan = int(input("Golongan Jabatan (1/2/3): "))
pendidikan = input("Pendidikan (SMA/D1/D3/S1): ")
jam_kerja = int(input("Jumlah jam kerja: "))

gaji_pokok = 300000  # Gaji pokok per bulan

tunjangan_jabatan, tunjangan_pendidikan, honor_lembur, total_gaji = hitung_gaji(gaji_pokok, golongan_jabatan, pendidikan, jam_kerja)

print("\nLayar Keluaran\n")
print("Karyawan yang bernama", nama_karyawan)
print("Honor yang diterima:")
print("Tunjangan Jabatan Rp", tunjangan_jabatan)
print("Tunjangan Pendidikan Rp", tunjangan_pendidikan)
print("Honor Lembur Rp", honor_lembur)
print("+")
print("Total Gaji Rp", total_gaji)
