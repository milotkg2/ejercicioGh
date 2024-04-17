print("Bienvenido al mundo de la programación")
print("Para comenzar, ingresa tu nombre")

nom = (input())
print(f"Bienvenido {nom}")

x = int(input("ingrese un valor para X de la siguiente ecuacion ((x**2)+(3*x)+1)/4"))
solucion =((x**2)+(3*x)+1)/4

print(f"el resultado de la ecuacion es {solucion}")

nombre = input("ingrese su nombre")
rut = input("ingrese su rut")
correo = input("ingrese su correo")
telefono = input("ingresesu telefono")

print(f"NOMBRE:\t\t{nombre.upper}\nRUT:\t\t{rut}\nCORREO:\t\t{correo.upper}\nTELEFONO:\t\t{telefono}")




import os
import time
os.system("cls")

cantidad = int(input("ingrese cantidad de notas "))
contadorNota = 0
for x in range(cantidad):
    nota = float(input(f"ingrese nota {x+1}\n"))
    contadorNota = contadorNota+nota
    print(f"de momento llevo sumado {contadorNota}")
    time.sleep(4)
    promedio = contadorNota/cantidad    
print(f"segun la {cantidad} de notas, tu promedio es {promedio}")



totalIngresos=0
x=True
while x:
    try:
        pasajes=int(input("cuántos pasajes deseas vender\n"))
        if pasajes>0:
            x=False
        else:
           print("solo numeros enteros positivo") 
    except:
        print("solo numeros enteros positivo")
    
for x in range(pasajes): 
    try:
        precio=int(input(f"ingrese el precio del pasajes {x+1}\n"))
        totalIngresos=totalIngresos+precio
    except:
        print("only lukas men...")
        break

if totalIngresos>0:        
    print(f"para {pasajes} pasajes, el valor a pagar es: ${totalIngresos}")

