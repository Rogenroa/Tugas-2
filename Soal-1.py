  
def menu():
    print("----My Menu----")
    print("[1] Daftar Kontak")
    print("[2] Tambah Kontak")
    print("[3] Keluar")

menu()
option = int(input("Pilih menu : "))

Nama = ["Fajar", "Alex"]
NoTelpon = [811, 812]

while option != 3:
    if option == 1:
    #do option 1
        print("Daftar Kontak :")
        print("Nama : "+ str(Nama))
        print("NoTelpon : "+ str(NoTelpon))
    elif option == 2:
    #do option 2
        d = input("Nama : ")
        e = int(input("No Telpon : "))
        Nama.append(d)
        NoTelpon.append(e)
        print("Kontak berhasil ditambahkan")
    else:
    #do diluar itu
        print("Menu tidak tersedia")

    print()
    menu()
    option = int(input("Pilih menu : "))

print("Program selesai, sampai jumpa!")