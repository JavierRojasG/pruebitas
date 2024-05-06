## javier rojas guerrero ##
### prueba 2 ###

import math

def imprimir_tabla_datos(): #se imprime aca la tabla de datos #
    print("Tabla de datos:")
    print("Artefacto | Consumo Diario x persona")
    print("---------------------------------------------------------")
    print("||  Hervidor || 5.9") 
    print("||  Microondas 800 watts || 0.8")
    print("||  Refrigerador Clase A || 7.6 (*)")
    print("||  Aspiradora || 7.0")
    print("||  Secador de pelo || 4.5")
    print("||  Lavadora/Secadora || 2.1")
    print("---------------------------------------------------------\n")


def calcular_consumo_semanal():
    consumo_diario = {
        "Hervidor": 5.9,
        "Microondas 800 watts": 0.8,
        "Refrigerador Clase A": 7.6,
        "Aspiradora 1400W": 7.0,
        "Secador de pelo 1800W": 4.5,
        "Lavadora/Secadora": 2.1
    }
    
    imprimir_tabla_datos()
    
    # aca se solicitaran los miembros, la cantidad para empezar a calcular, ademas que no dejara ingresar letras sino números #
    while True:
        try:
            num_integrantes = int(input("Ingrese el número de integrantes del grupo familiar, mínimo 1 máximo 5: "))
            if num_integrantes < 1 or num_integrantes > 5:
                print("El número de integrantes debe estar entre 1 y 5. Inténtelo de nuevo por favor.")
            else:
                break
        except ValueError:
            print("Por favor, ingrese un número válido.")
            return
    
    consumo_integrantes = []
    
    # calcularemos el consumo semanal de cada integrante #
    for i in range(num_integrantes):
        consumo_persona = 0
        print(f"Integrante {i+1}:")
        for artefacto, consumo_diario_persona in consumo_diario.items():
            #se solicita la cantidad de veces que se usa el artefacto x dia, maximo 3 veces como dice el ejercicio. #
            uso_diario = int(input(f"Número de veces que utiliza {artefacto} por día. maximo 3: "))
            if uso_diario < 0 or uso_diario > 3:
                print("El número de veces debe estar entre 0 y 3.")
                return
            consumo_persona += uso_diario * consumo_diario_persona
        consumo_integrantes.append(consumo_persona) ## usado para enlistar cosas a la lista de consumo integrantes ##
    
    #### se calculara el consumo total! ademas se redondeará para que no de valores largos. ##
    consumo_semanal_total = sum(consumo_integrantes)
    round(consumo_semanal_total)
    
    ### Se mostrará el consuom total ##
    print(f"\nEl consum semanal total del grupo familiar es: {consumo_semanal_total} kilowats")

calcular_consumo_semanal() ## imprimir programa al final con todo lo anterior hecho y definido x el orden. ##
