import tkinter as tk
import colorsys
import random

_BG        = "#1A1B26"
_CANVAS_BG = "#24283B"
_GRID      = "#2A2E42"
_DEAD      = "#24283B"
_ACCENT    = "#7AA2F7"
_TEXT      = "#C0CAF5"
_SUBTEXT   = "#565F89"
_BTN_FG    = "#1A1B26"


class GameOfLifeInterface(tk.Frame):
    ROWS      = 60
    COLS      = 80
    CELL_SIZE = 9

    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self._configure_root()
        self._build_layout()
        self._cell_ids = [[None] * self.COLS for _ in range(self.ROWS)]
        self._init_cells()

    def _configure_root(self):
        self.root.title("Game of Life  v2.0")
        self.root.configure(bg=_BG)
        self.root.resizable(False, False)
        try:
            self.root.iconbitmap("./img/Glider.ico")
        except Exception:
            pass

    def _build_layout(self):
        tk.Label(
            self.root, text="Game of Life",
            font=("Arial", 22, "bold"), bg=_BG, fg=_ACCENT,
        ).pack(pady=(12, 6))

        self.canvas = tk.Canvas(
            self.root,
            width=self.COLS * self.CELL_SIZE,
            height=self.ROWS * self.CELL_SIZE,
            bg=_CANVAS_BG, bd=0,
            highlightthickness=1,
            highlightbackground=_ACCENT,
        )
        self.canvas.pack(padx=20)

        stats_row = tk.Frame(self.root, bg=_BG)
        stats_row.pack(fill="x", padx=20, pady=(6, 2))
        self.gen_var   = tk.StringVar(value="Generación: 0")
        self.alive_var = tk.StringVar(value="Vivas: 0")
        tk.Label(stats_row, textvariable=self.gen_var,   font=("Consolas", 11), bg=_BG, fg=_TEXT).pack(side="left")
        tk.Label(stats_row, textvariable=self.alive_var, font=("Consolas", 11), bg=_BG, fg=_TEXT).pack(side="right")

        btn_row = tk.Frame(self.root, bg=_BG)
        btn_row.pack(fill="x", padx=20, pady=6)
        kw = dict(font=("Arial", 11, "bold"), fg=_BTN_FG, relief="flat", padx=6, pady=8, cursor="hand2")
        self.btn_start = tk.Button(btn_row, text="Iniciar",   bg="#9ECE6A", **kw)
        self.btn_stop  = tk.Button(btn_row, text="Pausar",    bg="#F7768E", **kw)
        self.btn_step  = tk.Button(btn_row, text="Paso",      bg="#7AA2F7", **kw)
        self.btn_rand  = tk.Button(btn_row, text="Aleatorio", bg="#BB9AF7", **kw)
        self.btn_clear = tk.Button(btn_row, text="Limpiar",   bg="#FF9E64", **kw)
        self.btn_exit  = tk.Button(btn_row, text="Salir",     bg="#414868", fg=_TEXT, relief="flat",
                                   padx=6, pady=8, cursor="hand2", font=("Arial", 11, "bold"))
        for btn in (self.btn_start, self.btn_stop, self.btn_step,
                    self.btn_rand, self.btn_clear, self.btn_exit):
            btn.pack(side="left", expand=True, fill="x", padx=2)

        speed_row = tk.Frame(self.root, bg=_BG)
        speed_row.pack(fill="x", padx=20, pady=(0, 10))
        tk.Label(speed_row, text="Velocidad:", font=("Arial", 10), bg=_BG, fg=_TEXT).pack(side="left")
        self.speed_var = tk.IntVar(value=8)
        tk.Scale(
            speed_row, variable=self.speed_var,
            from_=1, to=40, orient="horizontal",
            bg=_BG, fg=_TEXT, troughcolor=_GRID,
            highlightthickness=0, showvalue=True,
        ).pack(side="left", fill="x", expand=True)
        tk.Label(speed_row, text="gen/s", font=("Arial", 10), bg=_BG, fg=_TEXT).pack(side="left", padx=(4, 0))

        tk.Label(
            self.root, text="Coded by Tank3  |  v2.0",
            font=("Arial", 9), bg=_BG, fg=_SUBTEXT,
        ).pack(pady=(0, 8))

    def _init_cells(self):
        cs = self.CELL_SIZE
        for r in range(self.ROWS):
            for c in range(self.COLS):
                x1, y1 = c * cs, r * cs
                self._cell_ids[r][c] = self.canvas.create_rectangle(
                    x1, y1, x1 + cs, y1 + cs,
                    fill=_DEAD, outline=_GRID,
                )

    # ── public drawing API ────────────────────────────────────────────────────

    def set_alive(self, row, col):
        color = _vivid_color()
        self.canvas.itemconfig(self._cell_ids[row][col], fill=color, outline=color)

    def set_dead(self, row, col):
        self.canvas.itemconfig(self._cell_ids[row][col], fill=_DEAD, outline=_GRID)

    def apply_mask(self, changed, state):
        for r, c in zip(*changed.nonzero()):
            if state[r, c]:
                self.set_alive(r, c)
            else:
                self.set_dead(r, c)

    def update_stats(self, generation, alive):
        self.gen_var.set(f"Generación: {generation:,}")
        self.alive_var.set(f"Vivas: {alive:,}")


def _vivid_color():
    r, g, b = colorsys.hsv_to_rgb(random.random(), 0.75, 0.95)
    return "#%02x%02x%02x" % (int(r * 255), int(g * 255), int(b * 255))
