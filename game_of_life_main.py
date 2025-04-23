################################################################################
#                                                                              #
#                    Coded by Roberto (Tank3) Cruz Lozano                      #
#                     Refactored for clarity and config                        #
#                                                                              #
################################################################################

################################################################################
#                               MODULES
import tkinter as tk
from game_of_life_interface import GameOfLifeInterface
from game_of_life_class import GameOfLifeClass
from game_of_life_config import UPDATE_INTERVAL_MS # Importar intervalo

################################################################################
#                                 MAIN

def main():
    """Función principal para iniciar la aplicación."""
    root = tk.Tk()
    app_interface = GameOfLifeInterface(root) # Crea la interfaz
    game_logic = GameOfLifeClass(app_interface) # Crea la lógica, pasando la interfaz

    # Configura los eventos (botones, clics) conectando lógica e interfaz
    game_logic.setup_events()

    # Inicia el bucle del juego usando el intervalo de la configuración
    # Se llama a run_game_loop una vez para empezar el ciclo con root.after
    root.after(UPDATE_INTERVAL_MS, game_logic.run_game_loop)

    # Inicia el bucle principal de Tkinter
    root.mainloop()

if __name__ == '__main__':
    main()