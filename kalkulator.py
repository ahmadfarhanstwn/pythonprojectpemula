a = float(input("Masukkan Angka : "))
operator = input("Masukkan Operasi Yang Akan Digunakan : ")
b = float(input("Masukkan Angka : "))

if operator == "+":
    print(a + b)

elif operator == "-":
    print(a - b)

elif operator == "*":
    print(a * b)

elif operator == "/":
    print(a / b)

elif operator == "%":
    print(a % b)

elif operator == "**":
    print(a ** b)

else :
    print("Error")