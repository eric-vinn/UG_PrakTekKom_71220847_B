print("SELAMAT DATANG DI PROGRAM PEMBUAT PIRAMIDA BERLUBANG")
x = int(input("Masukkan Angka : "))
print("")
print(' '*(x-1),"*")
for y in range ((x-1),1,-1):
    print(' '*(y-1),"**")
print ("**"*x)