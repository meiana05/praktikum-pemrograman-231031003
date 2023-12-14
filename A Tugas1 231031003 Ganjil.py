#Tugas 1 : Buat program
#a. Input bilangan X
#b. Cek : jika ganjil maka cetak (“X adalah bilangan Ganjil ”)
#c. Jika tidak Maka cetak (“X adalah bilangan Bukan Ganjil”)
#d. Selesai

print(f'Tugas 1 : Buat Program')
print() 

x = int(input('Masukkan Nilai: '))
if x % 2 != 0 :
    print(f"{x} adalah bilangan ganjil")
else:
    print(f"{x} adalah bilangan bukan ganjil")

print(f"Selesai")
print()