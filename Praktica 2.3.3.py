Mikl = int (input("Сколько долларов есть у Майкла - "))
Ivan = int (input("Сколько долларов есть у Ивана - "))
Invest = int (input("Минимиальная сумма инвестиций - "))
if (Mikl>= Invest) and (Ivan >= Invest):
    print(2)
elif (Mikl>=Invest) and (Ivan<Invest):
    print("Mikl")
elif (Mikl<Invest) and (Ivan>=Invest):
    print("Ivan")
elif (Mikl<Invest) and (Ivan<Invest) and (Mikl+Ivan>=Invest):
    print(1)
elif (Mikl<Invest) and (Ivan<Invest) and (Mikl+Ivan<Invest):
    print(0)

