# game_of_life_config.py

# --- Dimensiones del Tablero ---
BOARD_WIDTH_CELLS = 25  # Ancho del tablero en celdas
BOARD_HEIGHT_CELLS = 25 # Alto del tablero en celdas
CELL_SIZE_PX = 20       # Tamaño de cada celda en píxeles

# --- Tiempos ---
UPDATE_INTERVAL_MS = 125 # Intervalo de actualización del juego en milisegundos

# --- Colores ---
# Paleta (Ejemplo: tonos azules y grises)
COLOR_BACKGROUND = "#22232D"      # Fondo general de la ventana
COLOR_CANVAS_BG = "#666B8A"       # Fondo del lienzo (celdas muertas inicial)
COLOR_GRID = "#FFFFFF"           # Color de las líneas de la cuadrícula
COLOR_ALIVE = "#ADD8E6"           # Color para celdas vivas (Light Blue)
COLOR_DEAD = COLOR_CANVAS_BG      # Color para celdas muertas (igual al fondo del canvas)
COLOR_TEXT = "#FFFFFF"           # Color del texto principal
COLOR_INFO_TEXT = "#FFFFFF"      # Color del texto de información inferior
COLOR_BUTTON_TEXT = "#121212"     # Color del texto en los botones

# Colores específicos de botones
COLOR_BTN_START = "#6CD987"
COLOR_BTN_STOP = "#D977B7"
COLOR_BTN_CLEAN = "#837ACC"
COLOR_BTN_EXIT = "#D3A16B"

# --- Textos ---
WINDOW_TITLE = "Game of Life (v1.02 - Refactored)"
MAIN_TITLE = "Game of Life"
INFO_TEXT_LEFT = "Coded by Tank3"
INFO_TEXT_RIGHT = "v1.02"

# --- Icono ---
ICON_PATH = "./img/Glider.ico" # Asegúrate que la ruta sea correcta

# --- Cálculos derivados ---
CANVAS_WIDTH = BOARD_WIDTH_CELLS * CELL_SIZE_PX
CANVAS_HEIGHT = BOARD_HEIGHT_CELLS * CELL_SIZE_PX
WINDOW_WIDTH = CANVAS_WIDTH + 100 # Ajusta según necesidad (espacio para bordes/info)
WINDOW_HEIGHT = CANVAS_HEIGHT + 150 # Ajusta según necesidad (espacio para título/botones/info)

# --- Estructura de Celda ---
from collections import namedtuple
# id: Identificador único (opcional, podría quitarse si no se usa)
# x1, y1, x2, y2: Coordenadas en píxeles del rectángulo en el canvas
# is_alive: Estado actual (True si viva, False si muerta)
# next_state: Estado calculado para la siguiente generación
# canvas_rect_id: ID del objeto rectángulo principal en el canvas (para cambiar color)
# canvas_inner_rect_id: ID del objeto rectángulo interior (si se usa un diseño de 2 rectángulos)
Cell = namedtuple("Cell", ["id", "x1", "y1", "x2", "y2", "is_alive", "next_state", "canvas_rect_id", "canvas_inner_rect_id"])