nama = input("masukkan nama :")
umur = int(input("masukkan umur :"))
tinggi = int(input("masukkan tinggi :"))
angka_fav = int(input("masukkan angka favorit kamu :"))

print("=========================")
pensil = int(input("masukkan jumlah pensil :"))
buku = int(input("masukkan jumlah buku :"))
hasil1 = pensil * 2000
hasil2 = buku * 5000

print("pensil :", hasil1)
print("buku :", hasil2)
print("total pembelian :", hasil1 + hasil2)

print("==========================")
if angka_fav % 2 == 0:
    print("angka favorit anda adalah bilangan genap")
else:
    print("angka favorit anda adalah bilangan ganjil")
