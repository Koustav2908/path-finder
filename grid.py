# Hospital grid layout (0 = empty, 1 = wall, 2 = special)
hospital_grid = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 2, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

# Location names and coordinates
location_map = {
    "Reception": (0, 0),
    "ER": (0, 6),
    "Room 101": (2, 0),
    "ICU": (2, 4),
    "OR": (4, 6),
    "Stairs": (4, 3),
    "Exit": (6, 6),
}

# Symbols for grid
symbols = {
    0: "⬜",  # Walkable path
    1: "⬛",  # Wall
    2: "🔵",  # Generic marker
}

# Prepare display grid
display_grid = [[symbols[cell] for cell in row] for row in hospital_grid]

# Label locations
for name, (r, c) in location_map.items():
    if name == "Reception":
        display_grid[r][c] = "R📍"
    elif name == "ER":
        display_grid[r][c] = "ER🏥"
    elif name == "Room 101":
        display_grid[r][c] = "101"
    elif name == "ICU":
        display_grid[r][c] = "ICU"
    elif name == "OR":
        display_grid[r][c] = "OR"
    elif name == "Stairs":
        display_grid[r][c] = "🔽"
    elif name == "Exit":
        display_grid[r][c] = "🚪"
