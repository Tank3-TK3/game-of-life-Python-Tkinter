################################################################################
#                                                                              #
#                    Coded by Roberto (Tank3) Cruz Lozano                      #
#                     Refactored for clarity and config                        #
#                                                                              #
################################################################################

################################################################################
#                               MODULES
import tkinter as tk
from tkinter import font
# Importar configuraciones
from game_of_life_config import (
    BOARD_WIDTH_CELLS, BOARD_HEIGHT_CELLS, CELL_SIZE_PX,
    CANVAS_WIDTH, CANVAS_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, UPDATE_INTERVAL_MS,
    COLOR_BACKGROUND, COLOR_CANVAS_BG, COLOR_GRID, COLOR_ALIVE, COLOR_DEAD,
    COLOR_TEXT, COLOR_INFO_TEXT, COLOR_BUTTON_TEXT,
    COLOR_BTN_START, COLOR_BTN_STOP, COLOR_BTN_CLEAN, COLOR_BTN_EXIT,
    WINDOW_TITLE, MAIN_TITLE, INFO_TEXT_LEFT, INFO_TEXT_RIGHT, ICON_PATH
)

################################################################################
#                                CLASS

class GameOfLifeInterface(tk.Frame):
    """
    Crea y gestiona la interfaz gráfica de usuario (GUI) para el Juego de la Vida.
    """
    def __init__(self, root=None):
        """
        Inicializa la interfaz gráfica.

        Args:
            root: La ventana raíz de Tkinter. Si es None, se crea una nueva.
        """
        if root is None:
            root = tk.Tk()
        super().__init__(root) # Inicializa tk.Frame

        self.root = root
        self.update_interval = UPDATE_INTERVAL_MS
        self._configure_root()
        self._setup_fonts()
        self._create_widgets()

    def _configure_root(self):
        """Configura la ventana principal."""
        self.root.title(WINDOW_TITLE)
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+50+50")
        try:
            self.root.iconbitmap(ICON_PATH)
        except tk.TclError:
            print(f"Warning: Icono '{ICON_PATH}' no encontrado o formato inválido.")
        self.root.config(background=COLOR_BACKGROUND)
        self.root.resizable(width=False, height=False)

    def _setup_fonts(self):
        """Define las fuentes a utilizar."""
        self.font_titles = font.Font(family="Arial", size=25)
        self.font_text = font.Font(family="Arial", size=15)
        self.font_info = font.Font(family="Arial", size=10) # Fuente más pequeña para info

    def _create_widgets(self):
        """Crea todos los componentes (widgets) de la interfaz."""
        # Frame principal que contendrá todo
        self.main_frame = tk.Frame(self.root, background=COLOR_BACKGROUND)
        self.main_frame.pack(fill='both', expand=True)

        # Título
        self.label_title = tk.Label(self.main_frame, text=MAIN_TITLE,
                                    font=self.font_titles,
                                    foreground=COLOR_TEXT, background=COLOR_BACKGROUND)
        self.label_title.pack(pady=10)

        # Frame para el tablero (canvas)
        self.board_frame = tk.Frame(self.main_frame, background=COLOR_BACKGROUND,
                                   width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bd=0)
        self.board_frame.pack_propagate(0)
        self.board_frame.pack(pady=5)

        # Canvas (tablero)
        self.canvas_board = tk.Canvas(self.board_frame, background=COLOR_CANVAS_BG,
                                      width=CANVAS_WIDTH, height=CANVAS_HEIGHT,
                                      bd=0, highlightthickness=0) # Sin borde extra
        self.canvas_board.pack()
        self._draw_grid()

        # Frame para los botones
        self.buttons_frame = tk.Frame(self.main_frame, background=COLOR_BACKGROUND)
        # Ajusta el ancho si es necesario, o deja que se ajuste a los botones
        self.buttons_frame.pack(pady=10, fill='x', padx=50)

        # Botones
        self.buttons = self._create_buttons()

        # Frame para la información inferior
        self.info_frame = tk.Frame(self.main_frame, background=COLOR_BACKGROUND, height=25)
        self.info_frame.pack_propagate(0)
        self.info_frame.pack(side='bottom', fill='x')

        # Texto de información
        self.info_labels = self._create_info_labels()

    def _draw_grid(self):
        """Dibuja las líneas de la cuadrícula en el canvas."""
        for i in range(CELL_SIZE_PX, CANVAS_WIDTH, CELL_SIZE_PX):
            self.canvas_board.create_line(i, 0, i, CANVAS_HEIGHT, fill=COLOR_GRID)
        for i in range(CELL_SIZE_PX, CANVAS_HEIGHT, CELL_SIZE_PX):
            self.canvas_board.create_line(0, i, CANVAS_WIDTH, i, fill=COLOR_GRID)

    def _create_buttons(self):
        """Crea y configura los botones de control."""
        buttons_config = [
            ("Start", COLOR_BTN_START),
            ("Stop", COLOR_BTN_STOP),
            ("Clean", COLOR_BTN_CLEAN),
            ("Exit", COLOR_BTN_EXIT)
        ]
        buttons_widgets = {}
        for text, bg_color in buttons_config:
            button = tk.Button(self.buttons_frame, text=text, font=self.font_text,
                               background=bg_color, foreground=COLOR_BUTTON_TEXT,
                               relief=tk.FLAT, borderwidth=0, padx=10)
            # Configura el botón para expandirse horizontalmente
            button.pack(side='left', expand=True, fill='x', padx=5, pady=5)
            buttons_widgets[text] = button
        return buttons_widgets

    def _create_info_labels(self):
        """Crea las etiquetas de información en la parte inferior."""
        info_labels_widgets = {}

        label_left = tk.Label(self.info_frame, text=INFO_TEXT_LEFT,
                              font=self.font_info, foreground=COLOR_INFO_TEXT,
                              background=COLOR_BACKGROUND)
        label_left.pack(side='left', padx=10)
        info_labels_widgets["left"] = label_left

        label_right = tk.Label(self.info_frame, text=INFO_TEXT_RIGHT,
                               font=self.font_info, foreground=COLOR_INFO_TEXT,
                               background=COLOR_BACKGROUND)
        label_right.pack(side='right', padx=10)
        info_labels_widgets["right"] = label_right

        return info_labels_widgets

    def draw_alive_cell(self, cell):
        """Dibuja o actualiza una celda como viva en el canvas."""
        rect_id = cell.canvas_rect_id
        if rect_id is None:
            # Crea el rectángulo si no existe
            rect_id = self.canvas_board.create_rectangle(
                cell.x1, cell.y1, cell.x2, cell.y2,
                fill=COLOR_ALIVE, outline=COLOR_GRID # Usa color de grid como borde
            )
            # Almacena el ID del canvas en la estructura Cell (requiere que Cell sea mutable o reemplazarla)
            # Esto se maneja ahora devolviendo la celda actualizada
        else:
            # Actualiza el color si ya existe
            self.canvas_board.itemconfig(rect_id, fill=COLOR_ALIVE, outline=COLOR_GRID)

        # Retorna la celda con el ID del canvas actualizado
        return cell._replace(canvas_rect_id=rect_id, canvas_inner_rect_id=None) # No usamos inner rect ahora


    def draw_dead_cell(self, cell):
        """Dibuja o actualiza una celda como muerta en el canvas."""
        rect_id = cell.canvas_rect_id
        if rect_id is None:
             # Crea el rectángulo si no existe (por si se limpia antes de dibujar)
            rect_id = self.canvas_board.create_rectangle(
                cell.x1, cell.y1, cell.x2, cell.y2,
                fill=COLOR_DEAD, outline=COLOR_GRID
            )
        else:
            # Simplemente cambia el color a 'muerto' (fondo del canvas)
            self.canvas_board.itemconfig(rect_id, fill=COLOR_DEAD, outline=COLOR_GRID)

        # Retorna la celda con el ID del canvas actualizado
        return cell._replace(canvas_rect_id=rect_id, canvas_inner_rect_id=None)

    def get_cell_reference(self, cell_with_canvas_id):
        """
        Devuelve la referencia de la celda que incluye el ID del canvas,
        útil para que la clase lógica almacene la referencia actualizada.
        """
        return cell_with_canvas_id

    # No se necesita __del__ en Python para este caso.
    # def __del__(self):
    #    return 0