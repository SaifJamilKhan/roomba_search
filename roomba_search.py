from astarimpl import *
from random import randint

class GridGivenSize(SquareGrid):
    def __init__(self, width, height):
        super().__init__(width, height)

    def cost(self, from_node, to_node):
        return 1 # cost can be made variable but cost of 1 is assigned as of now

def draw_square(graph, id, style, width):
    r = "."
    if 'number' in style and id in style['number']: r = "%d" % style['number'][id]
    if 'start' in style and id == style['start']: r = "A"
    if 'goal' in style and id == style['goal']: r = "Z"
    if id in graph.walls: r = "#" * width
    return r

def draw_room(graph, width=2, **style):
    for y in range(graph.height):
        for x in range(graph.width):
            print("%%-%ds" % width % draw_square(graph, (x, y), style, width), end="")
        print()

def generateRoom(numberOfwalls, room_size):
    room = GridGivenSize(room_size, room_size)

    walls = []
    for x in range(numberOfwalls):
        walls.append((randint(0, 9),randint(0, 9)))

    room.walls = walls

    start, goal = (randint(0, 9),randint(0, 9)), (randint(0, 9),randint(0, 9))
    came_from, cost_so_far, min_distance = a_star_search(room, start, goal, 'manhattan')
    came_from, cost_so_far, eu_min_distance = a_star_search(room, start, goal, 'euclidean')
    came_from, cost_so_far, dia_min_distance = a_star_search(room, start, goal, 'diagonal')
    came_from, cost_so_far, dij_min_distance = a_star_search(room, start, goal, 'dijkstra')
    # print("[manhattan] Min distance is : ", min_distance)
    # print("[euclidean] Min distance is : ", eu_min_distance)
    # print("[diagonal] Min distance is : ", dia_min_distance)
    # draw_room(room, width=3, number=cost_so_far, start=start, goal=goal)
    # print()
    return [min_distance, eu_min_distance, dia_min_distance, dij_min_distance]

def simulation(num_of_rooms, room_size):
    print('number of rooms: ', num_of_rooms)
    print('room size: ', room_size)
    overall_average = 0
    count = 0
    overall_average_eu = 0
    count_eu = 0
    overall_average_dia = 0
    count_dia = 0
    overall_average_dij = 0
    count_dij = 0
    for x in range(num_of_rooms): #create 100 rooms with 10 walls in them each
        shortestDistance, shortestDistance_eu, shortestDistance_dia, shortestDistance_dij = generateRoom(40, room_size)
        if shortestDistance != 0:
            count += 1
            overall_average += shortestDistance
        if shortestDistance_eu != 0:
            count_eu += 1
            overall_average_eu += shortestDistance_eu
        if shortestDistance_dia != 0:
            count_dia += 1
            overall_average_dia += shortestDistance_dia
        if shortestDistance_dij != 0:
            count_dij += 1
            overall_average_dij += shortestDistance_dij

    overall_average = (overall_average / count)
    overall_average_eu = (overall_average_eu / count_eu)
    overall_average_dia = (overall_average_dia / count_dia)
    overall_average_dij = (overall_average_dij / count_dij)
    print("[manhattan] Average distance is : ", overall_average)
    print("[euclidean] Average distance is : ", overall_average_eu)
    print("[diagonal] Average distance is : ", overall_average_dia)
    print("[dijkstra] Average distance is : ", overall_average_dij)
    print()

simulation(1000, 30)
simulation(1000, 40)
simulation(1000, 50)
