from colored import fg, attr
from tablero import Tabla

def main():
    tablero = Tabla()
    
    tablero.define_color(["r", "g", "y", "b"])
    
    tablero.actualizar_tabla(["r", "g", "y", "b"], ["color_verde", "color_verde", "color_verde", "color_verde"])
    tablero.actualizar_tabla(["r", "r", "g", "y"], ["color_verde", "color_amarillo", "color_blanco", "color_blanco"])
    tablero.actualizar_tabla(["g", "y", "b", "r"], ["color_amarillo", "color_amarillo", "color_blanco", "color_blanco"])
    
    tablero.mostrar_tabla()

if __name__ == "__main__":
    main()