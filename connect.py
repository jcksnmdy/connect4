# import pygame module in this program
import pygame
  
# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
  
# define the RGB value
# for black colour
black = (0, 0, 0)
  
# assigning values to X and Y variable
X = 520
Y = 440
  
# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y ))
  
# set the pygame window name
pygame.display.set_caption('Image')
  
# create a surface object, image is drawn on it.
grid = pygame.image.load(r'/Users/s1034274/Desktop/connect4/grid.png')

choice1 = "red"
choice2 = "blue"
playerPeice = pygame.image.load(r'/Users/s1034274/Desktop/connect4/' + str(choice1) + '.png')
playerPeice = pygame.transform.scale(playerPeice, (50, 50))

y = 20

gridState = [[' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ']]
player = 1
globalCol = 1
globalRow = 1


def dropPuck(col):
    global player, yD, globalCol, playerPeice, globalRow, choice1, choice2, colEnd, rowEnd
    print("dropping on col " + str(col))
    i = 5
    globalCol = col
    while ("1" not in gridState[i][col-1]) and ("2" not in gridState[i][col-1]) and (i >= 0):
        print("dropping") 
        i-=1 
    if (i < 5):  
        stamp((colEnd, rowEnd), playerPeice)
        globalRow = (i+2)
        gridState[i+1][(col-1)] = str(player)
        print(gridState[5])
        print(gridState[4])
        print(gridState[3])
        print(gridState[2])
        print(gridState[1])
        print(gridState[0])
        if (player == 1):
            player = 2
            playerPeice = pygame.image.load(r'/Users/s1034274/Desktop/connect4/' + str(choice1) + '.png')
            playerPeice = pygame.transform.scale(playerPeice, (50, 50))
            print(choice1)
        else:
            player = 1
            playerPeice = pygame.image.load(r'/Users/s1034274/Desktop/connect4/' + str(choice2) + '.png')
            playerPeice = pygame.transform.scale(playerPeice, (50, 50))
            print(choice2)
    else:
        print("Not possible")
    yD = 20


stamps = []

def stamp(pos, surf):
    stamps.append((pos, surf))

def draw_stamps(target_surf):
    for pos, surf in stamps:
        target_surf.blit(surf, pos)

dropping = False
col1 = 57
col2 = 116
col3 = 175
col4 = 233
col5 = 292
col6 = 350
col7 = 410

row1 = 357
row2 = 298
row3 = 239
row4 = 180
row5 = 121
row6 = 62
p1Color = (255, 0, 0)
p2Color = (0, 0, 255)


def determinCol():
    global globalCol
    if (globalCol == 1):
        return col1
    if (globalCol == 2):
        return col2
    if (globalCol == 3):
        return col3
    if (globalCol == 4):
        return col4
    if (globalCol == 5):
        return col5
    if (globalCol == 6):
        return col6
    if (globalCol == 7):
        return col7

def determinRow():
    global globalRow
    if (globalRow == 1):
        return row1
    if (globalRow == 2):
        return row2
    if (globalRow == 3):
        return row3
    if (globalRow == 4):
        return row4
    if (globalRow == 5):
        return row5
    if (globalRow == 6):
        return row6
    else:
        return 0

col1Button = pygame.Rect(col1, 10, 50, 29)
col2Button = pygame.Rect(col2, 10, 50, 29)
col3Button = pygame.Rect(col3, 10, 50, 29)
col4Button = pygame.Rect(col4, 10, 50, 29)
col5Button = pygame.Rect(col5, 10, 50, 29)
col6Button = pygame.Rect(col6, 10, 50, 29)
col7Button = pygame.Rect(col7, 10, 50, 29)


p1B = pygame.Rect(10, 10, 30, 29)
p2B = pygame.Rect(10, 40, 30, 29)
rowEnd = 1000
colEnd = 1000

def callback(value):
    pass



countI = 0

def click_event(event, x, y, flags, params):
    global image, countI, x1, y1, x2, y2, x3, y3
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
        countI+=1
ret = None
image = None

timeWinning = 0

def main():
    global dropping, player, y, globalCol, playerPeice, globalRow, choice1, choice2, colEnd, rowEnd
    global ret, image, timeWinning, yD, p1Color, p2Color
    x = 0
    y = 0
    while True:
        # completely fill the surface object
        # with white colour
        display_surface.fill(black)
        if dropping:
            if (yD<=rowEnd):
                yD*=1.019
            else:
                yD = rowEnd
                dropping = False
                stamp((colEnd, rowEnd), playerPeice)
            # copying the image surface object
            # to the display surface object at
            # (0, 0) coordinate.
            display_surface.blit(playerPeice, (colEnd, yD))
        
        draw_stamps(display_surface)
        pygame.draw.rect(display_surface, p1Color, p1B)
        pygame.draw.rect(display_surface, p2Color, p2B)
        display_surface.blit(grid, (50, 40))
        
        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for event in pygame.event.get() :
            if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos  # gets mouse position
                    if col1Button.collidepoint(mouse_pos):
                        dropPuck(1)
                        rowEnd = determinRow()
                        colEnd = determinCol()
                        dropping = True
                    if col2Button.collidepoint(mouse_pos):
                        dropPuck(2)
                        rowEnd = determinRow()
                        colEnd = determinCol()
                        dropping = True
                    if col3Button.collidepoint(mouse_pos):
                        dropPuck(3)
                        rowEnd = determinRow()
                        colEnd = determinCol()
                        dropping = True
                    if col4Button.collidepoint(mouse_pos):
                        dropPuck(4)
                        rowEnd = determinRow()
                        colEnd = determinCol()
                        dropping = True
                    if col5Button.collidepoint(mouse_pos):
                        dropPuck(5)
                        rowEnd = determinRow()
                        colEnd = determinCol()
                        dropping = True
                    if col6Button.collidepoint(mouse_pos):
                        dropPuck(6)
                        rowEnd = determinRow()
                        colEnd = determinCol()
                        dropping = True
                    if col7Button.collidepoint(mouse_pos):
                        dropPuck(7)
                        rowEnd = determinRow()
                        colEnd = determinCol()
                        dropping = True

                    if p1B.collidepoint(mouse_pos):
                        if (choice1 == "red"):
                            choice1 = "blue"
                            p1Color = (0, 0, 255)
                        elif (choice1 == "blue"):
                            choice1 = "yellow"
                            p1Color = (255, 255, 0)
                        elif (choice1 == "yellow"):
                            choice1 = "green"
                            p1Color = (0, 255, 0)
                        elif (choice1 == "green"):
                            choice1 = "red"
                            p1Color = (255, 0, 0)
                        print(choice1)
                    if p2B.collidepoint(mouse_pos):
                        if (choice2 == "red"):
                            choice2 = "blue"
                            p2Color = (0, 0, 255)
                        elif (choice2 == "blue"):
                            choice2 = "yellow"
                            p2Color = (255, 255, 0)
                        elif (choice2 == "yellow"):
                            choice2 = "green"
                            p2Color = (0, 255, 0)
                        elif (choice2 == "green"):
                            choice2 = "red"
                            p2Color = (255, 0, 0)
                        print(choice1)

            # if event object type is QUIT
            # then quitting the pygame
            # and program both.
            if event.type == pygame.QUIT :
                # deactivates the pygame library
                pygame.quit()
                # quit the program.
                quit()
    
            # Draws the surface object to the screen.  
        pygame.display.update() 


if __name__ == '__main__':
    main()
