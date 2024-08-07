from tablero import Tabla
from jugador import Creador, Adivinador

# Para jugar se necesita la tabla y los jugadores (creador o adivinador)
class Jugar:
    def __init__(self):
        self.tabla = Tabla()
        self.creador_codigo = None
        self.adivinador_codigo = None
# el juego inicia cuando primero se sabe si el jugador va a ser el creador o el adivinador. Si es creador es TRUE
# por lo que el código no se genera de manera aleatoria, pero si es FALSE el código se genera aleatoreamente.    
    def juego_master(self):
        pregunta = input('Bienvenido, ¿deseas ser el jugador o el adivinador del código? pon en la casilla jugador o adivinador: ')
        if pregunta == 'creador':
            self.creador_codigo = Creador(True)
            self.adivinador_codigo = Adivinador(False)
        else:
            self.creador_codigo = Creador(False)
            self.adivinador_codigo = Adivinador(True)
# una vez definido quién es el jugador, se debe generar el código de colores, ya sea por la persona o de manera
# aleatoria, el cual se encuentra en el método creador_codigo de la clase Creador     
        self.tabla.define_color(self.creador_codigo.creador_codigo())
    
    def jugada_turnos(self):
        for turnos in range(12):
            intentos = self.adivinador_codigo.adivinador_codigo()
            retro = self.tabla.comprobar_color_retroalimentacion(intentos)
            self.tabla.actualizar_tabla(intentos, retro)
            self.tabla.mostrar_tabla()
            print(f'Te quedan 11 {turnos}')
            if retro == ['color_verde']*4:
                print('Felicidades, ¡Ganaste!')
                return
        print(f'Lo siento, perdiste la partida. El código era {self.tabla.contenedor_colores}')
            
    def iniciar_juego(self):
        self.juego_master()
        self.jugada_turnos()
    
if __name__ == "__main__":
    juego = Jugar()
    juego.iniciar_juego()
    
    #para que se ejecute en la función principa