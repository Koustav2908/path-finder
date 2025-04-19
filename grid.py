# Hospital grid layout (0 = empty, 1 = wall, 2 = special)
hospital_grid = [
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0],
]

# Location names and coordinates
location_map = {
    "Reception": (0, 0),
    "ER": (0, 10),
    "Room 101": (2, 0),
    "Room 102": (2, 4),
    "Room 103": (2, 10),
    "ICU": (4, 4),
    "OR": (4, 10),
    "Radiology": (6, 5),
    "Lab": (6, 11),
    "Pharmacy": (8, 0),
    "Cafeteria": (8, 10),
    "Stairs": (4, 3),
    "Exit": (9, 11),
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
