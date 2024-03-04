n=int(input("ingrese n : "))
cantidad=int(input("Ingrese la cantidad de productos : "))
precios=[]
precio_Total=0
for i in range(cantidad):
    precio=float(input(f"ingrese el precio del producto {i+1} "))
    precios.append(precio)
    precio_Total+=precio
descuento_inicial=0.2
descuento_total=0
for i in precios:
    if i<=n:
        descuento_aplicado=descuento_inicial
    else :
        descuento_aplicado=(descuento_inicial)/(2**i//n)
    descuento_producto=descuento_aplicado*i
    descuento_total+=descuento_producto
precio_final=precio_Total-descuento_total
print(precio_Total)
print(descuento_total)
print(precio_final)
