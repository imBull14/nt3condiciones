nombreUsuario=input(("Ingrese su nombre: "))
edadUsuario=int(input("Ingrese su edad: "))

if edadUsuario>=0 and edadUsuario <=15:
    print(f"Apreciado {nombreUsuario} usted es menor de edad")
elif edadUsuario>15 and edadUsuario<=28:
    print(f"Apreciado {nombreUsuario} usted es un Joven")
elif edadUsuario>28 and edadUsuario<=60:
    print(f"Apreciado {nombreUsuario} usted es un Adulto")
elif edadUsuario>60 and edadUsuario<110:
    print(f"Apreciado {nombreUsuario} usted es un Adulto Mayor")
else:
    print ("Error, no se reconoce la edad ingresada")

