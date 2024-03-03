# Votaciones de la CONFECH¶
# Este problema apareció en el certamen 1 del segundo semestre de 2011 en el campus Vitacura.
# La CONFECH, en su afán de agilizar el proceso de recuento de las votaciones, 
# le ha encargado el desarrollo de un programa de registro de votación por universidades.
# Primero, el programa debe solicitar al usuario ingresar la cantidad de universidades 
# que participan en el proceso.Luego, para cada una de las universidades, el usuario debe 
# ingresar el nombre de la universidad y los votos de sus alumnos, 
# que pueden ser: aceptar (A), rechazar (R), nulo (N) o blanco (B). El término de la votación 
# se indica ingresando una X, tras lo cual se debe mostrar los totales de votos de la universidad,
# con el formato que se muestra en el ejemplo.Finalmente, el programa debe mostrar el resultado de la votación,
# indicando la cantidad de universidades que aceptan, que rechazan y en las que hubo empate entre estas dos opciones.

n_Universidades=int(input("Ingrese el numero de universidades : "))
universidades=[]
aceptan=0
rechazan=0
empate=0
for i in range(n_Universidades):
    nombre_U=input(f'Ingrese el nombre de la universidad numero {i+1} : ')

    aceptar=0
    rechazar=0
    nulo=0
    blanco=0
    lista_votos=[]
    while True:
        voto=input(f'Ingrese el voto de un alumno de la Universidad {nombre_U} (A para aceptar, R para rechazar, N para nulo, B para blanco, X para terminar):').lower()
        if voto=="a":
            aceptar+=1
        elif voto=="r":
            rechazar+=1
        elif voto=="n":
            nulo+=1
        elif voto=="b":
            blanco+=1
        elif voto=="x":
            break
        else:
            print("voto no valido. intente de nuevo")
        lista_votos.append(voto)
    
    universidades.append({
        "nombre":nombre_U,
        "aceptar":aceptar,
        "rechazar":rechazar,
        "nulo":nulo,
        "blanco":blanco,
        "votos":lista_votos
    })

    if aceptar>rechazar:
        aceptan+=1
    elif rechazar>aceptar:
        rechazan+=1
    else:
        empate+=1

print(f'Numero de universidades: {n_Universidades}')
print()

for universidad in universidades:
    print(f'Universidad: {universidad["nombre"]}')
    print()
    for i in universidad["votos"]:
        print(f'Voto:{i}')
    print(f'{universidad["nombre"]} : {universidad["aceptar"]} aceptan, {universidad["rechazar"]} rechazan, {universidad["nulo"]} nulos,{universidad["blanco"]} blancos')
    print()

print(f'Universidades que aceptan: {aceptan}')
print(f'Universidades que rechazan: {rechazan}')
print(f'Universidades con empate: {empate}')


    
            
