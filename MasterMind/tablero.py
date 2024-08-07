from colored import fg, attr

class Tabla:
    
    #se define la lista de colores para poder manipularlo en el código
    colores_dispo = {
        'r': fg(1),
        'g': fg(2),
        'y': fg(3),
        'b': fg(4)
    }
    
    # el constructor tendrá como inicializador de la clase la lista de colores (color que se intentará adivinar
    # o el que se generará de manera aleatoria) y los turnos (intento y retroalimentación)
    def __init__(self):
        self.contenedor_colores = []
        self.contenedor_turnos = []
    
    # método que tiene como parametro color, luego como argumento se pasará el codigo 
    # del color (generado o aleatorio) 
    def define_color(self, color):
        self.contenedor_colores = color    
    
    # método que comprueba los colores de la retroalimentación. Cada turno genera una retroalimentacion, esta será
    # verde si la posición del turno coincide con  la posición del color del código
    # amarilo si el color se encuentra en el código pero no en la posición correcta
    # blanco si no coincide ni posición ni color
    def comprobar_color_retroalimentacion(self, turnos):
        retro = []
        copia_contenedor_colores = self.contenedor_colores.copy()
        for i in range(4):
            if turnos[i] == copia_contenedor_colores[i]:
                retro.append('color_verde')
                copia_contenedor_colores[i] = None
            elif turnos[i] == copia_contenedor_colores:
                retro.append('color_amarillo')
                copia_contenedor_colores.remove(turnos[i])
            else: retro.append('color_blanco')
            
        return retro
    
# método que permita mostrar la tabla en la consola. Esta tabla va a mostrar los turnos y la retroalimentación.
# se recorre por cada turno y retroalimentación del contenedor de turnos (contiene el turno y la retro) y va a 
# mostrar los colores de las bolitas
    def mostrar_tabla(self):
        for turno, retroalimentacion in self.contenedor_turnos:
            turno_jugado = ' '.join([
                self.colores_dispo[colores] + '⬤' + attr('reset') #Limpia la paleta de colores, para que el siguiente color no se duplique
                for colores in turno
            ])
# si cada adivinanza coincide con el código se moestrarán los colores correspondientes.
            retro_jugado = ' '.join([
                fg(2) + '⬤' + attr('reset') if adivina == 'color_verde'
                else fg(3) + '⬤' + attr('reset') if adivina == 'color_amarillo'
                else '⬤'
                for adivina in retroalimentacion
            ])
            
            print(f'{turno_jugado} --- {retro_jugado}')
            
    
    def actualizar_tabla(self, turno, intento):
        self.contenedor_turnos.append((turno, intento))
    
    