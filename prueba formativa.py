import os
import time
cls="cls"
op=1
subtotal= 0
contador1=0
cotador2=0
contador3=0
contador4=0
while op <= 4:
    print("menu")
    print("1.Pikachu Roll $4500")
    print("2. Otaku Roll $5000")
    print("3. Pulpo Venenoso Roll $5200")
    print("4. Anguila Eléctrica Roll $4800")
    print("5.salir del menu")
    try:
        op=int(input("Selecciona una opcion: "))
    except ValueError:
        print("Ingresa un numero del 1-4")
        continue
    if op == 1:
        subtotal = (subtotal+4500)
        contador1 +=1
        print(f"elegiste la opcion pikachu roll")
    elif op == 2:
        subtotal= (subtotal+5000)
        contador2 +=1
        print(f"eligiste la opcion otaku roll")
    elif op ==3:
        subtotal= (subtotal+5200)
        contador3 +=1
        print("eligiste la opcion Pulpo Venenoso Roll")
    elif op ==4:
        subtotal=(subtotal+4800)
        contador4 +=1
        print("eligiste la opcion Anguila Eléctrica Roll")
    elif op==5:
        break
os.system("cls")

print(f"cantidad total de Pikachu Rolls = {contador1}")
