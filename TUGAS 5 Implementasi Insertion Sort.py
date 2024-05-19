def insertion_sort(array):
  """
  Fungsi untuk mengurutkan array menggunakan Insertion Sort.

  Args:
    array: Array bilangan bulat yang ingin diurutkan.

  Returns:
    Array yang telah diurutkan.
  """

  for i in range(1, len(array)):
    key = array[i]
    j = i - 1
    while j >= 0 and array[j] > key:
      array[j + 1] = array[j]
      j -= 1
    array[j + 1] = key
  return array

# Meminta input dari pengguna
panjang_array = int(input("Masukkan panjang array: "))
array = []
for i in range(panjang_array):
  elemen = int(input(f"Masukkan elemen ke-{i + 1}: "))
  array.append(elemen)

# Menampilkan array sebelum diurutkan
print("Array sebelum diurutkan:", array)

# Mengurutkan array menggunakan Insertion Sort
array_urut = insertion_sort(array)

# Menampilkan array setelah diurutkan
print("Array setelah diurutkan:", array_urut)
