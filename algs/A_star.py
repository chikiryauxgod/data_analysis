from heapq import heappop, heappush

class AStar:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(AStar, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.graph = {}
        self.heuristic = None

    def set_graph(self, graph):
        self.graph = graph

    def set_heuristic(self, heuristic):
        self.heuristic = heuristic

    def a_star(self, start, goal):
        if not self.graph or not self.heuristic:
            raise ValueError("Graph and heuristic must be set before running the algorithm...")
        
        open_set = []
        heappush(open_set, (0, start)) 
        came_from = {}
        g_score = {node: float('inf') for node in self.graph}
        g_score[start] = 0
        f_score = {node: float('inf') for node in self.graph}
        f_score[start] = self.heuristic(start, goal)

        while open_set:
            _, current = heappop(open_set)

            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return path[::-1] 

            for neighbor, cost in self.graph[current].items():
                tentative_g_score = g_score[current] + cost
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + self.heuristic(neighbor, goal)
                    heappush(open_set, (f_score[neighbor], neighbor))

        return None 


def heuristic(node, goal):
    estimates = {
        'A': 7, 'B': 6, 'C': 2, 'D': 5, 'E': 1, 'F': 0
    }
    return estimates[node]


astar = AStar()
astar.set_graph({
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'D': 1, 'E': 5},
    'C': {'A': 3, 'F': 2},
    'D': {'B': 1},
    'E': {'B': 5, 'F': 2},
    'F': {'C': 2, 'E': 2}
})
astar.set_heuristic(heuristic)

start, goal = 'A', 'F'
path = astar.a_star(start, goal)
print("The shortest path:", path)
