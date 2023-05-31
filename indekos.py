from hunian import Hunian

class Indekos(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni, pembayaran, is_kmr_kosong=False):
        super().__init__("Indekos", pembayaran=pembayaran)
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni
        self.is_kmr_kosong = is_kmr_kosong

    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni
    
    def get_is_kmr_kosong(self):
        
        if self.is_kmr_kosong == True:
            return "Ada"
        
        return "Tidak Ada"

    def get_summary(self):
        return "Hunian Indekos."
    
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nPenghuni : " + str(self.nama_penghuni) + "\nJumlah Kamar : " + str(self.jml_kamar) + "\nAda Kamar Kosong : " + self.get_is_kmr_kosong() + "\nPembayaran : " + self.pembayaran + "\n";
    
    def set_nama_penghuni(self, nama_penghuni):
        self.nama_penghuni = nama_penghuni