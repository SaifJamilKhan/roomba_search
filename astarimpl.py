import heapq
import math

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id):
        return id not in self.walls

    def neighbors(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0: results.reverse() # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results

def heuristic(a, b, option):
    distance = None
    (x1, y1) = a
    (x2, y2) = b
    if option == 'manhattan':
        distance = abs(x1 - x2) + abs(y1 - y2)
    elif option == 'euclidean':
        distance = math.sqrt(pow((x1 - x2),2) + pow((x1 - x2),2))
    elif option == 'diagonal':
        distance = max(abs(x1 - x2), abs((x1 - x2)))
    return distance

def a_star_search(graph, start, goal, option):
    queue = PriorityQueue()
    queue.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    min_distance = 9999999
    while not queue.empty():
        current = queue.get()

        if current == goal:

            for next in graph.neighbors(current): # look at cost of all the neighbors
                if next in cost_so_far:
                    min_distance = min(min_distance, cost_so_far[next])
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next, option)
                queue.put(next, priority)
                came_from[next] = current

    if min_distance == 9999999:
        min_distance = 0
    return came_from, cost_so_far, min_distance
