from astarimpl import *
from random import randint
import csv

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
    if id in graph.walls: r = "#"
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
        walls.append((randint(0, room_size),randint(0, room_size)))

    room.walls = walls

    start, goal = (randint(0, room_size),randint(0, room_size)), (randint(0, room_size),randint(0, room_size))
    came_from, cost_so_far, min_distance = a_star_search(room, start, goal, 'manhattan')
    # print('manhattan')
    # draw_room(room, width=3, number=cost_so_far, start=start, goal=goal)

    # print('euclidean')
    came_from, eu_cost_so_far, eu_min_distance = a_star_search(room, start, goal, 'euclidean')
    # draw_room(room, width=3, number=eu_cost_so_far, start=start, goal=goal)

    # print('diagonal')
    came_from, dia_cost_so_far, dia_min_distance = a_star_search(room, start, goal, 'diagonal')
    # draw_room(room, width=3, number=dia_cost_so_far, start=start, goal=goal)

    # print('dijkstra')
    came_from, dij_cost_so_far, dij_min_distance = a_star_search(room, start, goal, 'dijkstra')
    # draw_room(room, width=3, number=dij_cost_so_far, start=start, goal=goal)

    # print()
    return [min_distance, eu_min_distance, dia_min_distance, dij_min_distance, len(cost_so_far), len(eu_cost_so_far), len(dia_cost_so_far), len(dij_cost_so_far)]

def simulation(num_of_rooms, room_size):
    print('number of rooms: ', num_of_rooms)
    print('room size: ', room_size)
    overall_distance, overall_distance_eu, overall_distance_dia, overall_distance_dij = 0, 0, 0, 0
    overall_time, overall_time_eu, overall_time_dia, overall_time_dij = 0, 0, 0, 0
    count, count_eu, count_dia, count_dij = 0, 0, 0, 0
    avg_distance, avg_distance_eu, avg_distance_dia, avg_distance_dij = 0, 0, 0, 0
    avg_time, avg_time_eu, avg_time_dia, avg_time_dij = 0, 0, 0, 0

    # for x in range(num_of_rooms): #create 100 rooms with 10 walls in them each
    while (count < num_of_rooms):
        results = generateRoom(room_size*10, room_size)
        shortest_distance = results[0]
        shortest_distance_eu = results[1]
        shortest_distance_dia = results[2]
        shortest_distance_dij = results[3]

        time = results[4]
        time_eu = results[5]
        time_dia = results[6]
        time_dij = results[7]

        if shortest_distance != 0:
            count += 1
            overall_distance += shortest_distance
            overall_time += time
        if shortest_distance_eu != 0:
            count_eu += 1
            overall_distance_eu += shortest_distance_eu
            overall_time_eu += time_eu
        if shortest_distance_dia != 0:
            count_dia += 1
            overall_distance_dia += shortest_distance_dia
            overall_time_dia += time_dia
        if shortest_distance_dij != 0:
            count_dij += 1
            overall_distance_dij += shortest_distance_dij
            overall_time_dij += time_dij

    avg_distance = (overall_distance / count)
    avg_distance_eu = (overall_distance_eu / count_eu)
    avg_distance_dia = (overall_distance_dia / count_dia)
    avg_distance_dij = (overall_distance_dij / count_dij)

    avg_time = overall_time / count
    avg_time_eu = overall_time_eu / count_eu
    avg_time_dia = overall_time_dia / count_dia
    avg_time_dij = overall_time_dij / count_dij

    print("count ", count)
    print("[manhattan] Average distance is : ", avg_distance)
    print("[euclidean] Average distance is : ", avg_distance_eu)
    print("[diagonal] Average distance is : ", avg_distance_dia)
    print("[dijkstra] Average distance is : ", avg_distance_dij)

    print("[manhattan] Average time is : ", avg_time)
    print("[euclidean] Average time is : ", avg_time_eu)
    print("[diagonal] Average time is : ", avg_time_dia)
    print("[dijkstra] Average time is : ", avg_time_dij)
    print()

    return [avg_distance, avg_distance_eu, avg_distance_dia, avg_distance_dij, avg_time, avg_time_eu, avg_time_dia, avg_time_dij]

with open('data.csv', mode='w') as data_file:
    data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for num_of_rooms in [10, 100, 500]:
        for room_size in [20, 40, 50, 100]:
            result = simulation(num_of_rooms, room_size)
            data_writer.writerow(result)
