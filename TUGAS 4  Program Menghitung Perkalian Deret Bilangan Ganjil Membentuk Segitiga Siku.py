# Inisialisasi variabel
n = 5  # Jumlah baris (tinggi segitiga)

# Menghitung dan menampilkan deret bilangan
for i in range(1, n + 1):
  # Menginisialisasi variabel untuk menampung hasil perkalian dan deret bilangan pada baris i
  hasil_perkalian = 1
  deret_bilangan = ""

  # Menghitung dan menambahkan bilangan ganjil pada baris i
  for j in range(1, i + 1):
    bilangan_ganjil = 2 * j - 1
    hasil_perkalian *= bilangan_ganjil
    deret_bilangan += str(bilangan_ganjil) + " "  # Menambahkan spasi

  # Menampilkan hasil untuk baris i
  print(deret_bilangan + "=", hasil_perkalian)
