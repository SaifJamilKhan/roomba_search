from astarimpl import *
diagram4 = GridWithWeights(10, 10)
diagram4.walls = [
(2,2),(1,2),(0,2),(3,2),(4,2),(5,2),
(10,4),(9,4),(8,4),(7,4),(6,4),(3,4),(4,4),(5,4),
(2,6),(1,6),(0,6),(3,6),(4,6),(5,6)
]

start, goal = (1, 1), (7, 8)
came_from, cost_so_far = a_star_search(diagram4, start, goal)
draw_grid(diagram4, width=3, point_to=came_from, start=start, goal=goal)
print()
draw_grid(diagram4, width=3, number=cost_so_far, start=start, goal=goal)

