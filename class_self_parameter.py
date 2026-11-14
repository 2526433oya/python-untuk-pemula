class Nilai:
    def __init__(self, mapel, angka):
        self.mapel = mapel
        self.angka = angka

    def tampil(self):
        print(self.mapel, ":", self.angka)


n = Nilai("Pemrograman Web", 90)
n.tampil()
