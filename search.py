# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

import numpy as np


grid = [[0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0]]
# grid =[[0,0,0],
#        [0,0,0],
#        [0,0,0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def get_neighbors(cell):
    ls =[]
    for i in range(len(delta)):
        x = cell[0]+delta[i][0]
        y = cell[1]+delta[i][1]
        if (x >=0 and x < len(grid)) and (y >=0 and y < len(grid[0])):
            ls.append([x,y])
#     print(ls)
    return ls
    

def search(grid,init,goal,cost):
    current_cost = 0
    open = dict()
    closed =[]
    current_node = init
    open[tuple(init)] = current_cost
    try:
        while len(open)!=0:
            if current_node == tuple(goal):
                return [open[tuple(current_node)],current_node[0],current_node[1]]
                break
            else:
                neighbors = get_neighbors(current_node)
                closed.append(tuple(current_node))
    #             print(open)
    #             print(current_node)
    #             print(neighbors)
                for i in range(len(delta)):
                    x = current_node[0]+delta[i][0]
                    y = current_node[1]+delta[i][1]
                    if (x >=0 and x < len(grid)) and (y >=0 and y < len(grid[0])):
                        neighbor =[x,y]
                        if grid[neighbor[0]][neighbor[1]] ==0 :
                            current_cost = open[tuple(current_node)] + cost
                            if (tuple(neighbor)  not in open.keys()) or (open[tuple(neighbor)] > current_cost) :
                                open[tuple(neighbor)] = current_cost

                dictionary_keys = list(open.keys())
                open = {dictionary_keys[i]: sorted(open.values())[i] for i in range(len(dictionary_keys))}
                i = 0
                while list(open)[i] in closed :
                    i+=1
                current_node = list(open)[i]
    except:
        return "fail"

            
                            
                
print(search(grid,init,goal,cost))