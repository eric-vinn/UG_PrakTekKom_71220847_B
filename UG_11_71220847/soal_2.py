kata = str(input("Masukkan Kata: "))
def funPalindrome():
    if kata == kata[::-1]:
        print ("yes")
        print ("Jika dibalik:",kata[::-1])
    else:
        print ("No")
        print ("Jika dibalik:",kata[::-1])
funPalindrome()