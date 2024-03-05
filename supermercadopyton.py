n=int(input("ingrese n : "))
cantidad=int(input("Ingrese la cantidad de productos : "))
precios=[]
precio_Total=0
descuento_inicial=0.2
descuento_total=0
for i in range(cantidad):
    precio=float(input(f"ingrese el precio del producto {i+1} "))
    precios.append(precio)
    precio_Total+=precio
    grupos_completos = (i - 1) // n
    for i,precio in enumerate(precios,1):
        if i <= n:
            descuento_aplicado=descuento_inicial
        else:
            
            descuento_aplicado = descuento_inicial / (2 ** grupos_completos)

    descuento_producto = descuento_aplicado * precio
    descuento_total += descuento_producto
print("Precio total:", precio_Total)
print("Descuento total:", descuento_total)