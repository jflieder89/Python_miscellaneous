import pygame
import random
import copy #going to need this for deepcopy method, to be sure that creating the updated grid doesn't affect te current grid
import time #to implement a delay between the automatically iterating generations/grids
random.seed() #set the randomw seed based on the time without a parameter passed in
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
width = height = 20 #set width and height of grid blocks
margin = int(width/10) #set margin between grid blocks
grid = []    #empty master list of lists to be filled with 0's and 1's for the grid
dim =  30 #this will be how many grid blocks in each row and column are in the display

# test out glider gun. Be sure to change dim to be dim = 30 so it will work!!:
# grid = [
# [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# ]
#create random grid:
for row in range(dim):
    grid.append([]) #add a row to the grid
    for column in range(dim):
        grid[row].append(random.randint(0,1)) #add an element to the row, which will be randomly 0 or 1

pygame.init() #needed to get this started
window_size = [dim*(width + margin) + margin, dim*(height + margin) + margin] #set display size based on choices above
scr = pygame.display.set_mode(window_size) #actually create the display to show up on the screen
scr.fill(black)
pygame.display.set_caption("Game of Life") #set a caption for the display - self explanatory
done = False
clock = pygame.time.Clock()
neighbors_adj = [ [-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1] ] #differences in grid coordinates that a neighbor has

for row in range(dim):
    for column in range(dim):
        if grid[row][column] == 1:
            color = red
        else:
            color = white
        pygame.draw.rect(scr, color,[(margin + width) * column + margin, (margin + height) * row + margin, width, height])
clock.tick(50)
pygame.display.update()
# print(grid)

while not done: # to continue updating without having to explicitly prompt it
    for event in pygame.event.get(): #accounting for certain key/mouse/whatever inputs from the user
        if event.type == pygame.QUIT: #for example, if you close the grid display window
            print('\nGame closed out')
            done = True
        if event.type == pygame.KEYDOWN: #need to first check the type before checking key
            #print('q for quit')
            if event.key == pygame.K_q: # replace the 'q' to whatever key you wanted to be specified
                print('\nGame ended')
                done = True


    new_grid = copy.deepcopy(grid) #create a copy of grid for the next iteration
    for row in range(dim): #iterate through rows
        for col in range(dim): #iterate through elements of the row. USE GRID AND NOT ROW IN ORDER TO FULLY ITERATE!
            count = 0 #count of alive '1' neighbors around this grid block
            # print('grid is:', grid)
            # print('new_grid is:', new_grid)
            for i in neighbors_adj: #iterate through neighbor possibilities
                if ((row + i[0]) in range(dim)) and ((col + i[1]) in range(dim)) and (grid[row+i[0]][col+i[1]] == 1): #if the neighbor is on the grid and alive
                    # print()
                    # print('Got an alive neighbor')
                    # print('I\'m at row', row, 'and col', col)
                    # print('The alive neighbor is at row', row + i[0], 'and col', col + i[1])
                    # print('neighbor adj i is:', i)
                    # print('grid is:', grid)
                    # print('new_grid is:', new_grid)
                    count += 1
            # print('Final count of alive neighbors at row', row, 'and col', col, 'is', count)
            if (grid[row][col] == 0) and (count == 3): #if a dead grid block has exactly 3 live neighbors
                # print("It comes alive!")
                new_grid[row][col] = 1 #it comes to life!
            if (grid[row][col] == 1) and (count not in [2,3]): #if a live cell has fewer than 2 live neighbors
                # print("It dies!")
                new_grid[row][col] = 0 #it dies!
    grid = new_grid[:] #update the grid with the changes

        # here is some code to change the tiles by clicking:
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     pos = pygame.mouse.get_pos()
        #     column = pos[0] // (width + margin)
        #     row = pos[1] // (height + margin)
        #     grid[row][column] = 1
        #     print("Click ", pos, "Grid coordinates: ", row, column)

    for row in range(dim):
        for column in range(dim):
            if grid[row][column] == 1:
                color = red
            else:
                color = white
            pygame.draw.rect(scr, color,[(margin + width) * column + margin, (margin + height) * row + margin, width, height])
    clock.tick(50)
    pygame.display.update()
    time.sleep(1)
pygame.quit()
# pygame.display.init
