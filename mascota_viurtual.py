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

def obj_mascota(estados, dueno, trucos, nombre_mascota): 
    nombre = {"nombre" : nombre_mascota}

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

def obj_mascota_2(estados, dueno, trucos, nombre_mascota): 
    nombre = {"nombre" : nombre_mascota}

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
        "sueno" : "dormir",
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
    nombre_mascota_2 = input("Ingrese el nombre del gato: ")
    logros = 0
    estados = obj_estado() 
    trucos = obj_trucos(nombre_mascota)
    mascota = obj_mascota(estados["atributos"], nombre, trucos["acciones"], nombre_mascota)
    mascota_2 = obj_mascota_2(estados["atributos"], nombre, trucos["acciones"], nombre_mascota_2)
    juego = input("quieres empezar: ") 
    while juego == "si":
         
        nuevo_estado_1 = seleccionar_estado(mascota["atributos"]["estado"]) 
        print(f"El estado del perro es este: {nuevo_estado_1} \n Desea: alimentarla, dormir o darle de tomar ?") 
        accion_1 = input("Ingrese la accion: ") 
        estado_de_mascota_1 = estado_actual(accion_1, estados, nuevo_estado_1) 
        print(f"El estado de tu perro es: {estado_de_mascota_1}") 
        
        if estado_de_mascota_1 == estados["atributos"]["mejora"]:
            truco_1 = seleccionar_truco(trucos["acciones"])
            logros += 1
            print(f"¡Conseguiste un logro! \n Asi que tu perro festejo haciendo un truco: {truco_1}")
            
        nuevo_estado_2 = seleccionar_estado(mascota_2["atributos"]["estado"])
        print(f"El estado del gato es este: {nuevo_estado_2} \n Desea: alimentarla, dormir o darle de tomar ?")
        accion_2 = input("Ingrese la accion: ")  
        estado_de_mascota_2 = estado_actual(accion_2, estados, nuevo_estado_2) 
        print(f"El estado de tu gato es: {estado_de_mascota_2}") 
        
        if estado_de_mascota_2 == estados["atributos"]["mejora"]:
            truco_2 = seleccionar_truco(trucos["acciones"])
            logros += 1
            print(f"¡Conseguiste un logro! \n Asi que tu gato festejo haciendo un truco: {truco_2}")

        
        if estado_de_mascota_2 == "Insatisfecho" and estado_de_mascota_1 == "Insatisfecho":
            print(f"{nombre_mascota} esta peleando contra {nombre_mascota_2}")
            
        elif estado_de_mascota_1 == "Insatisfecho" or estado_de_mascota_2 == "Insatisfecho":
            print(f"{nombre_mascota} esta peleando contra {nombre_mascota_2}")
            
        juego = input("Quieres continuar: ")
        
    print(f"Tu cantidad de logros fue de: {logros}")

main()