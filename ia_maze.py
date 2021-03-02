# Maze generator -- Randomized Prim Algorithm

# Imports
import random
import time
import os
import numpy as np
from colorama import init
from colorama import Fore, Back, Style
from PIL import Image, ImageDraw
import numpy as np
import moviepy.editor as mp
images = []

# Functions


def clear(): return os.system('clear')


def printMaze(maze):
    for i in range(0, height):
        for j in range(0, width):
            if (maze[i][j] == 'u'):
                # print(Fore.WHITE + str(maze[i][j]), end=" ")
                print(Fore.WHITE + str(maze[i][j]), end=" ")

            elif (maze[i][j] == 'c'):
                # print(Fore.GREEN + str(maze[i][j]), end=" ")
                print(Fore.GREEN + "#", end=" ")

            else:
                # print(Fore.RED + str(maze[i][j]), end=" ")
                print(Fore.RED + "o", end=" ")

        print('')

# Find number of surrounding cells


def surroundingCells(rand_wall):
    s_cells = 0
    if (maze[rand_wall[0]-1][rand_wall[1]] == 'c'):
        s_cells += 1
    if (maze[rand_wall[0]+1][rand_wall[1]] == 'c'):
        s_cells += 1
    if (maze[rand_wall[0]][rand_wall[1]-1] == 'c'):
        s_cells += 1
    if (maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
        s_cells += 1

    return s_cells


# Main code
# Init variables
wall = 'w'
cell = 'c'
unvisited = 'u'
height = int(input('Hauteur : '))
width = int(input('Largeur : '))
solutions = int(input('Une ou Plusieurs Solutions [0/1] : '))
# solutions = 0
maze = []

# Initialize colorama
init()

# Denote all cells as unvisited
for i in range(0, height):
    line = []
    for j in range(0, width):
        line.append(unvisited)
    maze.append(line)

# Randomize starting point and set it a cell
starting_height = int(random.random()*height)
starting_width = int(random.random()*width)
if (starting_height == 0):
    starting_height += 1
if (starting_height == height-1):
    starting_height -= 1
if (starting_width == 0):
    starting_width += 1
if (starting_width == width-1):
    starting_width -= 1

# Mark it as cell and add surrounding walls to the list
maze[starting_height][starting_width] = cell
walls = []
walls.append([starting_height - 1, starting_width])
walls.append([starting_height, starting_width - 1])
walls.append([starting_height, starting_width + 1])
walls.append([starting_height + 1, starting_width])

# Denote walls in maze
maze[starting_height-1][starting_width] = 'w'
maze[starting_height][starting_width - 1] = 'w'
maze[starting_height][starting_width + 1] = 'w'
maze[starting_height + 1][starting_width] = 'w'

while (walls):
    # Pick a random wall
    rand_wall = walls[int(random.random()*len(walls))-1]

    # Check if it is a left wall
    if (rand_wall[1] != 0):
        if (maze[rand_wall[0]][rand_wall[1]-1] == 'u' and maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
            # Find the number of surrounding cells
            s_cells = surroundingCells(rand_wall)

            if (s_cells < 2):
                # Denote the new path
                maze[rand_wall[0]][rand_wall[1]] = 'c'

                # Mark the new walls
                # Upper cell
                if (rand_wall[0] != 0):
                    if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                        maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                    if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0]-1, rand_wall[1]])

                # Bottom cell
                if (rand_wall[0] != height-1):
                    if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
                        maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                    if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0]+1, rand_wall[1]])

                # Leftmost cell
                if (rand_wall[1] != 0):
                    if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
                        maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                    if ([rand_wall[0], rand_wall[1]-1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1]-1])

            # Delete wall
            for wall in walls:
                if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                    walls.remove(wall)

            continue

    # Check if it is an upper wall
    if (rand_wall[0] != 0):
        if (maze[rand_wall[0]-1][rand_wall[1]] == 'u' and maze[rand_wall[0]+1][rand_wall[1]] == 'c'):

            s_cells = surroundingCells(rand_wall)
            if (s_cells < 2):
                # Denote the new path
                maze[rand_wall[0]][rand_wall[1]] = 'c'

                # Mark the new walls
                # Upper cell
                if (rand_wall[0] != 0):
                    if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                        maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                    if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0]-1, rand_wall[1]])

                # Leftmost cell
                if (rand_wall[1] != 0):
                    if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
                        maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                    if ([rand_wall[0], rand_wall[1]-1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1]-1])

                # Rightmost cell
                if (rand_wall[1] != width-1):
                    if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
                        maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                    if ([rand_wall[0], rand_wall[1]+1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1]+1])

            # Delete wall
            for wall in walls:
                if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                    walls.remove(wall)

            continue

    # Check the bottom wall
    if (rand_wall[0] != height-1):
        if (maze[rand_wall[0]+1][rand_wall[1]] == 'u' and maze[rand_wall[0]-1][rand_wall[1]] == 'c'):

            s_cells = surroundingCells(rand_wall)
            if (s_cells < 2):
                # Denote the new path
                maze[rand_wall[0]][rand_wall[1]] = 'c'

                # Mark the new walls
                if (rand_wall[0] != height-1):
                    if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
                        maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                    if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0]+1, rand_wall[1]])
                if (rand_wall[1] != 0):
                    if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
                        maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                    if ([rand_wall[0], rand_wall[1]-1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1]-1])
                if (rand_wall[1] != width-1):
                    if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
                        maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                    if ([rand_wall[0], rand_wall[1]+1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1]+1])

            # Delete wall
            for wall in walls:
                if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                    walls.remove(wall)

            continue

    # Check the right wall
    if (rand_wall[1] != width-1):
        if (maze[rand_wall[0]][rand_wall[1]+1] == 'u' and maze[rand_wall[0]][rand_wall[1]-1] == 'c'):

            s_cells = surroundingCells(rand_wall)
            if (s_cells < 2):
                # Denote the new path
                maze[rand_wall[0]][rand_wall[1]] = 'c'

                # Mark the new walls
                if (rand_wall[1] != width-1):
                    if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
                        maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                    if ([rand_wall[0], rand_wall[1]+1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1]+1])
                if (rand_wall[0] != height-1):
                    if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
                        maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                    if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0]+1, rand_wall[1]])
                if (rand_wall[0] != 0):
                    if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                        maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                    if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0]-1, rand_wall[1]])

            # Delete wall
            for wall in walls:
                if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                    walls.remove(wall)

            continue

    # Delete the wall from the list anyway
    for wall in walls:
        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
            walls.remove(wall)


# Mark the remaining unvisited cells as walls
for i in range(0, height):
    for j in range(0, width):
        if (maze[i][j] == 'u'):
            maze[i][j] = 'w'

# Set entrance and exit
for i in range(0, width):
    if (maze[1][i] == 'c'):
        maze[0][i] = 'c'
        break

for i in range(width-1, 0, -1):
    if (maze[height-2][i] == 'c'):
        maze[height-1][i] = 'c'
        break

# Print final maze
# print(np.matrix(maze))
print('\n')
printMaze(maze)
print(Fore.WHITE)
# print(type(maze))
# print(maze)

bin_maze = np.zeros((height, width))

rdm = 0

for t in range(height):
    for u in range(width):
        """
        if t == 0:
            print(t)
            print(u)
            print(maze[t][u] == 'w')
            print(maze[t][u] == 'c')"""
        if maze[t][u] == ('w'):
            bin_maze[t, u] = 1
        if maze[t][u] == ('c'):
            bin_maze[t, u] = 0
        if solutions == 1 and t > 0 and u > 0 and t < height-1 and u < width-2:
            rdm = random.randint(1, 10)
            if rdm == 1:
                bin_maze[t, u] = 0

"""
print(np.matrix(bin_maze))
print(np.matrix(maze))
"""
# print(type(bin_maze))
list_bin_maze = list(bin_maze)
# print(type(list_bin_maze))

f_maze = open('txt_maze.txt', 'w')

# f_maze.write(str(np.matrix(maze)))
# f_maze.write('\n')
f_maze.write(str(bin_maze).replace(".", ""))

f_maze.close()

a = list_bin_maze

print("\tCalcul de la meilleure solution...")

"""a = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]"""

zoom = 20
borders = 6
start = 0, 1
end = height-1, width-2


def make_step(k):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == k:
                if i > 0 and m[i-1][j] == 0 and a[i-1][j] == 0:
                    m[i-1][j] = k + 1
                if j > 0 and m[i][j-1] == 0 and a[i][j-1] == 0:
                    m[i][j-1] = k + 1
                if i < len(m)-1 and m[i+1][j] == 0 and a[i+1][j] == 0:
                    m[i+1][j] = k + 1
                if j < len(m[i])-1 and m[i][j+1] == 0 and a[i][j+1] == 0:
                    m[i][j+1] = k + 1


def print_m(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(str(m[i][j]).ljust(2), end=' ')
        print()


def draw_matrix(a, m, the_path=[]):
    im = Image.new('RGB', (zoom * len(a[0]), zoom * len(a)), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    for i in range(len(a)):
        for j in range(len(a[i])):
            color = (255, 255, 255)
            r = 0
            if a[i][j] == 1:
                color = (0, 0, 0)
            if i == start[0] and j == start[1]:
                color = (0, 255, 0)
                r = borders
            if i == end[0] and j == end[1]:
                color = (0, 255, 0)
                r = borders
            draw.rectangle((j*zoom+r, i*zoom+r, j*zoom+zoom -
                            r-1, i*zoom+zoom-r-1), fill=color)
            if m[i][j] > 0:
                r = borders
                draw.ellipse((j * zoom + r, i * zoom + r, j * zoom + zoom - r - 1, i * zoom + zoom - r - 1),
                             fill=(255, 0, 0))
    for u in range(len(the_path)-1):
        y = the_path[u][0]*zoom + int(zoom/2)
        x = the_path[u][1]*zoom + int(zoom/2)
        y1 = the_path[u+1][0]*zoom + int(zoom/2)
        x1 = the_path[u+1][1]*zoom + int(zoom/2)
        draw.line((x, y, x1, y1), fill=(0, 255, 0), width=5)
    draw.rectangle(
        (0, 0, zoom * len(a[0]), zoom * len(a)), outline=(0, 255, 0), width=2)
    images.append(im)


m = []
for i in range(len(a)):
    m.append([])
    for j in range(len(a[i])):
        m[-1].append(0)
i, j = start
m[i][j] = 1

k = 0
while m[end[0]][end[1]] == 0:
    k += 1
    make_step(k)
    draw_matrix(a, m)


i, j = end
k = m[i][j]
the_path = [(i, j)]
while k > 1:
    if i > 0 and m[i - 1][j] == k-1:
        i, j = i-1, j
        the_path.append((i, j))
        k -= 1
    elif j > 0 and m[i][j - 1] == k-1:
        i, j = i, j-1
        the_path.append((i, j))
        k -= 1
    elif i < len(m) - 1 and m[i + 1][j] == k-1:
        i, j = i+1, j
        the_path.append((i, j))
        k -= 1
    elif j < len(m[i]) - 1 and m[i][j + 1] == k-1:
        i, j = i, j+1
        the_path.append((i, j))
        k -= 1
    draw_matrix(a, m, the_path)

for i in range(10):
    if i % 2 == 0:
        draw_matrix(a, m, the_path)
    else:
        draw_matrix(a, m)


"""
print_m(m)
print(the_path)
"""

GIF_NAME = 'gif_maze.gif'
MP4_NAME = 'mp4_maze.mp4'

images[0].save(GIF_NAME,
               save_all=True, append_images=images[1:],
               optimize=False, duration=1, loop=0)

print("GIF de la solution sauvegardé sous le nom : " + GIF_NAME)

clip = mp.VideoFileClip(GIF_NAME)
clip.write_videofile(MP4_NAME)

print("Video .mp4 de la solution sauvegardé sous le nom : " + MP4_NAME)

"""
f_maze = open('txt_maze.txt', 'w')

f_maze.write(str(np.matrix(a)))

f_maze.close()


print(type(a))
print(type(m))
"""
