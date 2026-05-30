import numpy as np


class GameOfLifeClass:
    def __init__(self, ui):
        self.ui = ui
        self.rows = ui.ROWS
        self.cols = ui.COLS
        self.cell_size = ui.CELL_SIZE
        self.state = np.zeros((self.rows, self.cols), dtype=np.uint8)
        self.generation = 0
        self.running = False
        self._drag_value = None

    # ── Conway logic ──────────────────────────────────────────────────────────

    def _neighbors(self):
        s = self.state
        above  = np.roll(s,  1, axis=0)
        below  = np.roll(s, -1, axis=0)
        return (above
                + below
                + np.roll(s,  1, axis=1)
                + np.roll(s, -1, axis=1)
                + np.roll(above,  1, axis=1)
                + np.roll(above, -1, axis=1)
                + np.roll(below,  1, axis=1)
                + np.roll(below, -1, axis=1))

    def _step(self):
        prev = self.state.copy()
        n = self._neighbors()
        alive = self.state == 1
        self.state = ((alive & ((n == 2) | (n == 3))) | (~alive & (n == 3))).astype(np.uint8)
        self.generation += 1
        self.ui.apply_mask(prev != self.state, self.state)
        self.ui.update_stats(self.generation, int(self.state.sum()))

    # ── actions ───────────────────────────────────────────────────────────────

    def _start(self):
        self.running = True

    def _stop(self):
        self.running = False

    def _step_once(self):
        self._stop()
        self._step()

    def _randomize(self):
        self.state = (np.random.random((self.rows, self.cols)) < 0.3).astype(np.uint8)
        self.generation = 0
        self.ui.apply_mask(np.ones((self.rows, self.cols), dtype=bool), self.state)
        self.ui.update_stats(0, int(self.state.sum()))

    def _clear(self):
        changed = self.state.astype(bool)
        self.state[:] = 0
        self.generation = 0
        self.running = False
        self.ui.apply_mask(changed, self.state)
        self.ui.update_stats(0, 0)

    # ── mouse events ──────────────────────────────────────────────────────────

    def _cell_at(self, event):
        r = event.y // self.cell_size
        c = event.x // self.cell_size
        if 0 <= r < self.rows and 0 <= c < self.cols:
            return r, c
        return None, None

    def _on_press(self, event):
        r, c = self._cell_at(event)
        if r is None:
            return
        self._drag_value = 1 - int(self.state[r, c])
        self._paint(r, c)

    def _on_drag(self, event):
        if self._drag_value is None:
            return
        r, c = self._cell_at(event)
        if r is None or int(self.state[r, c]) == self._drag_value:
            return
        self._paint(r, c)

    def _on_release(self, _event):
        self._drag_value = None

    def _on_erase_drag(self, event):
        r, c = self._cell_at(event)
        if r is None or self.state[r, c] == 0:
            return
        self.state[r, c] = 0
        self.ui.set_dead(r, c)
        self.ui.update_stats(self.generation, int(self.state.sum()))

    def _paint(self, r, c):
        self.state[r, c] = self._drag_value
        if self._drag_value:
            self.ui.set_alive(r, c)
        else:
            self.ui.set_dead(r, c)
        self.ui.update_stats(self.generation, int(self.state.sum()))

    # ── wiring ────────────────────────────────────────────────────────────────

    def events(self):
        self.ui.canvas.bind("<ButtonPress-1>",   self._on_press)
        self.ui.canvas.bind("<B1-Motion>",        self._on_drag)
        self.ui.canvas.bind("<ButtonRelease-1>",  self._on_release)
        self.ui.canvas.bind("<B3-Motion>",        self._on_erase_drag)
        self.ui.canvas.bind("<ButtonPress-3>",    self._on_erase_drag)

        self.ui.btn_start.config(command=self._start)
        self.ui.btn_stop.config( command=self._stop)
        self.ui.btn_step.config( command=self._step_once)
        self.ui.btn_rand.config( command=self._randomize)
        self.ui.btn_clear.config(command=self._clear)
        self.ui.btn_exit.config( command=self.ui.root.destroy)

    # ── game loop ─────────────────────────────────────────────────────────────

    def game(self):
        if self.running:
            self._step()
        delay = max(25, 1000 // self.ui.speed_var.get())
        self.ui.root.after(delay, self.game)
