class Pegawai:
  def __init__(self, nama, jam_kerja):
    self.nama = nama
    self.jam_kerja = jam_kerja
    self.hitung_honor()

  def hitung_honor(self):
    if self.jam_kerja > 8:
      self.honor_lembur = (self.jam_kerja - 8) * 5000
      self.total_honor = self.honor_lembur + 15000
    else:
      self.honor_lembur = 0
      self.total_honor = 15000

def main():
  jumlah_pegawai = int(input("Masukkan jumlah pegawai: "))
  pegawai_list = []

  for i in range(jumlah_pegawai):
    nama = input(f"Masukkan nama pegawai ke-{i+1}: ")
    jam_kerja = float(input(f"Masukkan jam kerja pegawai ke-{i+1}: "))

    pegawai = Pegawai(nama, jam_kerja)
    pegawai_list.append(pegawai)

  # Cetak tabel
  print("\n| No | Nama Pegawai | Jam Kerja | Honor Lembur | Total Honor |")
  print("|----|--------------|-----------|--------------|-------------|")
  for i, pegawai in enumerate(pegawai_list):
    print(f"| {i+1:2} | {pegawai.nama:15} | {pegawai.jam_kerja:9.2f} | {pegawai.honor_lembur:11d} | {pegawai.total_honor:11d} |")

if __name__ == "__main__":
  main()
