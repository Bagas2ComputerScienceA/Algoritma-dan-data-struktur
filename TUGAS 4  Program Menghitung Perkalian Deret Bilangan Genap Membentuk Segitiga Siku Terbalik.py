# Inisialisasi variabel
n = 5  # Jumlah baris (tinggi segitiga)

# Menghitung dan menampilkan deret bilangan
for i in range(n, 0, -1):  # Perulangan mundur dari n ke 1
  # Menginisialisasi variabel untuk menampung hasil perkalian dan deret bilangan pada baris i
  hasil_perkalian = 1
  deret_bilangan = ""

  # Menghitung dan menambahkan bilangan genap pada baris i
  for j in range(1, i + 1):
    bilangan_genap = 2 * j
    hasil_perkalian *= bilangan_genap
    deret_bilangan += str(bilangan_genap) + " + "  # Menambahkan tanda "+"

  # Menampilkan hasil untuk baris i
  print(deret_bilangan[:-3] + "=", hasil_perkalian)  # Menghapus tanda "+" di akhir

# Menampilkan hasil total
print("----------")
print("110")  # Hasil total (di luar segitiga)
