################################################################################
#                                                                              #
#                    Coded by Roberto (Tank3) Cruz Lozano                      #
#                     Refactored for clarity and config                        #
#                                                                              #
################################################################################

################################################################################
#                                MODULES
from game_of_life_config import (BOARD_WIDTH_CELLS, BOARD_HEIGHT_CELLS,
                                 CELL_SIZE_PX, Cell)

################################################################################
#                                CLASS

class GameOfLifeClass:
    """
    Gestiona la lógica y el estado del Juego de la Vida.
    """
    def __init__(self, app_interface):
        """
        Inicializa la lógica del juego.

        Args:
            app_interface: Instancia de GameOfLifeInterface para interactuar con la GUI.
        """
        self.app = app_interface
        self.width = BOARD_WIDTH_CELLS
        self.height = BOARD_HEIGHT_CELLS
        self.cell_size = CELL_SIZE_PX
        self.game_matrix = self._create_dashboard_matrix()
        self.is_running = False # Estado del juego (corriendo o detenido)

    def _create_dashboard_matrix(self):
        """Genera y retorna la matriz del juego con celdas inicializadas."""
        matrix = []
        cell_id_counter = 0
        for r in range(self.height): # row
            row_list = []
            y1 = r * self.cell_size
            y2 = y1 + self.cell_size
            for c in range(self.width): # column
                x1 = c * self.cell_size
                x2 = x1 + self.cell_size
                # Inicializa la celda como muerta y sin objetos canvas aún
                cell = Cell(
                    id=cell_id_counter,
                    x1=x1, y1=y1, x2=x2, y2=y2,
                    is_alive=False,
                    next_state=False,
                    canvas_rect_id=None,
                    canvas_inner_rect_id=None # Mantenido por si se reutiliza el diseño visual
                )
                row_list.append(cell)
                cell_id_counter += 1
            matrix.append(row_list)
        return matrix

    def _get_cell_at_coord(self, canvas_x, canvas_y):
        """Encuentra la celda correspondiente a las coordenadas del canvas."""
        if canvas_x < 0 or canvas_y < 0:
            return None
        col = canvas_x // self.cell_size
        row = canvas_y // self.cell_size
        if 0 <= row < self.height and 0 <= col < self.width:
            return self.game_matrix[row][col]
        return None

    def click_mouse_button(self, event):
        """Maneja el clic del ratón en el tablero para cambiar el estado de una celda."""
        cell = self._get_cell_at_coord(event.x, event.y)
        if cell:
            # Actualiza el estado lógico
            new_state = not cell.is_alive
            updated_cell = cell._replace(is_alive=new_state)
            row = cell.y1 // self.cell_size
            col = cell.x1 // self.cell_size
            self.game_matrix[row][col] = updated_cell

            # Actualiza la representación visual
            if new_state:
                self.app.draw_alive_cell(updated_cell)
            else:
                self.app.draw_dead_cell(updated_cell)
            # Guardamos la nueva referencia de celda actualizada en la matriz
            self.game_matrix[row][col] = self.app.get_cell_reference(updated_cell)


    def click_clean_button(self):
        """Limpia el tablero, poniendo todas las celdas a muertas."""
        self.is_running = False # Detiene el juego si estaba corriendo
        for r in range(self.height):
            for c in range(self.width):
                cell = self.game_matrix[r][c]
                if cell.is_alive:
                    updated_cell = cell._replace(is_alive=False, next_state=False)
                    self.game_matrix[r][c] = updated_cell
                    self.app.draw_dead_cell(updated_cell)
                    # Actualizamos la referencia en la matriz con el estado visual
                    self.game_matrix[r][c] = self.app.get_cell_reference(updated_cell)


    def _count_live_neighbors(self, row, col):
        """Cuenta las celdas vecinas vivas para una celda dada (con bordes conectados)."""
        live_neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0: # No contar la celda misma
                    continue
                # Calcula coordenadas vecinas con wrap around (toroidal)
                neighbor_row = (row + i) % self.height
                neighbor_col = (col + j) % self.width
                if self.game_matrix[neighbor_row][neighbor_col].is_alive:
                    live_neighbors += 1
        return live_neighbors

    def _calculate_next_state(self):
        """Calcula el estado de todas las celdas para la siguiente generación."""
        new_matrix = [row[:] for row in self.game_matrix] # Copia superficial para modificar
        for r in range(self.height):
            for c in range(self.width):
                cell = self.game_matrix[r][c]
                live_neighbors = self._count_live_neighbors(r, c)

                # Aplicar reglas del Juego de la Vida
                becomes_alive = False
                if cell.is_alive:
                    # Supervivencia: célula viva con 2 o 3 vecinos vivos sigue viva
                    if live_neighbors == 2 or live_neighbors == 3:
                        becomes_alive = True
                else:
                    # Nacimiento: célula muerta con exactamente 3 vecinos vivos nace
                    if live_neighbors == 3:
                        becomes_alive = True

                # Almacenar el estado futuro en la copia
                if cell.next_state != becomes_alive:
                     new_matrix[r][c] = cell._replace(next_state=becomes_alive)

        # Actualizar la matriz original con los nuevos estados calculados
        for r in range(self.height):
            for c in range(self.width):
                 current_cell = self.game_matrix[r][c]
                 calculated_cell = new_matrix[r][c]
                 if current_cell.next_state != calculated_cell.next_state:
                     self.game_matrix[r][c] = current_cell._replace(next_state=calculated_cell.next_state)


    def _update_board_state(self):
        """Actualiza el estado actual ('is_alive') de todas las celdas según el 'next_state' calculado."""
        for r in range(self.height):
            for c in range(self.width):
                cell = self.game_matrix[r][c]
                if cell.is_alive != cell.next_state:
                    self.game_matrix[r][c] = cell._replace(is_alive=cell.next_state)

    def _redraw_board(self):
        """Redibuja todas las celdas en el canvas según su estado actual."""
        for r in range(self.height):
            for c in range(self.width):
                cell = self.game_matrix[r][c]
                if cell.is_alive:
                    self.app.draw_alive_cell(cell)
                else:
                    self.app.draw_dead_cell(cell)
                # Actualizar referencia en la matriz por si cambió el ID del canvas
                self.game_matrix[r][c] = self.app.get_cell_reference(cell)


    def click_start_button(self):
        """Inicia la simulación del juego."""
        self.is_running = True
        print("Game Started") # Para depuración

    def click_stop_button(self):
        """Detiene la simulación del juego."""
        self.is_running = False
        print("Game Stopped") # Para depuración

    def _step(self):
        """Realiza un paso de la simulación: calcular, actualizar estado y redibujar."""
        self._calculate_next_state()
        self._update_board_state()
        self._redraw_board()

    def run_game_loop(self):
        """Ejecuta el bucle principal del juego si está activo."""
        if self.is_running:
            self._step()
        # Programa la siguiente ejecución independientemente del estado is_running
        # para mantener la interfaz responsiva y poder reiniciar.
        self.app.root.after(self.app.update_interval, self.run_game_loop)

    def setup_events(self):
        """Configura los bindings de eventos para la interacción."""
        # Clics en el canvas
        self.app.canvas_board.bind("<Button-1>", self.click_mouse_button) # Clic izquierdo
        self.app.canvas_board.bind("<B1-Motion>", self.click_mouse_button) # Arrastrar con clic izquierdo
        self.app.canvas_board.bind("<Button-3>", self.click_mouse_button) # Clic derecho
        self.app.canvas_board.bind("<B3-Motion>", self.click_mouse_button) # Arrastrar con clic derecho

        # Botones
        # Asume que app.buttons es una lista o dict donde se puede acceder al botón por nombre/índice
        self.app.buttons["Start"].config(command=self.click_start_button)
        self.app.buttons["Stop"].config(command=self.click_stop_button)
        self.app.buttons["Clean"].config(command=self.click_clean_button)
        self.app.buttons["Exit"].config(command=self.app.root.destroy)

    # No se necesita __del__ en Python para este caso.
    # def __del__(self):
    #    return 0