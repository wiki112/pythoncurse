'''
x=1

warunek=True
while warunek:
    print(F"{x}")
    while x >5 and x%5==0:
        print("duża liczba!")
        break
    x+=1
    if x > 25:
        break
    pass



for x in range(0,5,1):
    print(f"{x}")




    
for p in range(-9,4,3):
    print(f"{p}")


'''
linie=int(input("podaj liczbę linijek "))

x=1
while x <= int(linie):
    gw= '*'*x
    print(gw)
    x+=1


