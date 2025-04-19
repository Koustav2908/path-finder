import tkinter as tk

building_grid = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 2, 0],
]

CELL_SIZE = 60  # Size of each tile in pixels
ROWS = len(building_grid)
COLS = len(building_grid[0])

start = None
end = None


def draw_grid(canvas, path=None):
    for i in range(ROWS):
        for j in range(COLS):
            x1 = j * CELL_SIZE
            y1 = i * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE

            cell = building_grid[i][j]
            color = "white"
            if cell == 1:
                color = "black"
            elif cell == 2:
                color = "orange"

            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

            if path and (i, j) in path:
                canvas.create_rectangle(x1, y1, x2, y2, fill="lightgreen")

            if (i, j) == start:
                canvas.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill="blue")
            elif (i, j) == end:
                canvas.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill="red")


def on_canvas_click(event):
    global start, end

    col = event.x // CELL_SIZE
    row = event.y // CELL_SIZE

    if row >= ROWS or col >= COLS:
        return

    if not start:
        start = (row, col)
    elif not end:
        end = (row, col)
        find_and_draw_path()
    else:
        start = (row, col)
        end = None
        draw_grid(canvas)


def find_and_draw_path():
    finder = AStarPathfinder(building_grid, accessible_mode=accessible_var.get())
    path = finder.find_path(start, end)
    draw_grid(canvas, path=path)


# Tkinter Setup
root = tk.Tk()
root.title("Indoor Pathfinding (A*)")

canvas = tk.Canvas(root, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE)
canvas.pack()

accessible_var = tk.BooleanVar()
accessible_check = tk.Checkbutton(
    root, text="Accessible Mode (No Stairs)", variable=accessible_var
)
accessible_check.pack()

canvas.bind("<Button-1>", on_canvas_click)

draw_grid(canvas)
root.mainloop()
