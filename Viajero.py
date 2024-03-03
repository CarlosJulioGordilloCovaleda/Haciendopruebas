#Un viajero desea saber cuánto tiempo tomó un viaje que realizó. 
#Él tiene la duración en minutos de cada uno de los tramos del viaje.
#Desarrolle un programa que permita ingresar los tiempos de viaje de 
#los tramos y entregue como resultado el tiempo total de viaje en formato horas:minutos.
#El programa deja de pedir tiempos de viaje cuando se ingresa un 0.
tiempos_tramos=[]
Total_Minutos=0
while True:
    tiempo_tramo=int(input("Ingrese el tiempo del tramo recorrido : "))
    if tiempo_tramo==0:
        break
    tiempos_tramos.append(tiempo_tramo)

Total_Minutos=sum(tiempos_tramos)
horas=Total_Minutos//60
minutos= Total_Minutos%60
print()
print(" la duración del tiempo de cada tramo fue el siguiente ")
print()
for i,val in enumerate(tiempos_tramos, start=1):
    print(f"Tiempo de tramo {i} fue de {val} minutos ")
print()
print(f"Tiempo total de viaje: {horas}:{minutos} horas ")