import heapq


class AStarPathfinder:
    def __init__(self, grid, accessible_mode=False):
        """
        Initializes the A* pathfinder.

        Args:
            grid (list of lists): 2D grid representing the map.
                                  0 = walkable, 1 = wall, 2 = stairs.
            accessible_mode (bool): If True, avoid stairs (value 2) in the path.
        """

        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.accessible_mode = accessible_mode

    @staticmethod
    def heuristic(a, b):
        """
        Heuristic function using Manhattan distance.

        Args:
            a, b (tuple): Coordinates of two points.

        Returns:
            int: Estimated cost between the points.
        """

        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def get_neighbors(self, node):
        """
        Get valid neighboring nodes (up, down, left, right) for a given node.

        Args:
            node (tuple): Current position (x, y).

        Returns:
            list of tuples: List of walkable neighbor positions.
        """

        x, y = node
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        return [
            (nx, ny)
            for dx, dy in directions
            if 0 <= (nx := x + dx) < self.rows  # Valid row
            and 0 <= (ny := y + dy) < self.cols  # Valid column
            and self.grid[nx][ny] != 1  # Not a wall
            and not (
                self.accessible_mode and self.grid[nx][ny] == 2
            )  # Avoid stairs if in accessible mode
        ]

    def find_path(self, start, goal):
        """
        Finds the shortest path from start to goal using the A* algorithm.

        Args:
            start (tuple): Starting position.
            goal (tuple): Goal position.

        Returns:
            list of tuples: The path from start to goal. Empty list if no path found.
        """

        # Priority queue of nodes to explore
        open_set = [(self.heuristic(start, goal), start)]
        heapq.heapify(open_set)

        came_from = {}  # For reconstructing the path
        g_score = {start: 0}  # Cost from start to each node
        closed_set = set()  # Nodes already evaluated

        while open_set:
            _, current = heapq.heappop(open_set)

            if current in closed_set:
                continue
            closed_set.add(current)

            if current == goal:
                return self.reconstruct_path(came_from, current)

            for neighbor in self.get_neighbors(current):
                tentative_g = g_score[current] + 1  # Assume each step has a cost of 1

                if tentative_g < g_score.get(neighbor, float("inf")):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + self.heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score, neighbor))

        return []  # No path found

    def reconstruct_path(self, came_from, current):
        """
        Reconstructs the path from start to goal using the came_from map.

        Args:
            came_from (dict): Map of each node to its predecessor.
            current (tuple): The goal node.

        Returns:
            list of tuples: The reconstructed path from start to goal.
        """

        path = []
        while current in came_from:
            path.append(current)
            current = came_from[current]
        path.append(current)  # Append the start node
        return path[::-1]  # Return reversed path
