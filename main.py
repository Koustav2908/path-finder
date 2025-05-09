import tkinter as tk
from tkinter import messagebox, ttk

from a_star import AStarPathfinder
from grid import hospital_grid, location_map

# Constants
CELL_SIZE = 60  # Size of each tile in pixels
ROWS = len(hospital_grid)
COLS = len(hospital_grid[0])

# Global variables for start and end points
start = None
end = None


def draw_grid(canvas, path=None):
    """
    Draws the grid on the canvas. Optionally highlights a path if provided.
    """

    canvas.delete("all")
    for i in range(ROWS):
        for j in range(COLS):
            x1 = j * CELL_SIZE
            y1 = i * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE

            # Determine the color based on the cell type
            cell = hospital_grid[i][j]
            color = "#e8f1f8"  # Default walkable space
            if cell == 1:
                color = "#2b2d42"  # Wall
            elif cell == 2:
                color = "#e09f3e"  # Stairs

            # Draw the cell rectangle
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="#d0dbe5")

            # Highlight the path
            if path and (i, j) in path:
                canvas.create_rectangle(x1, y1, x2, y2, fill="#6ec6ca")

            # Mark start and end positions with circles
            if (i, j) == start:
                canvas.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill="#0077b6")
            elif (i, j) == end:
                canvas.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill="#d62839")


def on_location_select():
    """
    Triggered when user selects locations and clicks 'Find Path'.
    Updates start and end, then finds and displays the path.
    """

    global start, end
    start_name = start_combo.get()
    end_name = end_combo.get()
    if start_name in location_map and end_name in location_map:
        start = location_map[start_name]
        end = location_map[end_name]
        find_and_draw_path()


def find_and_draw_path():
    """
    Runs A* to find a path between selected locations and redraws the grid with the path.
    """

    if not start or not end:
        messagebox.showwarning("Incomplete", "Please select both start and end.")
        return
    finder = AStarPathfinder(hospital_grid)
    path = finder.find_path(start, end)
    draw_grid(canvas, path=path)


def reset_grid():
    """
    Resets the grid to its initial state and clears selections.
    """

    global start, end
    start = None
    end = None
    start_combo.set("")
    end_combo.set("")
    draw_grid(canvas)


def add_legend_item(color, label, shape="rect"):
    """
    Adds a legend item to the legend section in the sidebar.
    """

    item_frame = tk.Frame(legend_frame, bg="#e6f2ff")
    item_frame.pack(anchor="w", pady=2)

    legend_canvas = tk.Canvas(
        item_frame, width=20, height=20, bg="#e6f2ff", highlightthickness=0
    )
    if shape == "rect":
        legend_canvas.create_rectangle(2, 2, 18, 18, fill=color, outline="black")
    elif shape == "oval":
        legend_canvas.create_oval(2, 2, 18, 18, fill=color, outline="black")
    legend_canvas.pack(side="left")

    tk.Label(item_frame, text=label, bg="#e6f2ff", font=("Arial", 10)).pack(
        side="left", padx=5
    )


# ------------------------ UI Setup ------------------------

# Main Window
root = tk.Tk()
root.title("🏥 Indoor Hospital Navigation")

# Main container frame
main_frame = tk.Frame(root, bg="#f0f0f0")
main_frame.pack(fill="both", expand=True)

# Sidebar for controls and legend
sidebar = tk.Frame(main_frame, width=250, bg="#ddefff", padx=15, pady=15)
sidebar.pack(side="left", fill="y")

# Sidebar title
tk.Label(
    sidebar, text="Indoor Navigator", font=("Helvetica", 16, "bold"), bg="#ffffff"
).pack(pady=10)

# Start location dropdown
tk.Label(sidebar, text="Start Location", bg="#e6f2ff").pack(anchor="w")
start_combo = ttk.Combobox(sidebar, values=list(location_map.keys()), state="readonly")
start_combo.pack(fill="x", pady=5)

# End location dropdown
tk.Label(sidebar, text="Destination", bg="#e6f2ff").pack(anchor="w")
end_combo = ttk.Combobox(sidebar, values=list(location_map.keys()), state="readonly")
end_combo.pack(fill="x", pady=5)

# Buttons
tk.Button(
    sidebar, text="Find Path", command=on_location_select, bg="#0077b6", fg="#ffffff"
).pack(fill="x", pady=5)
tk.Button(sidebar, text="Reset", command=reset_grid).pack(fill="x", pady=5)

# Legend section
legend_frame = tk.LabelFrame(sidebar, text="Legend", bg="#e6f2ff", padx=10, pady=10)
legend_frame.pack(fill="x", pady=10)

# Add legend items
add_legend_item("#e8f1f8", "Walkable Space")
add_legend_item("#2b2d42", "Wall")
add_legend_item("#e09f3e", "Stairs")
add_legend_item("#6ec6ca", "Path")
add_legend_item("#0077b6", "Start", shape="oval")
add_legend_item("#d62839", "End", shape="oval")

# Canvas to draw the grid
canvas = tk.Canvas(
    main_frame, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE, bg="#ffffff"
)
canvas.pack(side="left", fill="both", expand=True)

# Draw the initial grid
draw_grid(canvas)

# Run the Tkinter event loop
root.mainloop()
