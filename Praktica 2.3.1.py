a = int(input("Введите число "))
if a == 0:
    print("Нулевое" , end=" ")
if a>0:
    print("Положительное" , end=' ')
elif a<0:
    print("Отрицательное" , end=" ")
if a%2 == 0:
    print("четное число")
else:
    print("нечетное число")