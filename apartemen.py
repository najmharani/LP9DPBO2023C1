from hunian import Hunian

class Apartemen(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, jml_lantai, pembayaran):
        super().__init__("Apartemen", jml_penghuni, jml_kamar, pembayaran=pembayaran)
        self.nama_pemilik = nama_pemilik
        self.jml_lantai = jml_lantai

    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nJumlah Kamar : " + str(self.jml_kamar) + "\nJumlah Lantai : " + str(self.jml_lantai) + "\n";
    
    def set_nama_pemilik(self, nama_pemilik):
        self.nama_pemilik = nama_pemilik