import random as rm
import string as str
from palabras import palabras
from hangman_visual import vidas_diccionario_visual

'''Juego del Ahorcado'''

def obtener_palabra(palabras):
    #Seleccionar una palabra de la lista al azar
    palabra = rm.choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = rm.choice(palabras)

    return palabra.upper()

def hangman():
    print('=====================================')
    print('= Bienvenid@ al juego del Ahorcado! =')
    print('=====================================')

    palabra = obtener_palabra(palabras)

    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(str.ascii_uppercase)

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")

        #Mostrar el estado de la palabra
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        print(vidas_diccionario_visual[vidas])
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input('Escoge una letra: ').upper()

        '''La letra del usuario se suma si esta en el abecedario y no esta en el conjunto de letras ya ingresadas'''
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            # Consulto si la letra esta en la palabra la quita de las que faltan adivinar, sino quita una vida
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas -= 1
                print(f'\n Tu letra, {letra_usuario} no esta en la palabra.')
        
        #Si repite una letra
        elif letra_usuario in letras_adivinadas:
            print('\nYa elegiste esa letra. Elige otra por favor.')
        else:
            print('\n Esta letra no es valida.')

    #Cuando se adivina la letra o se queda sin vidas.
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f'Ahorcado! Perdiste. La palabra era: {palabra}')
    else:
        print(f'Ganaste!, adivinaste la palabra {palabra}.')

hangman()