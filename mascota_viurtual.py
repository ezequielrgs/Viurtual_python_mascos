import random

""" mascota: nombre:str, trucos:int | str, dueño & estado: function (dict), { feliz:bool | int triste: bool | int hambriento: bool | int } <- podemos llevar a cabo los comportamientos.

+----------------------------+
|        Usuario             |
+----------------------------+
|           -Nombre          |
|           -Mascota         |
|           -LogrosMascota   |
+----------------------------+
|           -Premiar         |
|           -Alimentar       |
|           -Jugar           |
+----------------------------+



+----------------------------+
|          Mascota           |
+----------------------------+
|           -Nombre          |
|           -Estado          |
|           -Trucos          |
|           -Dueño           |
+----------------------------+
|        -Alimentar          |
|        -Jugar              |
|        -Dormir             |
+----------------------------+

+----------------------------+
|          Estado            |
+----------------------------+
|                            |
|           -Hambre          |
|           -Sueño           |
|           -Sed             |
|           -Felicidad       |
+----------------------------+
|                            |
|        -Alimentar          |
|        -Jugar              |
+----------------------------+
"""

def obj_mascota(estados, dueno, trucos): 
    nombre = {"nombre" : "Pepa"}

    atributos = {
        "nombre" : nombre["nombre"],
        "estado" : estados,
        "trucos" : trucos,
        "duenio" : dueno
    }

    acciones = {
        "ac" : "alimentar",
        "ac1" : "jugar",
        "ac2" : "dormir"  
    }

    objeto_mascota = {
        "nombre" : nombre,
        "atributos" : atributos,
        "acciones" : acciones
    }

    return objeto_mascota

#-----------------------------------------------------------------------

def obj_estado()-> dict: 
    nombre = {"nombre" : "Estados"}

    atributos = {
        "hambre" : "hambre",
        "sueno" : "sueno",
        "sed" : "sed",
        "mejora" : "felicidad"
    }

    acciones = {
        "hambre" : "alimentarla",
        "sueno" : "dormirla",
        "sed" : "darle de tomar"
    }

    objeto_estado = {
        "nombre" : nombre,
        "atributos" : atributos,
        "acciones" : acciones
    }

    return objeto_estado

#------------------------------------------------------------------------

def obj_trucos(mascota):

    nombre = {"nombre" : "trucos"}

    atributos = {
        "nombre mascota" : mascota,  
        "trucos aprendidos" : 3, 
    }


    acciones = {  
        "ac1" : "dar la pata", 
        "ac2" : "saltar",  
        "ac3" : "boltereta"
    }


    objeto_trucos = {
        "nombre" : nombre,  
        "atributos" : atributos,  
        "acciones" : acciones  
    }

    return objeto_trucos

#---------------------------------------------------------------------------------

def seleccionar_truco(trucos):
    valores_trucos = list(trucos.values()) 
    return random.choice(valores_trucos)


def seleccionar_estado(estados):
    estados_validos = [k for k in estados.keys() if k != "mejora"]
    return random.choice(estados_validos)


def estado_actual(accion, estados, nuevo_estado): 

    if nuevo_estado == estados["atributos"]["hambre"]: 
        if accion == estados["acciones"]["hambre"]: 
            estado_mascota = estados["atributos"]["mejora"] 
        else: 
            estado_mascota = "Insatisfecho"

    elif nuevo_estado == estados["atributos"]["sueno"]:
        if accion == estados["acciones"]["sueno"]: 
            estado_mascota = estados["atributos"]["mejora"]
        else:
            estado_mascota = "Insatisfecho"
        
    elif nuevo_estado == estados["atributos"]["sed"]:
        if accion == estados["acciones"]["sed"]:
            estado_mascota = estados["atributos"]["mejora"]
        else:
            estado_mascota = "Insatisfecho"
        
    elif nuevo_estado == estados["atributos"]["mejora"]:
        estado_mascota = estados["atributos"]["mejora"]
    
    return estado_mascota


def main(): 
    nombre = input("Ingrese su nombre: ")
    nombre_mascota = input("Ingrese el nombre del perro: ")
    logros = 0
    estados = obj_estado() 
    trucos = obj_trucos(nombre_mascota)
    mascota = obj_mascota(estados["atributos"], nombre, trucos["acciones"])
    juego = input("quieres empezar: ") 
    while juego == "si": 
        nuevo_estado = seleccionar_estado(mascota["atributos"]["estado"]) 
        print(f"El estado del bicho es este: {nuevo_estado} \n Desea: alimentarla, dormir o darle de tomar ?") 
        accion = input("Ingrese la accion: ") 
        estado_de_mascota = estado_actual(accion, estados, nuevo_estado) 
        print(f"El estado de tu mascota es: {estado_de_mascota}") 
        if estado_de_mascota == estados["atributos"]["mejora"]:
            truco = seleccionar_truco(trucos["acciones"])
            logros += 1
            print(f"¡Conseguiste un logro! \n Asi que tu perro festejo haciendo un truco: {truco}")
        juego = input("Quieres continuar: ")
    print(f"Tu cantidad de logros fue de: {logros}")

main()