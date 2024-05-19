# Inisialisasi variabel
n = 5  # Jumlah baris (tinggi segitiga)

# Menghitung dan menampilkan deret bilangan
for i in range(1, n + 1):
  # Menginisialisasi variabel untuk menampung jumlah dan deret bilangan pada baris i
  jumlah = 0
  deret_bilangan = ""

  # Menghitung dan menambahkan bilangan genap pada baris i
  for j in range(1, i + 1):
    bilangan_genap = 2 * j
    jumlah += bilangan_genap
    deret_bilangan += str(bilangan_genap) + " "

  # Menampilkan hasil untuk baris i
  print(deret_bilangan + "=", jumlah)
