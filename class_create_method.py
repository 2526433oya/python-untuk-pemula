class Siswa:
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas

    def perkenalan(self):
        print("Nama saya", self.nama, "dari kelas", self.kelas)


s = Siswa("Oya", "XI RPL")
s.perkenalan()
