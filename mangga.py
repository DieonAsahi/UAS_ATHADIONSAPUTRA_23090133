from buah import Buah

class Mangga(Buah):
    def __init__(self, nama, jenis):
        super().__init__(nama)
        self.jenis = jenis
    
    def deskripsi(self):
        return f"Mangga: {self.nama}, Jenis: {self.jenis}"