"""
Juego del Ahorcado
==================

Práctica de programación que evalúa:
- Variables y tipos de datos primitivos
- Sentencias condicionales
- Sentencias iterativas
- Manipulación de strings

Autor: [Daniel Felipe Oliveros Rojas]
Fecha: [7/11/2025]
"""


import random


def limpiar_pantalla():    
    """
    Imprime varias líneas en blanco para 'limpiar' la consola
    y que el jugador 2 no vea la palabra introducida
    """
    print(  "\n" * 50)
    print("Limpiando pantalla...")



def solicitar_palabra()->str:
    """
    Solicita una palabra al jugador 1
    La palabra debe tener mínimo 5 caracteres y solo contener letras
    
    Returns:
        str: La palabra a adivinar en mayúsculas
    """

    # TODO: Implementar la función
    # - Usar un bucle while para repetir hasta que la palabra sea válida N/A
    # - Verificar que tenga al menos 5 caracteres (len())  N/A
    # - Verificar que solo contenga letras (isalpha()) N/A 
    # - Convertir a mayúsculas (upper()) ---->  Completo

    palabras = [
        "python", "variable"
    ]

    palabra = random.choice(palabras)

    palabra =palabra.upper()

    return palabra


def solicitar_letra(letras_usadas:list)->str:
    """
    Solicita una letra al jugador 2
    La letra debe ser válida (solo una letra) y no estar ya usada
    
    Args:
        letras_usadas (list): Lista de letras ya introducidas
        
    Returns:
        str: La letra introducida en mayúsculas
    """
    # TODO: Implementar la función
    # - Usar un bucle while para repetir hasta que la letra sea válida ---->  Completado 
    # - Verificar que sea solo un carácter (len() == 1) ----> Completado 
    # - Verificar que sea una letra (isalpha()) ---->  Completado 
    # - Verificar que no esté en letras_usadas (operador 'in')   
    # - Convertir a mayúsculas (upper()) ---->  Completado 
    
    letra = input("Escribe un una sola letra: ")

    while not letra.isalpha() or len(letra) > 1 or letra.upper() in letras_usadas:
            letra = input("Escribe un UNA SOLA LETRA POR FAVOR: ")

    letra = letra.upper()

    return letra



def mostrar_estado(palabra_oculta, intentos, letras_usadas):
    """
    Muestra el estado actual del juego
    
    Args:
        palabra_oculta (str): La palabra con _ y letras adivinadas
        intentos (int): Número de intentos restantes
        letras_usadas (list): Lista de letras ya usadas
    """
    # TODO: Implementar la función
    # - Imprimir intentos restantes
    # - Imprimir la palabra con espacios entre caracteres
    # - Imprimir las letras usadas
    
    print(f"Intentos restantes: {intentos}")
    
    
    print(palabra_oculta) 
    

    for i in letras_usadas:
        print(f"{i}, ") 




def actualizar_palabra_oculta(palabra, palabra_oculta, letra):
    """
    Actualiza la palabra oculta revelando las apariciones de la letra

    Args:
        palabra (str): La palabra completa a adivinar
        palabra_oculta (str): La palabra actual con _ y letras adivinadas
        letra (str): La letra que se ha adivinado
        
    Returns:
        str: La palabra oculta actualizada
    """
    # TODO: Implementar la función
    # - Recorrer la palabra original con un bucle for
    # - Usar enumerate() para obtener índice y carácter
    # - Si el carácter coincide con la letra, reemplazar en palabra_oculta
    # - Puedes convertir palabra_oculta a lista, modificar y volver a string

    
    palabra_oculta = list(palabra_oculta)

    for indice, caracter in enumerate(palabra):
        if caracter == letra:
            palabra_oculta[indice] = letra
            print(palabra_oculta)

    
    return "".join(palabra_oculta)


def jugar():
    """
    Función principal que ejecuta el juego del ahorcado
    """
    print("=== JUEGO DEL AHORCADO ===\n")
    
    # Configuración inicial
    INTENTOS_MAXIMOS = 5

    # TODO: Solicitar la palabra al jugador 1
    # palabra = solicitar_palabra() ----> 
    
    palabra = solicitar_palabra()

    # TODO: Limpiar la pantalla para que el jugador 2 no vea la palabra
    # limpiar_pantalla()
    limpiar_pantalla()  

    
    # TODO: Inicializar variables del juego
    # - palabra_oculta: string con guiones bajos (ej: "_ _ _ _ _")
    # - intentos: número de intentos restantes
    # - letras_usadas: lista vacía
    # - juego_terminado: False
    
    palabra_oculta = "_" * len(palabra)


    letras_usadas = []
    
    juego_terminado = False
    
    
    print("Jugador 2: ¡Adivina la palabra!\n")
    
    # TODO: Bucle principal del juego
    # - Mientras haya intentos y el juego no haya terminado:
    #   1. Mostrar el estado actual
    #   2. Solicitar una letra
    #   3. Añadir la letra a letras_usadas
    #   4. Si la letra está en la palabra:
    #      - Actualizar palabra_oculta
    #      - Mostrar mensaje de acierto
    #      - Si ya no hay '_' en palabra_oculta, el jugador ha ganado
    #   5. Si la letra NO está en la palabra:
    #      - Restar un intento
    #      - Mostrar mensaje de fallo
    
    while INTENTOS_MAXIMOS > 0 and juego_terminado == False :

        mostrar_estado(palabra_oculta, INTENTOS_MAXIMOS,letras_usadas)

        letra = solicitar_letra(letras_usadas)

        letras_usadas.append(f"{letra}" )


        palabra_oculta = actualizar_palabra_oculta(palabra, palabra_oculta,letra)

        if letra not in palabra:
            INTENTOS_MAXIMOS -= 1
            print("La letra no está en la palabra")

    
    # TODO: Mostrar mensaje final
    # - Si ganó: mostrar felicitación y la palabra
    # - Si perdió: mostrar mensaje de derrota y la palabra correcta

    if palabra == palabra_oculta :
        print("Ganaste")
    else:
        print(f"perdiste la palbra era {palabra}")
        

def main():
    """
    Punto de entrada del programa
    """
    jugar()
    
    # TODO (Opcional): Preguntar si quiere jugar otra vez
    jugar_otra_vez = input("\n¿Quieres jugar otra vez? (s/n): ")
    if jugar_otra_vez.lower() == 's':
        main()
    


if __name__ == "__main__":
    main()
