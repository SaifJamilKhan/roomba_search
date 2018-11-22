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
    if 'path' in style and id in style['path']: r = "@"
    if id in graph.walls: r = "#" * width
    return r

def draw_room(graph, width=2, **style):
    for y in range(graph.height):
        for x in range(graph.width):
            print("%%-%ds" % width % draw_square(graph, (x, y), style, width), end="")
        print()


def generateRoom(numberOfwalls):
	room = GridGivenSize(10, 10)

	walls = []
	for x in range(numberOfwalls):
		walls.append((randint(0, 9),randint(0, 9)))

	room.walls = walls

	start, goal = (randint(0, 9),randint(0, 9)), (randint(0, 9),randint(0, 9))
	came_from, cost_so_far, min_distance = a_star_search(room, start, goal)
	print("Min distance is : ")
	print(min_distance)
	draw_room(room, width=3, number=cost_so_far, start=start, goal=goal)
	print()
	return min_distance

	
overall_average = 0
count = 0
for x in range(100): #create 100 rooms with 10 walls in them each
	shortestDistance = generateRoom(20) 
	if shortestDistance != 0:
		count += 1
		overall_average += shortestDistance

overall_average = (overall_average / count)
print("Average distance is : ")
print(overall_average)

