import pygame
from pygame.locals import *
from random import randint

h = 10

iADifficulty = 0

posXenemy = 420
posYenemy = 10

posX = 420
posY = 500

size = 30
espacement = 15

nbrboat = 5
listBoats = [2, 3, 3, 4, 5]  # list des bateaux connu par leurs index et leur valeurs correspondent a leur taille

pts = 0
ptsennemy = 0

width = 1200
height = 960

white = (255, 255, 255)
black = (0, 0, 0)
grey = (128, 128, 128)
red = (128, 0, 0)
green = (0, 128, 0)
blue = (0, 0, 128)


def init_board(board):
    for i in range(0, h):
        board.append([0] * h)


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, (len(board[0]) - 1))


def setupEnnemyBoat(board, listBoats):
    k = 0
    while (k < len(listBoats)):
        row = random_row(board)
        col = random_col(board)
        taille = listBoats[k]
        if (board[row][col] == 0):
            cptrow = 0
            cptcol = 0
            cptrow2 = 0
            cptcol2 = 0
            for i in range(taille):
                if (row + taille < len(board) - 1 and board[row + i][col] == 0):
                    cptrow = cptrow + 1
            for j in range(taille):
                if (col + taille < len(board[0]) - 1 and board[row][col + j] == 0):
                    cptcol = cptcol + 1
            for i in range(taille):
                if (0 < row - taille and board[row - i][col] == 0):
                    cptrow2 = cptrow2 + 1
            for j in range(taille):
                if (0 < col - taille and board[row][col - j] == 0):
                    cptcol2 = cptcol2 + 1

            if (cptrow == taille):
                for i in range(taille):
                    board[row + i][col] = 1
                k = k + 1
                print('check1' + str(k))
            elif (cptcol == taille):
                for j in range(taille):
                    board[row][col + j] = 1
                k = k + 1
                print('check2' + str(k))
            elif (cptrow2 == taille):
                for i in range(taille):
                    board[row - i][col] = 1
                k = k + 1
                print('check3' + str(k))
            elif (cptcol2 == taille):
                for j in range(taille):
                    board[row][col - j] = 1
                k = k + 1
                print('check4' + str(k))
        else:
            print('error01')


# def generateEnemy(listBoat, ennemyBoard):
#
#    row = 0
#    col = 0
#    for i in range(len(listBoat)): # 5 ships in enemy
#        horizontal = randint(0,1)
#        if(horizontal):
#            while ((col + listBoat[i] < len(ennemyBoard[1]) -1)):
#                row = randint(0, len(ennemyBoard[0]) - 2)  # this shouldnt be problematic here
#                col = randint(0, len(ennemyBoard[1]) - 2)  # must check if ship will fit
#                for j in range(listBoat[i]):  # if no ships are already there
#                    if ennemyBoard[row][col + j] == 1:
#                        col = 0
#            for j in range(listBoat[i]):  # place ships
#                ennemyBoard[row][col + j] = 1
#        else:
#            while ((row + listBoat[i] < len(ennemyBoard[0]) - 1)):
#                col = randint(0, len(ennemyBoard[1]) - 2)  # this shouldnt be problematic here
#                row = randint(0, len(ennemyBoard[0]) - 2)  # must check if ship will fit
#                for j in range(listBoat[i]):  # if no ships are already there
#                    if ennemyBoard[row + j][col] == 1:
#                        row = 0
#            for j in range(listBoat[i]):  # place ships
#                ennemyBoard[row + j][col] = 1
#


def setupboat(screen, board, listboats):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    loop = 0
    while (loop < 40):

        if (click[0] == 1):
            loop = loop + 1
        for i in range(h):

            if (posX + i * (size + espacement) < mouse[0] < posX + size + i * (size + espacement) and posY < mouse[
                1] < posY + size):
                pygame.draw.rect(screen, grey, (posX + i * (size + espacement), posY, size, size))

                if (click[0] == 1):
                    loop = False




            else:
                pygame.draw.rect(screen, black, (posX + i * (size + espacement), posY, size, size))

            for j in range(h):
                if (posX + i * (size + espacement) < mouse[0] < posX + size + i * (size + espacement) and posY + j * (
                        size + espacement) < mouse[1] < posY + size + +j * (size + espacement)):
                    pygame.draw.rect(screen, grey,
                                     (posX + i * (size + espacement), posY + j * (size + espacement), size, size))

                    if (click[0] == 1):
                        loop = False


                else:
                    pygame.draw.rect(screen, black,
                                     (posX + i * (size + espacement), posY + j * (size + espacement), size, size))
        pygame.display.update()


def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    mainloop(screen)


def mainloop(screen):
    imagetest = pygame.image.load('bateau01.png')
    imagetest = pygame.transform.scale(imagetest, (100, 100))

    fondEcran = pygame.image.load('bateau.jpg')
    fondEcran = pygame.transform.scale(fondEcran, (1200, 960))

    font = pygame.font.Font(None, 150)
    title = font.render(" ", 1, (0, 128, 255))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        Start(screen, 'bateau01.png', 'ancre.png', 550, 800, fondEcran, title)

        #        render ( screen, bonus, snake_parts)
        #
        #        pygame.draw.rect ( screen, white, (42, 42, 64, 24 ))
        pygame.display.update()
    pygame.quit()


def Start(screen, img, img2, x, y, fondEcran, title):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if (x + 100 > mouse[0] > x and y + 100 > mouse[1] > y):
        imagetest = pygame.image.load(img)
        imagetest = pygame.transform.scale(imagetest, (120, 120))
        screen.blit(fondEcran, (0, 0))
        screen.blit(imagetest, (x - 10, y - 10))
        screen.blit(title, (350, 15))
        if (click[0] == 1):
            GameLoop(screen)

    else:
        imagetest = pygame.image.load(img)
        imagetest = pygame.transform.scale(imagetest, (100, 100))
        screen.blit(fondEcran, (0, 0))
        screen.blit(imagetest, (550, 800))
        screen.blit(title, (350, 15))

    if (x + 100 + 250 > mouse[0] > x + 250 and y + 100 > mouse[1] > y):

        if (click[0] == 1):
            difficultyLoop(screen)

    imagetest2 = pygame.image.load(img2)
    imagetest2 = pygame.transform.scale(imagetest2, (100, 100))
    screen.blit(imagetest2, (800, 800))


def GameLoop(screen):
    board = []
    boardennemy = []
    global pts
    pts = 0
    global ptsennemy
    ptsennemy = 0
    init_board(board)
    init_board(boardennemy)
    setupEnnemyBoat(boardennemy, listBoats)
    #    generateEnemy(listBoats, boardennemy)
    print_board(boardennemy)

    boatplaced = 0

    tryboard = []
    init_board(tryboard)
    tryboardennemy = []
    init_board(tryboardennemy)

    fondEcran = pygame.image.load('sea.jpg')
    fondEcran = pygame.transform.scale(fondEcran, (1200, 960))

    screen.blit(fondEcran, (0, 0))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                #            ToDo event sur les touches du clavier pour deplacer le curseur

        #########################################################################Placement des bateaux###################################################
        #################################################################################################################################################
        #################################################################################################################################################
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (boatplaced < 5):
            pygame.draw.rect(screen, grey, (0, 250, 300, 50))
            font = pygame.font.Font(None, 40)
            title = font.render("Place your ships!", 1, (250, 250, 250))
            screen.blit(title, (0, 250))
        else:
            pygame.draw.rect(screen, grey, (0, 250, 300, 50))
            font = pygame.font.Font(None, 40)
            title = font.render("Play!", 1, (250, 250, 250))
            screen.blit(title, (0, 250))
        if (pts == 17):
            pygame.draw.rect(screen, grey, (0, 250, 300, 50))
            font = pygame.font.Font(None, 40)
            title = font.render("You are victorious!", 1, (250, 250, 250))
            screen.blit(title, (0, 250))
        if (ptsennemy == 17):
            pygame.draw.rect(screen, grey, (0, 250, 300, 50))
            font = pygame.font.Font(None, 40)
            title = font.render("You have lost!", 1, (250, 250, 250))
            screen.blit(title, (0, 250))

        for i in range(h):

            if (posX + i * (size + espacement) < mouse[0] < posX + size + i * (size + espacement) and posY < mouse[
                1] < posY + size):
                pygame.draw.rect(screen, grey, (posX + i * (size + espacement), posY, size, size))

                if (click[0] == 1 and boatplaced < 5):
                    row = i
                    col = 0
                    taille = listBoats[boatplaced]
                    if (board[row][col] == 0):
                        cptrow = 0

                        cptrow2 = 0

                        for i in range(taille):
                            if (row + taille < len(board) - 1 and board[row + i][col] == 0):
                                cptrow = cptrow + 1

                        for i in range(taille):
                            if (0 < row - taille and board[row - i][col] == 0):
                                cptrow2 = cptrow2 + 1

                        if (cptrow == taille):
                            for i in range(taille):
                                board[row + i][col] = 1
                            boatplaced = boatplaced + 1
                            print('check1' + str(boatplaced))


                        elif (cptrow2 == taille):
                            for i in range(taille):
                                board[row - i][col] = 1
                            boatplaced = boatplaced + 1
                            print('check3' + str(boatplaced))

                if (click[2] == 1 and boatplaced < 5):
                    row = i
                    col = 0
                    taille = listBoats[boatplaced]
                    if (board[row][col] == 0):
                        cptcol = 0
                        cptcol2 = 0
                        for j in range(taille):
                            if (col + taille < len(board[0]) - 1 and board[row][col + j] == 0):
                                cptcol = cptcol + 1
                        for j in range(taille):
                            if (0 < col - taille and board[row][col - j] == 0):
                                cptcol2 = cptcol2 + 1

                        if (cptcol == taille):
                            for j in range(taille):
                                board[row][col + j] = 1
                            boatplaced = boatplaced + 1
                            print('check2' + str(boatplaced))

                        elif (cptcol2 == taille):
                            for j in range(taille):
                                board[row][col - j] = 1
                            boatplaced = boatplaced + 1
                            print('check4' + str(boatplaced))




            else:
                pygame.draw.rect(screen, black, (posX + i * (size + espacement), posY, size, size))

            for j in range(h):
                if (posX + i * (size + espacement) < mouse[0] < posX + size + i * (size + espacement) and posY + j * (
                        size + espacement) < mouse[1] < posY + size + +j * (size + espacement)):
                    pygame.draw.rect(screen, grey,
                                     (posX + i * (size + espacement), posY + j * (size + espacement), size, size))

                    if (click[0] == 1 and boatplaced < 5):
                        row = i
                        col = j
                        taille = listBoats[boatplaced]
                        if (board[row][col] == 0):
                            cptrow = 0
                            cptrow2 = 0

                            for i in range(taille):
                                if (row + taille < len(board) - 1 and board[row + i][col] == 0):
                                    cptrow = cptrow + 1

                            for i in range(taille):
                                if (0 < row - taille and board[row - i][col] == 0):
                                    cptrow2 = cptrow2 + 1

                            if (cptrow == taille):
                                for i in range(taille):
                                    board[row + i][col] = 1
                                boatplaced = boatplaced + 1
                                print('check1' + str(boatplaced))


                            elif (cptrow2 == taille):
                                for i in range(taille):
                                    board[row - i][col] = 1
                                boatplaced = boatplaced + 1
                                print('check3' + str(boatplaced))

                    if (click[2] == 1 and boatplaced < 5):
                        row = i
                        col = j
                        taille = listBoats[boatplaced]
                        if (board[row][col] == 0):
                            cptcol = 0
                            cptcol2 = 0
                            for j in range(taille):
                                if (col + taille < len(board[0]) - 1 and board[row][col + j] == 0):
                                    cptcol = cptcol + 1
                            for j in range(taille):
                                if (0 < col - taille and board[row][col - j] == 0):
                                    cptcol2 = cptcol2 + 1
                            if (cptcol == taille):
                                for j in range(taille):
                                    board[row][col + j] = 1
                                boatplaced = boatplaced + 1
                                print('check' + str(boatplaced))
                            elif (cptcol2 == taille):
                                for j in range(taille):
                                    board[row][col - j] = 1
                                boatplaced = boatplaced + 1
                                print('check' + str(boatplaced))



                else:
                    pygame.draw.rect(screen, black,
                                     (posX + i * (size + espacement), posY + j * (size + espacement), size, size))
        ####################################################################################################################################################↨
        ####################################################################################################################################################↨
        ####################################################################################################################################################↨

        setup(screen, tryboard, tryboardennemy, boardennemy, boatplaced, board)
        ennemysetup(screen, tryboard, board)
        rebuild(screen, tryboard, tryboardennemy)

        #        end(screen)

        pygame.display.update()


def ennemysetup(screen, tryboard, board):
    global pts
    global ptsennemy

    for i in range(h):
        if (board[i][0] == 1 and pts < 17):
            pygame.draw.rect(screen, blue, (posX + i * (size + espacement), posY, size, size))
        else:
            pygame.draw.rect(screen, black, (posX + i * (size + espacement), posY, size, size))

        for j in range(h):

            if (board[i][j] == 1 and pts < 17):
                pygame.draw.rect(screen, blue,
                                 (posX + i * (size + espacement), posY + j * (size + espacement), size, size))
            else:
                pygame.draw.rect(screen, black,
                                 (posX + i * (size + espacement), posY + j * (size + espacement), size, size))


def setup(screen, tryboard, tryboardennemy, boardennemy, boatplaced, board):
    global pts
    global ptsennemy
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    for i in range(h):

        if (posXenemy + i * (size + espacement) < mouse[0] < posXenemy + size + i * (size + espacement) and posYenemy <
                mouse[1] < posYenemy + size and tryboard[i][0] == 0 and boatplaced == 5 and pts < 17):
            pygame.draw.rect(screen, grey, (posXenemy + i * (size + espacement), posYenemy, size, size))

            if (click[0] == 1):

                if (boardennemy[i][0] == 1):
                    tryboard[i][0] = 1
                    pts = pts + 1

                else:
                    tryboard[i][0] = 2

                row = random_row(boardennemy)
                col = random_col(boardennemy)
                while (tryboardennemy[row][col] == 1):
                    row = random_row(boardennemy)
                    col = random_col(boardennemy)

                if (board[row][col] == 1):
                    tryboardennemy[i][0] = 1
                    ptsennemy = ptsennemy + 1

                else:
                    tryboardennemy[row][col] = 2


        else:
            pygame.draw.rect(screen, black, (posXenemy + i * (size + espacement), posYenemy, size, size))

        for j in range(h):
            if (posXenemy + i * (size + espacement) < mouse[0] < posXenemy + size + i * (
                    size + espacement) and posYenemy + j * (size + espacement) < mouse[1] < posYenemy + size + +j * (
                    size + espacement) and tryboard[i][j] == 0 and boatplaced == 5 and pts < 17):
                pygame.draw.rect(screen, grey,
                                 (posXenemy + i * (size + espacement), posYenemy + j * (size + espacement), size, size))

                if (click[0] == 1):
                    if (boardennemy[i][j] == 1):
                        tryboard[i][j] = 1
                        pts = pts + 1
                    else:
                        tryboard[i][j] = 2

                    row = random_row(boardennemy)
                    col = random_col(boardennemy)
                    while (tryboardennemy[row][col] == 1 or tryboardennemy[row][col] == 2):
                        row = random_row(boardennemy)
                        col = random_col(boardennemy)

                    if (board[row][col] == 1):
                        tryboardennemy[row][col] = 1
                        ptsennemy = ptsennemy + 1

                    else:
                        tryboardennemy[row][col] = 2

            else:
                pygame.draw.rect(screen, black,
                                 (posXenemy + i * (size + espacement), posYenemy + j * (size + espacement), size, size))


def difficultyLoop(screen):
    running = True

    global iADifficulty

    fondEcran = pygame.image.load('sea.jpg')
    fondEcran = pygame.transform.scale(fondEcran, (1200, 960))

    font = pygame.font.Font(None, 150)
    fontbis = pygame.font.Font(None, 50)
    title = font.render("Difficulty", 1, (0, 0, 0))
    choice1 = fontbis.render("Easy", 1, (0, 0, 0))
    choice2 = fontbis.render("Advanced", 1, (0, 0, 0))

    #    if ()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                #            ToDo event sur les touches du clavier pour deplacer le curseur
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        screen.blit(fondEcran, (0, 0))
        screen.blit(title, (50, 500))
        screen.blit(choice1, (700, 150))
        screen.blit(choice2, (700, 350))

        if (1000 > mouse[0] > 700 and 250 > mouse[1] > 150):

            if (click[0] == 1):
                iADifficulty = 0
                running = False
        if (1000 > mouse[0] > 700 and 450 > mouse[1] > 350):

            if (click[0] == 1):
                iADifficulty = 1
                running = False

        pygame.display.update()


def rebuild(screen, tryboard, tryboardennemy):
    for i in range(len(tryboard)):
        for j in range(len(tryboard[0])):
            if (tryboard[i][j] == 1):
                pygame.draw.rect(screen, red,
                                 (posXenemy + i * (size + espacement), posYenemy + j * (size + espacement), size, size))
            if (tryboard[i][j] == 2):
                pygame.draw.rect(screen, white,
                                 (posXenemy + i * (size + espacement), posYenemy + j * (size + espacement), size, size))

    for i in range(len(tryboardennemy)):
        for j in range(len(tryboardennemy[0])):
            if (tryboardennemy[i][j] == 1):
                pygame.draw.rect(screen, red,
                                 (posX + i * (size + espacement), posY + j * (size + espacement), size, size))
            if (tryboardennemy[i][j] == 2):
                pygame.draw.rect(screen, white,
                                 (posX + i * (size + espacement), posY + j * (size + espacement), size, size))


def end(screen):
    global pts
    global ptsennemy
    if (pts == 17 or ptsennemy == 17):
        screen.fill(white)
        font = pygame.font.Font(None, 150)
        if (pts == 17):
            title = font.render("Gagné", 1, (0, 0, 0))
        if (ptsennemy == 17):
            title = font.render("Perdu", 1, (0, 0, 0))

        screen.blit(title, (400, 15))


def print_board(board):
    for row in board:
        print(" ".join(str(row)))


# guess_row = int(input( "Guess row :"))
# guess_col = int(input( "Guess col :"))

# print (ship_row)
# print (ship_col)
#
# if guess_row == ship_row and guess_col == ship_col :
#    print ("congratulation you sank my battleship!")
#
# else :
#    print (" you missed")
main()