class Mahasiswa:
  def __init__(self, nim, nama, nilai_uts, nilai_uas):
    self.nim = nim
    self.nama = nama
    self.nilai_uts = nilai_uts
    self.nilai_uas = nilai_uas
    self.nilai_akhir = self.hitung_nilai_akhir()
    self.nilai_huruf = self.hitung_nilai_huruf()

  def hitung_nilai_akhir(self):
    return (self.nilai_uas * 0.4) + (self.nilai_uts * 0.6)

  def hitung_nilai_huruf(self):
    if self.nilai_akhir >= 80:
      return "A"
    elif self.nilai_akhir >= 70:
      return "B"
    elif self.nilai_akhir >= 56:
      return "C"
    elif self.nilai_akhir >= 47:
      return "D"
    else:
      return "E"

def main():
  jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))
  mahasiswa_list = []

  for i in range(jumlah_mahasiswa):
    nim = input(f"Masukkan NIM mahasiswa ke-{i+1}: ")
    nama = input(f"Masukkan nama mahasiswa ke-{i+1}: ")
    nilai_uts = float(input(f"Masukkan nilai UTS mahasiswa ke-{i+1}: "))
    nilai_uas = float(input(f"Masukkan nilai UAS mahasiswa ke-{i+1}: "))

    mahasiswa = Mahasiswa(nim, nama, nilai_uts, nilai_uas)
    mahasiswa_list.append(mahasiswa)

  # Cetak tabel
  print("\n| No | Nama Mahasiswa | Nilai UTS | Nilai UAS | Nilai Akhir | Nilai Huruf |")
  print("|----|----------------|-----------|-----------|-------------|-------------|")
  for i, mahasiswa in enumerate(mahasiswa_list):
    print(f"| {i+1:2} | {mahasiswa.nama:15} | {mahasiswa.nilai_uts:9.2f} | {mahasiswa.nilai_uas:9.2f} | {mahasiswa.nilai_akhir:9.2f} | {mahasiswa.nilai_huruf:3} |")

if __name__ == "__main__":
  main()
