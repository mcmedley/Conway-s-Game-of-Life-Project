import time
import sys

def empty_plane(x, y):
    l = []
    for rows in range(0, x):
        l.append([])
        for columns in range(0, y):
            l[rows].append(False)
    return l

def seed_plane_position(plane, x, y):
    if x > len(plane) or y > len(plane[0]) or x < 0 or y < 0:
        return plane
    elif plane[x][y] == False:
        plane[x][y] = True
        return plane

def seed_plane(plane):
    line = sys.stdin.readline()
    s = line.split()
    while line != "" and line != "\n":
        z = seed_plane_position(plane, int(s[0]), int(s[1]))
        line = sys.stdin.readline()
        s = line.split()
    return z


def print_plane(plane):
    for rows in range(0, len(plane)):
        for columns in range(0, len(plane[0])):
            if plane[rows][columns] == True:
                print("o", end="")
            else:
                print(" ", end="")
        print()
    return ""

def count_neighbors(plane, x, y):
    count = 0
    for rows in range(x-1, x+2):
        for columns in range(y-1, y+2):
            if rows < 0 or rows >= len(plane) or columns < 0 or columns >= len(plane[0]):
                count += 0
            elif x == rows and y == columns:
                count += 0
            elif x <= len(plane) and y <= len(plane[0]) and x >= 0 and y >= 0 and plane[rows][columns] == True:
                count += 1
    return count

def run_timestep(plane):
    new_plane = empty_plane(len(plane), len(plane[0]))
    for i in range(0, len(plane)):
        for j in range(0, len(plane[0])):
            c = count_neighbors(plane, i, j)
            if plane[i][j] == True and (c == 0 or c == 1 or c > 3):
                new_plane[i][j] = False
            elif plane[i][j] == True and (c == 2 or c == 3):
                new_plane[i][j] = True
            elif plane[i][j] == False and c == 3:
                new_plane[i][j] = True
            else:
                new_plane[i][j] == False
    return new_plane

def play_life():
    x = int(input("Insert width of plane: "))
    y = int(input("Insert length of plane: "))
    z = int(input("How many iterations? "))
    new_plane = empty_plane(x, y)
    setup = seed_plane(new_plane)
    if z < 0:
        z = float("inf")
    while z != 0:
        p = print_plane(setup)
        setup = run_timestep(setup)
        z-=1
        time.sleep(0.1)
print(play_life())   