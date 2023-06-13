import sys
ves = False

Year = int(input("Введите дату (0000): "))
if Year < 2000:
    print("\nГод должен быть тысячным (0000)")
    sys.exit () 
if Year % 4 == 0:
        ves = True
        print("Год весокосный")
Month = 12
Result = 0
v = False
Prime = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'] 
for j in range(int(Month)):
    for i in (Prime):
        if ves == True:
            if(j == 0 or j == 2 or j == 4 or j == 6 or j == 7 or j == 9 or j == 11):
                One = int(i[0])
                Two = int(i[1])
                Result += One + Two
        if ves == False:
            if(j == 0 or j == 2 or j == 4 or j == 6 or j == 7 or j == 9 or j == 11):
                One = int(i[0])
                Two = int(i[1])
                Result += One + Two

Prime.remove(Prime[30])
for j in range(int(Month)):
    for i in (Prime):
        if ves == True:
            if(j == 3 or j == 5 or j == 8 or j == 10):
                One = int(i[0])
                Two = int(i[1])
                Result += One + Two
        if ves == False:
            if(j == 3 or j == 5 or j == 8 or j == 10):
                One = int(i[0])
                Two = int(i[1])
                Result += One + Two

Prime.remove(Prime[29])
for j in range(int(Month)):
    for i in (Prime):
        if ves == True:
            if(j == 1):
                One = int(i[0])
                Two = int(i[1])
                Result += One + Two
        if ves == False:
            if(v == False):
                v = True
                Prime.remove(Prime[28])
            if(j == 1):
                One = int(i[0])
                Two = int(i[1])
                Result += One + Two   
print(f"{Result}") 