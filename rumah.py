from hunian import Hunian

class Rumah(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar,  luas_tanah, pembayaran):
        super().__init__("Rumah", jml_penghuni, jml_kamar, pembayaran=pembayaran)
        self.nama_pemilik = nama_pemilik
        self.luas_tanah = luas_tanah

    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_luas_tanah(self):
        return str(self.luas_tanah) + " m^2"
    
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nJumlah Kamar : " + str(self.jml_kamar) + "\nLuas Tanah : " + self.get_luas_tanah() + "\n";
    
    def set_nama_pemilik(self, nama_pemilik):
        self.nama_pemilik = nama_pemilik
   