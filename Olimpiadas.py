print("Ejercicio # 3")
print("Sistema de verificador de multiplos")
num1=int(input("Ingrese un número a verificar"))
if num1 %2 and num1%3 and num1%5==0:
    print(f"{num1} es multiplo del 2 del 3 y del 5")
elif num1 %2 and num1%3 ==0:
    print(f"{num1} es multiplo del 2 y del 3")
elif num1 %2 ==0:
    print(f"{num1} es multiplo solamente del 2")
elif num1 %3 ==0:
    print(f"{num1} es multiplo solamente del 3")
elif num1 %5 ==0:
    print(f"{num1} es multiplo solamente del 5")
elif num1 %3 and num1%5 ==0:
    print(f"{num1} es multiplo del 3 y del 5")
elif num1 %2 and num1%5 ==0:
    print(f"{num1} es multiplo del 2 y del 5")
else:
    print("No es posible realizar la verificación")
    
print("Ejercicio # 27")
print("Clasificador de edades con bono")
nomb=input("Ingrese su nombre:")
ed=int(input(f"{nomb} ingrese su edad para saber que tipo de bono tiene:"))
if ed<= 17:
    print(f"{nomb} tienes un bono juvenil")
elif ed >=18 and ed <=59:
    print(f"{nomb} no tienes bono")
else:
    print(f"{nomb} tienes un bono de adulto mayor")

print("Ejercicio # 2")
usuarios=[]
usuarios.append(input("Ingrese un nombre (Ej:camilo):").lower())
usuarios.append(input("Ingrese un nombre (Ej:sara):").lower())
usuarios.append(input("Ingrese un nombre (Ej:luisa):").lower())
dispositivos=[]
dispositivos.append(input("Ingrese un dispositivo (Ej:laptop):").lower())
dispositivos.append(input("Ingrese un dispositivo (Ej:tablet):").lower())
dispositivos.append(input("Ingrese un dispositivo (Ej:smartphone):").lower())

#punto 1
if "luisa" in usuarios[2]:
    usuarios.append("david")
    if "sara" in usuarios[1]: #punto 3
        usuarios.remove("sara")
        if "camilo" in usuarios[0]:          #punto 5
            usuarios.remove("camilo")
            usuarios.append("andres")
            usuarios.remove("luisa")
            usuarios.remove("david")
            usuarios.append("luisa")
            usuarios.append("david")
            soporte_tecnico=[usuarios[0],usuarios[1]]   #punto 6
            if "andres" in soporte_tecnico[0]:            #punto 9
                soporte_tecnico.append("nivel avanzado")
                if "nivel avanzado" in soporte_tecnico[2]:         #punto 10
                    registro_usuario={"nombre":"andres","equipo":"tablet","estado":"activo"}
                    try:                                  #punto 11
                        registro_usuario["último ingreso"]="18/06/2025"
                    except NameError:
                        print("No existe el diccionario registro_usuario")
                        if "sara" in usuarios: #Punto 13
                            print("Ya está en la lista")
                        else:
                            usuarios.append("sara")
else:
    print("No se puede realizar el proceso")
 
#punto 2
if "smartphone" in dispositivos[2]:
    dispositivos.append("smartwatch")
    elem=len(dispositivos)
    if elem>=3:     #punto 4
        dispositivos.remove(dispositivos[0])
        dispositivos_moviles=[dispositivos[1],dispositivos[2]]#punto 7
        if "smartwatch" in dispositivos_moviles[1]:
            nuevo_dispositivo=("smartwatch","disponible")    #punto 8
            if "impresora" in dispositivos:    #punto 12
                print("Ya está en la lista")
            else:
                dispositivos.append("impresora")
else:
    print("No se puede realizar el proceso")
    
print(usuarios)

print(dispositivos)

print(soporte_tecnico)

print(dispositivos_moviles)

print(nuevo_dispositivo)

print(registro_usuario)
