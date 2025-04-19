import heapq


class AStarPathfinder:
    def __init__(self, grid, accessible_mode=False):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.accessible_mode = accessible_mode

    @staticmethod
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def get_neighbors(self, node):
        x, y = node
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        return [
            (nx, ny)
            for dx, dy in directions
            if 0 <= (nx := x + dx) < self.rows
            and 0 <= (ny := y + dy) < self.cols
            and self.grid[nx][ny] != 1
            and not (self.accessible_mode and self.grid[nx][ny] == 2)
        ]

    def find_path(self, start, goal):
        open_set = [(self.heuristic(start, goal), start)]
        heapq.heapify(open_set)

        came_from = {}
        g_score = {start: 0}
        closed_set = set()

        while open_set:
            _, current = heapq.heappop(open_set)

            if current in closed_set:
                continue
            closed_set.add(current)

            if current == goal:
                return self.reconstruct_path(came_from, current)

            for neighbor in self.get_neighbors(current):
                tentative_g = g_score[current] + 1

                if tentative_g < g_score.get(neighbor, float("inf")):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + self.heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score, neighbor))

        return []

    def reconstruct_path(self, came_from, current):
        path = []
        while current in came_from:
            path.append(current)
            current = came_from[current]
        path.append(current)
        return path[::-1]
