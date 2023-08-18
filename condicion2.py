temperatura = int(input("Digita la temperatura: "))
gradosAlcohol = int(input("Digita los grados de alcohol: "))

if temperatura>50 or gradosAlcohol>5:  #Utilizar And(y) , Or(o) 
    print("ALARMA")
else:
    print("NORMAL")