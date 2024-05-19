# Inisialisasi variabel untuk menampung jumlah dan deret bilangan
jumlah = 0
deret_bilangan = ""

# Perulangan untuk menghitung 10 bilangan genap
for i in range(1, 11):
  # Menghitung bilangan genap
  bilangan_genap = 2 * i

  # Menambahkan bilangan genap ke deret
  deret_bilangan += str(bilangan_genap) + " + "

  # Menghitung jumlah
  jumlah += bilangan_genap

# Menampilkan hasil
print("Deret bilangan genap:")
print(deret_bilangan[:-3])  # Menghapus tanda "+" di akhir
print("Jumlah:", jumlah)
