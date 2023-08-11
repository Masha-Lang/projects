############################ IMPORTS ###################################

import random

############################ FUNCTIONS #################################

def add_wall(c1, c2):
    walls[0].append([c1, c2])

def check(node_x, node_y):
    try:
        if node_x != -1 and node_y != -1:   
            if maze[node_x][node_y] == "0": return True
    except:
        pass

def output():
    for i in range(b):
        print(" ".join(maze[i]))
    print("\n")

############################ VARIABLES ################################

possibilities = [[]]
walls = [[]]
a = []
b = 7
maze = [["0" for j in range(b)] for i in range(b)]
for i in range(b): 
    maze[i][0] = maze[i][-1] = maze[0][i] = maze[-1][i] = "@"
    add_wall(0, i)
    add_wall(b-1, i)

for i in range(1, b-1):
    add_wall(i, 0)
    add_wall(i, b-1)

############################ MAIN-FUNCTION ############################

def get_maze(node_x, node_y, r):
    while True:
        possibilities.append([])
        walls.append([])
        for i in walls[r]:
            a.clear()
            for j in walls:
                if i in j: a.append("0")
            if len(a) == 1 and maze[i[0]][i[1]] != ".": maze[i[0]][i[1]] = "0"
        ### Get all possibilities
        if check(node_x, node_y+1): possibilities[r].append([node_x, node_y+1])
        if check(node_x+1, node_y): possibilities[r].append([node_x+1, node_y])
        if check(node_x, node_y-1): possibilities[r].append([node_x, node_y-1])
        if check(node_x-1, node_y): possibilities[r].append([node_x-1, node_y])
        ### Mark as visited and do walls arround
        maze[node_x][node_y] = "."
        walls[r].clear()
        if maze[node_x][node_y+1] != ".": walls[r].append([node_x, node_y+1])
        if maze[node_x+1][node_y] != ".": walls[r].append([node_x+1, node_y])
        if maze[node_x][node_y-1] != ".": walls[r].append([node_x, node_y-1])
        if maze[node_x-1][node_y] != ".": walls[r].append([node_x-1, node_y])
        for i in walls[r]:
                if maze[i[0]][i[1]] != ".": maze[i[0]][i[1]] = "@"
        ### Get random node from possibilities
        if len(possibilities[r]) == 0:
            for i in walls[r]: walls[0].append(i)
            del walls[r]
            del possibilities[r]
            return
        else:   
            x = random.choice(possibilities[r])
        get_maze(x[0], x[1], r+1)
        possibilities[r] = []


############################ START #####################################

# Get Maze
get_maze(1, 1, 1)
# To print out the output just call the function `output()`