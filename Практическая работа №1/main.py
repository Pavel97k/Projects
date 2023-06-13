number = input("Введите количество чисел: ")
MAT = input("Введите операцию(+,-,*,/): ")
        
for i in range(int(number)):
    A = int(input("Введите " + str(i+1) + " число: "))
    if i == 0:
        B = A
        continue
    try:
        if MAT == "+":
            B = B + A
        if MAT == "-":
            B = B - A
        if MAT == "*":
            B = B * A
        if MAT == "/":
            B = B / A
            
    except ZeroDivisionError:
        print("Ошибка при расчёте числа!")
print(B) 