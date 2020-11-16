def home() :
    print("\n --- Menu ---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    pilih = int(input("Pilih nomor menu : "))
    return pilih

def daftar(kontak1,kontak2):
    print("\nDaftar Kontak : ")
    for i in range(len(kontak1)): #jml kontak1=kontak2
        print("\nNama : ",kontak1[i])
        print("No Telepon : ",kontak2[i])

def tambah(kontak1,kontak2):
    kontak1.append(str(input("Nama : ")))
    kontak2.append(str(input("No Telepon : ")))

    

value=True
kontak1 = ["Lea","Michael"]
kontak2 = ["087987342948", "083416793827"]

while value:
    pilih=home()
    if pilih==1:
        daftar(kontak1,kontak2)
        value = True
    elif pilih==2:
        tambah(kontak1,kontak2)
        print("Kontak Berhasil ditambahkan")
        value=True
    elif pilih==3:
        print("\nProgram selesai, sampai jumpa!")
        print("Semoga harimu menyenangkan!")
        value=False
    else:
        print("\nMenu tidak tersedia")
        value=True