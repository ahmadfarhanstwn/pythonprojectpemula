import math

print("Daftar operasi menghitung luas bangun datar:\n1. Menghitung Luas Segitiga\n2. Menghitung Luas Lingkaran\n3. Menghitung Luas Persegi\n4. Menghitung Luas Persegi Panjang\n5. Menghitung luas Belah Ketupat\n6. Menghitung luas Jajar Genjang\n7. Menghitung luas Layang-Layang")
choice = input("Pilih Operasi Yang Akan Digunakan (Berupa Angka) : ")
print("\n")

if choice == "1":
    print("MENGHITUNG LUAS SEGITIGA")
    alas = float(input("Masukkan nilai alas : "))
    tinggi = float(input("Masukkan nilai tinggi : "))
    luassegitiga = float(0.5 * alas * tinggi)
    print("Luas Segitiga : %f" %luassegitiga)

elif choice == "2":
    print("MENGHITUNG LUAS LINGKARAN")
    r = float(input("Masukkan Nilai jari-jari : "))
    luaslingkaran = float(math.pi * r ** 2)
    print("Luas Lingkaran : %f" %luaslingkaran)

elif choice == "3":
    print("MENGHITUNG LUAS PERSEGI")
    sisi = float(input("Masukkan nilai sisi : "))
    luaspersegi = float(sisi ** 2)
    print("Luas Persegi : %f" %luaspersegi)

elif choice == "4":
    print("MENGHITUNG LUAS PERSEGI PANJANG")
    panjang = float(input("Masukkan nilai panjang : "))
    lebar = float(input("Masukkan nilai lebar : "))
    luaspersegipanjang = float(panjang * lebar)
    print("Luas Persegi Panjang : %f" %luaspersegipanjang)

elif choice == "5":
    print("MENGHITUNG LUAS BELAH KETUPAT")
    d1 = float(input("Masukkan nilai diameter 1 : "))
    d2 = float(input("Masukkan nilai diameter 2 : "))
    luasbelahketupat = float(0.5 * d1 * d2)
    print("Luas Belah Ketupat : %f" %luasbelahketupat)

elif choice == "6":
    print("MENGHITUNG LUAS JAJAR GENJANG")
    alas = float(input("Masukkan nilai alas : "))
    tinggi = float(input("Masukkan nilai tinggi : "))
    luasjajargenjang = float(alas * tinggi)
    print("Luas Jajar Genjang : %f" %luasjajargenjang)

elif choice == "7":
    print("MENGHITUNG LUAS LAYANG-LAYANG")
    d1 = float(input("Masukkan nilai diameter 1 : "))
    d2 = float(input("Masukkan nilai diameter 2 : "))
    luaslayanglayang = float(0.5 * d1 * d2)
    print("Luas Belah Ketupat : %f" % luaslayanglayang)

else :
    print("Maaf angka yang anda masukkan tidak syncron, silahkan coba kembali !!!")