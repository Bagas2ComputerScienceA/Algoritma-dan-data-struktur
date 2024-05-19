# Inisialisasi variabel untuk menampung jumlah dan deret bilangan
jumlah = 0
deret_bilangan = ""

# Perulangan untuk menghitung 10 bilangan ganjil
for i in range(1, 11):
  # Menghitung bilangan ganjil
  bilangan_ganjil = 2 * i - 1

  # Menambahkan bilangan ganjil ke deret
  deret_bilangan += str(bilangan_ganjil) + " + "

  # Menghitung jumlah
  jumlah += bilangan_ganjil

# Menampilkan hasil
print("Deret bilangan ganjil:")
print(deret_bilangan[:-3])  # Menghapus tanda "+" di akhir
print("Jumlah:", jumlah)
