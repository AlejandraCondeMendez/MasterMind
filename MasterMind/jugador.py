import random

class Jugador:
    lista_colores_dispo = ['r', 'g', 'y', 'b']
    def __init__(self, jugador = True):
        self.jugador = jugador

# creador del código: lo puede crear la persona o puede ser generado de manera aleatoria
class Creador(Jugador):
    def creador_codigo(self):
        if self.jugador:
            while True:
                creador_codigo = input('Por favor crea el código secretro, usando los cuatro colores disponibles, ejemplo: r g y b ').strip().split()
                if len(creador_codigo)!=4:
                    print('Por favor no ingresar mas de cuatro colores')
                    continue
                if all(color in self.lista_colores_dispo for color in creador_codigo):
                    break
                else: 
                    print("Uno o más colores no son válidos. Por favor, usa colores válidos separados por espacios.")
                    print("Colores válidos:", self.lista_colores_dispo)
        else:
            creador_codigo = random.choices(self.lista_colores_dispo, k=4)
        
        return creador_codigo
                    

# adivinador del código: el código lo puede adivinar la persona o puede ser generado de manera aleatoria
class Adivinador(Jugador):
    def adivinador_codigo(self):
        if self.jugador:
            while True:
                adivinador_codigo = input('Adivina el código, puedes usar los cuatro colores disponibles, ejemplo: r g y b  ').strip().split()
                if len(adivinador_codigo)!=4:
                    print('Por favor no ingresar mas de cuatro colores  ')
                    continue
                if all(color in self.lista_colores_dispo for color in adivinador_codigo):
                    break
                else: 
                    print("Uno o más colores no son válidos. Por favor, usa colores válidos separados por espacios.")
                
        else:
            adivinador_codigo = random.choices(self.lista_colores_dispo, k=4)
            
        return adivinador_codigo