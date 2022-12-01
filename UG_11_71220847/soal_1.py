print ("Select operation.")
print ("1. Add")
print ("2. Subtract")
print ("3. Multiply")
print ("4. devide")

choice = int(input("Enter choice (1/2/3/4): "))
if choice == 1:
    def add():
        first = int(input("Enter first number: "))
        second = int(input("Enter second number: "))
        hasil = (first + second)
        print(first, "+", second, "=", hasil)
    add()
elif choice == 2:
    def Substract():
        first = int(input("Enter first number: "))
        second = int(input("Enter second number: "))
        hasil = (first - second)
        print(first, "-", second, "=", hasil)
    Substract()
elif choice == 3:
    def Multiply():
        first = int(input("Enter first number: "))
        second = int(input("Enter second number: "))
        hasil = (first * second)
        print(first, "*", second, "=", hasil)
    Multiply()
elif choice == 4:
    def Devide():
        first = int(input("Enter first number: "))
        second = int(input("Enter second number: "))
        hasil = (first / second)
        print(first, "/", second, "=", hasil)
    Devide()