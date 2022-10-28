class barang:
    discount = 0.5
    def __init__(self, nama: str, harga: float, jumlah: int):

        assert harga >=0
        assert jumlah >=0

        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah
       
    def total(self):
        return self.harga*self.jumlah
    
    def diskon(self):
         self.harga = self.harga * barang.discount

barang1 = barang("iphone", 12000000,4)
barang1.diskon()
barang2 = barang("android", 13000000, 9)
barang2.diskon()

print(barang1.total())
print(barang2.total())