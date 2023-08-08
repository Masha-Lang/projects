import random

maze = [["0" for j in range(10)] for i in range(10)]
possibilities = []



def check(node_x, node_y):
    try:
        if node_x != -1 and node_y != -1:   
            if maze[node_x][node_y] == "0" and maze[node_x][node_y] != "@": return True
    except:
        pass

def output():
    for i in range(10):
        print(" ".join(maze[i]))
    print("\n")

def function(node_x, node_y):
    if maze[node_x][node_y+1] != "." and maze[node_x][node_y+1] != "@": maze[node_x][node_y+1] = "y"
    if maze[node_x+1][node_y] != "." and maze[node_x+1][node_y] != "@": maze[node_x+1][node_y] = "y"
    if maze[node_x][node_y-1] != "." and maze[node_x][node_y-1] != "@": maze[node_x][node_y-1] = "y"
    if maze[node_x-1][node_y] != "." and maze[node_x-1][node_y] != "@": maze[node_x-1][node_y] = "y"
    ### Get all possibilities
    possibilities.clear()
    if check(node_x, node_y+2) and maze[node_x][node_y+1] != "@": possibilities.append([node_x, node_y+1])
    if check(node_x+2, node_y) and maze[node_x+1][node_y] != "@": possibilities.append([node_x+1, node_y])
    if check(node_x, node_y-2) and maze[node_x][node_y-1] != "@": possibilities.append([node_x, node_y-1])
    if check(node_x-2, node_y) and maze[node_x-1][node_y] != "@": possibilities.append([node_x-1, node_y])
    ### Mark as visited and do walls arround
    maze[node_x][node_y] = "."
    if maze[node_x][node_y+1] == "y": maze[node_x][node_y+1] = "@"
    if maze[node_x+1][node_y] == "y": maze[node_x+1][node_y] = "@"
    if maze[node_x][node_y-1] == "y": maze[node_x][node_y-1] = "@"
    if maze[node_x-1][node_y] == "y": maze[node_x-1][node_y] = "@"
    while True:
        ### Get random node from possibilities
        print(possibilities)
        if len(possibilities) == 0:
            return
        else:   
            x = random.choice(possibilities)
        output()
        function(x[0], x[1])

function(1, 1)


