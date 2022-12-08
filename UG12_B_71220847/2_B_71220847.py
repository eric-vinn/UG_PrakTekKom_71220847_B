print("~~~ Selamat Datang di Kalkulator Sederhana ~~~")
x = input("Masukkan operator matematika yang ingin Anda hitung: ")
while True:
    if x == '+':
        va1 = int(input('Mau penjumlahan berapa: '))
        var2 = int(input('Print berapa banyak: '))
        for i in range(var2):
            print(f'{i+1} + {var2-i} = {(i+1)+(var2-i)}')
    elif x == '-':
        var1 = int(input('Mau pengurangan berapa: '))
        var2 = int(input('Print berapa banyak: '))
        for i in range(var2):
            print(f'{i+1} + {var2-i} = {(i+1)-(var2-i)}')
    elif x in ('*'):
        var1 = int(input('Mau perkalian berapa: '))
        var2 = int(input('Print berapa banyak: '))
        for i in range(var2):
            print(f'{i+1} X {var2-i} = {(i+1)*(var2-i)}')
    elif x == ':':
        var1 = int(input('Mau pembagian berapa: '))
        var2 = int(input('Print berapa banyak: '))
        for i in range(var2):
            print(f'{i+1} : {var2-i} = {(i+1)/(var2-i)}')
    else:
        print('Terjadi kesalahan')
        break
    y = input('Apakah Anda Ingin Menghitung Lagi? (Y/T): ')
    if y in ('T'):
        print('Terima Kasih dan Sampai Jumpa Lagi!')
        break
    elif y in ('Y'):
        continue
    else:
        print('ERROR\nPilih Y atau T\nUlangi Program')
        break