import pygame
import sys
import math
import os
import random 
import numpy as np
from queue import PriorityQueue



class piece_pacakge_info: 
     
     def __init__(self,piece_type,coors,obs): 
        self.piece = peice 
        sellf.piece_type = piece_type
        self.coors = coors 
        self.obs = obs 
    


#Tile Object for each tile in the gameboard

class Tile:
    #load in images

    #Anthony Code:
    '''images = [
        pygame.image.load("C:/PYTHONSTUFF/Wumpus/imgs/bluewumpus.png"),
        pygame.image.load("C:/PYTHONSTUFF/Wumpus/imgs/bluewizard.png"),
        pygame.image.load("C:/PYTHONSTUFF/Wumpus/imgs/bluehero.png"),
        pygame.image.load("C:/PYTHONSTUFF/Wumpus/imgs/redwumpus.png"),
        pygame.image.load("C:/PYTHONSTUFF/Wumpus/imgs/redwizard.jpg"),
        pygame.image.load("C:/PYTHONSTUFF/Wumpus/imgs/redhero.png")
    ]'''

    images = [
        pygame.image.load("imgs/bluewumpus.png"),
        pygame.image.load("imgs/bluewizard.png"),
        pygame.image.load("imgs/bluehero.png"),
        pygame.image.load("imgs/redwumpus.png"),
        pygame.image.load("imgs/redwizard.jpg"),
        pygame.image.load("imgs/redhero.png")
    ]

    def __init__(self, rowval, colval):
        self.unit = "empty"
        self.player = "neutral"
        self.neighbors = []
        self.rowval = rowval
        self.colval = colval
        self.img = self.images[0]

        #observations in order: hero, mage, wumpus, pit
        self.OBSV = [0, 0, 0, 0]
        #Legend:
        #first(0) index corresponds to enemy hero in adjacent tile
        #second(1) index corresponds to enemy mage in adjacent tile
        #third(2) index corresponds to enemy wumpus in adjacent tile
        #fourth(3) index corresponds to pit in adjacent tile

        #These will automatically be made for each tile every round: requires no input for algorithm

        self.pValues = [0, 0, 0, 0]
        #Legend:
        #first(0) index corresponds to probability of enemy hero in adjacent tile
        #second(1) index corresponds to probability of enemy mage in adjacent tile
        #third(2) index corresponds to probability of enemy wumpus in adjacent tile
        #fourth(3) index corresponds to probability of pit in adjacent tile

        #These will need to be manually calculated by the algorithm, then updated every round


    def show(self, screen, color, w, h, playerType):
        #pygame.draw.rect(screen, color, (self.colval * w, self.colval * w, w, h), 0)
        if playerType == "wumpus":
            self.img = self.images[0]
            self.img = pygame.transform.scale(self.img, (int(w), int(h)))
            imageRect = self.img.get_rect()
            screen.blit(self.img, (self.colval * w, self.rowval * h), imageRect)
            #screen.blit(self.img, [self.colval * w, self.rowval*h])
        if playerType == "mage":
            self.img = self.images[1]
            self.img = pygame.transform.scale(self.img, (int(w), int(h)))
            imageRect = self.img.get_rect()
            screen.blit(self.img, (self.colval * w, self.rowval * h), imageRect)
            #screen.blit(self.img, [self.colval * w, self.rowval*h])
        if playerType == "hero":
            self.img = self.images[2]
            self.img = pygame.transform.scale(self.img, (int(w), int(h)))
            imageRect = self.img.get_rect()
            screen.blit(self.img, (self.colval * w, self.rowval * h), imageRect)
            #screen.blit(self.img, [self.colval * w, self.rowval * h])
        if playerType == "wumpus-agent":
            self.img = self.images[3]
            self.img = pygame.transform.scale(self.img, (int(w), int(h)))
            imageRect = self.img.get_rect()
            screen.blit(self.img, (self.colval * w, self.rowval * h), imageRect)
        if playerType == "mage-agent":
            self.img = self.images[4]
            self.img = pygame.transform.scale(self.img, (int(w), int(h)))
            imageRect = self.img.get_rect()
            screen.blit(self.img, (self.colval * w, self.rowval * h), imageRect)
        if playerType == "hero-agent":
            self.img = self.images[5]
            self.img = pygame.transform.scale(self.img, (int(w), int(h)))
            imageRect = self.img.get_rect()
            screen.blit(self.img, (self.colval * w, self.rowval * h), imageRect)
        if playerType == "empty":
            pygame.draw.rect(screen, color, (self.colval * w, self.rowval * h, w, h), 0)
        if playerType == "pit":
            pygame.draw.rect(screen, color, (self.colval * w, self.rowval * h, w, h), 0)
        
        pygame.draw.line(screen, (0,0,0), [self.colval * w, self.rowval*h], [self.colval * w + w, self.rowval*h], 1)
        pygame.draw.line(screen, (0,0,0), [self.colval * w, self.rowval*h], [self.colval * w, self.rowval*h + h], 1)
        pygame.display.update()


    #this function will filter the tile into 4 different pieces, with a filter on representing an observation
    def showOBSV(self, screen, h, player):
        
        #creating screen rectangles based on the four quadrants of the tile
        heroRect = pygame.Rect(self.colval * h, self.rowval * h, h/2, h/2)
        mageRect = pygame.Rect(self.colval * h + h/2, self.rowval * h, h/2, h/2)
        wumpusRect = pygame.Rect(self.colval * h, self.rowval * h + h/2, h/2, h/2)
        pitRect = pygame.Rect(self.colval * h + h/2, self.rowval * h + h/2, h/2, h/2)

        #fills the visualization area with a filtered image if an observation is present
        if self.OBSV[0] == 1:
            screen.fill((255, 120, 120), heroRect, pygame.BLEND_RGB_MULT)
        if self.OBSV[1] == 1:
            screen.fill((102, 204, 0), mageRect, pygame.BLEND_RGB_MULT)
        if self.OBSV[2] == 1:
            screen.fill((120, 120, 255), wumpusRect, pygame.BLEND_RGB_MULT)
        if self.OBSV[3] == 1:
            screen.fill((210, 105, 30), pitRect, pygame.BLEND_RGB_MULT)


        pygame.draw.line(screen, (0,0,0), [self.colval * h, self.rowval*h], [self.colval * h + h, self.rowval*h], 1)
        pygame.draw.line(screen, (0,0,0), [self.colval * h, self.rowval*h], [self.colval * h, self.rowval* h + h], 1)
        pygame.display.update()
        return

    #this function checks if the observation that a given tile receives is consistent with its neighboring pieces/pits.
    def filtering(self, screen, h, player):
		
        possible_hero_tiles = [None]*0
        consistent_hero = [None]*0
        possible_mage_tiles = [None]*0
        consistent_mage = [None]*0
        possible_wumpus_tiles = [None]*0
        consistent_wumpus = [None]*0
        possible_pit_tiles = [None]*0
        consistent_pit = [None]*0
	
        for i in range(self.side):
            for j in range(self.side):
                if self.board[i][j].OBSV[0] == 1:
                    for k in self.board[i][j].neighbors:
                        possible_hero_tiles.append(self.board[i][j])
                        if self.board[i][j].player == "adversary" and self.board[i][j].unit == "hero":
                            consistent_hero.append(self.board[i][j])
                if self.board[i][j].OBSV[1] == 1:
                    for k in self.board[i][j].neighbors:
                        possible_mage_tiles.append(self.board[i][j])
                        if self.board[i][j].player == "adversary" and self.board[i][j].unit == "mage":
                            consistent_mage.append(self.board[i][j])
                if self.board[i][j].OBSV[2] == 1:
                    for k in self.board[i][j].neighbors:
                        possible_wumpus_tiles.append(self.board[i][j])
                        if self.board[i][j].player == "adversary" and self.board[i][j].unit == "wumpus":
                            consistent_wumpus.append(self.board[i][j])
                if self.board[i][j].OBSV[3] == 1:
                    for k in self.board[i][j].neighbors:
                        possible_pit_tiles.append(self.board[i][j])
                        if self.board[i][j].player == "neutral" and self.board[i][j].unit == "pit":
                            consistent_pit.append(self.board[i][j])


#Gameboard Class containing tiles indexed by row and column
class Gameboard:
    def __init__(self, side):
        self.side = side
        self.size = self.side * self.side

        #creates board 2D array of Tiles
        self.board = [[0 for i in range(self.side)] for j in range(self.side)]
        for i in range(self.side):
            for j in range(self.side):
                self.board[i][j] = Tile(i,j)

    #Set units back to starting point
    def newBoard(self):
        for i in range(self.side):
            unit = "empty"
            if i % 3 == 0:
                unit = "wumpus"
            elif i % 3 == 1:
                unit = "hero"
            else:
                unit = "mage"

            self.board[i][0].unit = unit
            self.board[i][0].player = "agent"
            self.board[i][self.side-1].unit = unit
            self.board[i][self.side-1].player = "adversary"
        
    #creates pits
    def setPits(self):
        for i in range(1, self.side-1):
            #randomly chooses colomn val
            pitcol = random.randint(0, self.side-1)
            self.board[pitcol][i].unit = "pit"

    #sets neighbors for all Tiles
    def setNeighbors(self):
        for i in range(self.side):
            for j in range(self.side):
                self.board[i][j].neighbors = []

                #goes through tiles diagonal and adjacent to the tile, and appends to neighbors list
                for k in range(-1, 2):
                    if (i+k < 0) or (i+k >= self.side):
                        continue
                    for l in range(-1, 2):
                        if (k == 0 and l == 0):
                            continue
                        if (j+l < 0) or (j+l >= self.side):
                            continue
                        self.board[i][j].neighbors.append(self.board[i + k][j + l])

    def map_check(self, piece_mappings, ops_list, given_p):
        if given_p != None:
            give_f = 0
            for maping in piece_mappings: 
                if maping[0] == given_p[0] and maping[1] == given_p[1]: 
                    give_f = 1 

            if give_f == 0:
                return False

        for maping in piece_mappings:
            for neighbor in self.board[maping[1][0]][maping[1][1]].neighbors:
                if self.board[neighbor.rowval][neighbor.colval].player == "agent":
                    is_in = 0
                    for obs_piece in obs_list:
                        if maping[0] == obs_piece[0]:
                            for neighbor2 in self.board[obs_piece[1][0]][obs_piece[1][1]].neighbors:
                                if maping[1] == neighbor2:
                                    is_in = 1
                    if(is_in == 0):
                        return False
        return True                      
    

    def piece_space_map(self, vec_piece,no_pieces,obs_loc,given_p): 
        ''' this function will take a set of pieces and map them to all posiblle lcoations on the board '''
        open_spaces = [None]*0 
        
        for i in range(self.side): 
            for j in range(self.side): 
                if self.board[i][j].player == "neutral" and self.board[i][j].unit != "pit": 
                    open_spaces.append([i,j])  
        
        """each for loop correpodns to the number of pieces that we have to generate spaces for. 
           We are mapping a fector of pieces that are represented by chars to the generated positions."""
        
        p_o = 0
        if no_pieces == 2:  
            for op in open_spaces: 
                for op2 in open_spaces: 
                    if( self.map_check(obs_loc, [[vec_piece[0],op ], [vec_piece[1], op2]],given_p)):
                        p_o += self.prob_func([[vec_piece[0],op ], [vec_piece[1], op2]])
        
        elif no_pieces == 3: 
            for op in open_spaces: 
                for op2 in open_spaces:
                    for op3 in open_spaces:
                        if( self.map_check(obs_loc, [[vec_piece[0],op ], [vec_piece[1], op2], [vec_piece[2],op3] ], given_p)):
                            p_o += self.prob_func([[vec_piece[0],op ], [vec_piece[1], op2],[vec_piece[2],op3]])
        
        elif no_pieces == 4: 
            for op in open_spaces: 
                for op2 in open_spaces:
                    for op3 in open_spaces:
                        for op4 in open_spaces:
                            if( self.map_check(obs_loc, [[vec_piece[0],op ], [vec_piece[1], op2], [vec_piece[2],op3], [vec_piece[3],op4] ],given_p )):
                                p_o += self.prob_func([[vec_piece[0],op ], [vec_piece[1], op2],[vec_piece[2],op3],[vec_piece[3],op4]]) 
            
        elif no_pieces == 5: 
            for op in open_spaces: 
                for op2 in open_spaces:
                      for op3 in open_spaces:
                            for op4 in open_spaces:
                                for op5 in open_spaces: 
                                    if( self.map_check(obs_loc, [[vec_piece[0],op ], [vec_piece[1], op2], [vec_piece[2],op3], [vec_piece[3],op4], [vec_piece[4],op5] ], given_p)):
                                        p_o +=  self.prob_func([[vec_piece[0],op ], [vec_piece[1], op2],[vec_piece[2],op3], [vec_piece[3],op4], [vec_piece[4],op5]]) 
 

        elif no_pieces == 6: 
            for op in open_spaces: 
                for op2 in open_spaces:
                      for op3 in open_spaces:
                            for op4 in open_spaces:
                                for op5 in open_spaces:
                                    for op6 in open_spaces:
                                        if( self.map_check(obs_loc, [[vec_piece[0],op ], [vec_piece[1], op2], [vec_piece[2],op3], [vec_piece[3],op4], [vec_piece[4],op5],[vec_piece[5],op6]],given_p)):
                                            p_o += self.prob_func([[vec_piece[0],op ], [vec_piece[1], op2], [vec_piece[2],op3], [vec_piece[3],op4], [vec_piece[4],op5],[vec_piece[5],op6]])
            
        return p_o

        #self.pValues = [0, 0, 0, 0]
        #Legend:
        #first(0) index corresponds to probability of enemy hero in adjacent tile
        #second(1) index corresponds to probability of enemy mage in adjacent tile
        #third(2) index corresponds to probability of enemy wumpus in adjacent tile
        #fourth(3) index corresponds to probability of pit in adjacent tile


    def norm_factor(self, piece_type):
        prob_sum = float(0)
        for i in range(self.side):
            for j in range(self.side):
                if piece_type == self.board[i][j].unit:
                    if piece_type == "hero":
                        prob_sum += self.board[i][j].pValues[0]
                    elif piece_type == "mage":
                        prob_sum += self.board[i][j].pValues[0]
                    elif piece_type == "wumpus":
                        prob_sum += self.board[i][j].pValues[2]
        if prob_sum <= 0: 
            return 0
        
        return 1/float(prob_sum)    

    '''object list piece_map: 
	
	tuple: ( (M,(x,y)) , (H,(x',y')) ...) 
	piece_types: [M, W, H]   '''

    def prob_func(self, piece_map):
        #get numer of heroes, mages, and wumpus
        h = 0
        for i in range(self.side):
            for j in range(self.side):
                if self.board[i][j].unit == "hero" and self.board[i][j].player == "adversary":
                    h += 1
        m = 0
        for i in range(self.side):
            for j in range(self.side):
                if self.board[i][j].unit == "hero" and self.board[i][j].player == "adversary":
                    m += 1
        w = 0
        for i in range(self.side):
            for j in range(self.side):
                if self.board[i][j].unit == "wumpus" and self.board[i][j].player == "adversary":
                    w += 1

        norm_h = self.norm_factor("hero")
        norm_m = self.norm_factor("mage")
        norm_w = self.norm_factor("wumpus")

        "We have now compute all the normalization factors we need above" 
        prod = 1
        for piece in piece_map:
            if piece[0] == "wumpus":
                prod *= norm_w * self.board[piece[1][0]][piece[1][1]].pValues[2] * w
                w = w -1 
            elif piece[0] == "mage": 
                prob *=  norm_h *  self.board[piece[1][0]][piece[1][1]].pValues[0] * h 
                h = h - 1 
            elif piece[0] == "hero": 
                prob *=  norm_m *  self.board[piece[1][0]][piece[1][1]].pValues[1] * m
                m = m - 1 
        return prod



    def position(self, value):
    #computes the index of value in the matrix interpreation of the array
        indx = math.floor(value/self.side)
        j = -indx*self.side + value
        if j >= 0:
            return [indx, j]
        return [-1, -1]

    def inv_position(self, i, j):
    #Converts position back to an array value
        if i >= self.side or i < 0:
            return -1
        if j >= self.side or j < 0:
            return -1
        return j + i * self.side

    #modifys the observation parameters after a player makes a move
    #input is the player whose turn it is moving onto
    def modifyOBSV(self, player):
        for i in range(self.side):
            for j in range(self.side):
                if self.board[i][j].player == player:
                    for k in self.board[i][j].neighbors:
                        if k.unit == "pit":
                            self.board[j][i].OBSV[3] = 1
                        if (k.unit == "wumpus") and (k.player != player):
                            self.board[j][i].OBSV[2] = 1
                        if (k.unit == "mage") and (k.player != player):
                            self.board[j][i].OBSV[1] = 1
                        if (k.unit == "hero") and (k.player != player):
                            self.board[j][i].OBSV[0] = 1

                else:
                    self.board[j][i].OBSV = [0, 0, 0, 0]
    



pygame.init()
#Creating a GameBoard object for visualization
screen = pygame.display.set_mode((1080, 720))

BOARD = Gameboard(9)
BOARD.newBoard()
BOARD.setPits()
BOARD.setNeighbors()
BOARD.modifyOBSV("adversary")


cols = BOARD.side
row = BOARD.side
w = 720 // cols
h = 720 // row

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (220, 220, 220)
orange = (255, 102, 0)
yellow = (255, 255, 0)
purple = (102, 0, 255)

#function used to refresh a tile on visualization
def showBoardUnit(screen, board, i, j):
    global w
    global h
    #print("***************")
    #print(str(board[i][j].player) + "-" + str(board[i][j].unit))
    #print("***************")
    board[i][j].show(screen, (127,127,127), w, h, "empty")
    if board[j][i].unit == "wumpus":
        if board[j][i].player == "adversary":
            board[i][j].show(screen, green, w, h, "wumpus")
        else:
            board[i][j].show(screen, red, w, h, "wumpus-agent")
    if board[j][i].unit == "hero":
        if board[j][i].player == "adversary":
            board[i][j].show(screen, blue, w, h, "hero")
        else:
            board[i][j].show(screen, orange, w, h, "hero-agent")
    if board[j][i].unit == "mage":
        if board[j][i].player == "adversary":
            board[i][j].show(screen, purple, w, h, "mage")
        else:
            board[i][j].show(screen, yellow, w, h, "mage-agent")
    if board[j][i].unit == "pit":
        board[i][j].show(screen, purple, w, h, "pit")

#returns a victory type string based on inputted types
def matchup(p_type,adv_type):
    if adv_type == "empty" or p_type == "empty":
        return "Win"
    if p_type == adv_type:
        return "draw"
    else:
        if adv_type == "mage":
            if p_type == "wumpus":
                return "Win"
            else:
                return "Loss"
        elif adv_type == "wumpus":
            if p_type == "hero":
                return "Win"
            else:
                return "Loss"
        else:
            if p_type == "mage":
                return "Win"
            else:
                return "Loss"


#loops through entire board to create tiles
for i in range(cols):
    for j in range(row):
        showBoardUnit(screen, BOARD.board, i, j)

selectSecond = False
playerTurn = True
validDestination = False
currentplayer = "adversary"

#creates toggle fog buton, 3 by 3 button, 6 by 6 button, and 9 by 9 button
font = pygame.font.Font('freesansbold.ttf', 20)

pygame.draw.rect(screen, (250,250,250), [800, 20, 200, 40])
text1 = font.render('New 3x3', True, (0,0,0))
screen.blit(text1, (850, 20))

pygame.draw.rect(screen, (250,250,250), [800, 80, 200, 40])
text2 = font.render('New 6x6', True, (0,0,0))
screen.blit(text2, (850, 80))

pygame.draw.rect(screen, (250,250,250), [800, 140, 200, 40])
text3 = font.render('New 9x9', True, (0,0,0))
screen.blit(text3, (850, 140))

pygame.draw.rect(screen, (250,250,250), [800, 200, 200, 40])
text4 = font.render('Toggle Fog', True, (0,0,0))
screen.blit(text4, (830, 200))

pygame.draw.rect(screen, (250,250,250), [800, 260, 200, 40])
text4 = font.render('Toggle Agent Auto', True, (0,0,0))
screen.blit(text4, (810, 260))

pygame.display.update()

#variable used to determine if fog of war is currently on or off
fogStatus = False

#variable used to store selected unit
unitSelected = BOARD.board[0][0]

#variable used to store desired location
destination = BOARD.board[0][0]

#Defaults to agent automatically moving once player does a turn
autoAgentMove = True
oneMoveOnly = False

prevTile = None

#This function is linked to the visualization loop
#when mouse clicks, selects player piece, or its desired location
def mousePress(x):
    global selectSecond
    global playerTurn
    global validDestination
    global fogStatus
    global currentplayer
    global unitSelected
    global destination
    global autoAgentMove
    global oneMoveOnly
    global BOARD
    global screen
    global cols
    global row
    global w
    global h
    a = x[0]
    b = x[1]
    g1 = a // (720 // cols)
    g2 = b // (720 // row)
    global prevTile

    

    #First Click (select unit or toggle fog of war)
    if selectSecond == False:

        #OPTION 1: toggle fog
        if (a < 1000 and a > 800 and b < 240 and b > 200):
            if fogStatus:
                print("toggling off fog")
                for i in range(cols):
                    for j in range(row):
                        showBoardUnit(screen, BOARD.board, i, j)
                
                pygame.draw.rect(screen, (0,0,0), [800, 400, 200, 280])
                pygame.display.update()
                fogStatus = False
            else:
                print("toggling on fog")
                for i in range(cols):
                    for j in range(row):
                        if BOARD.board[j][i].player == currentplayer:
                            BOARD.board[i][j].showOBSV(screen, 720//cols, currentplayer)
                        else:
                            tilerect = pygame.Rect(j * h, i * h, h, h)
                            screen.fill((80, 80, 80), tilerect, pygame.BLEND_RGB_MULT)
                            pygame.display.update()
                fogStatus = True
            return

        #OPTION 2: create new 3 by 3 board
        elif (a < 1000 and a > 800 and b < 60 and b > 20):
            BOARD = Gameboard(3)
        
        #OPTION 3: create new 6 by 6 board
        elif (a < 1000 and a > 800 and b < 120 and b > 80):
            BOARD = Gameboard(6)

        #OPTION 4: create new 9 by 9 board
        elif (a < 1000 and a > 800 and b < 180 and b > 140):
            BOARD = Gameboard(9)
        
        if a < 1000 and a > 800 and ((b < 180 and b > 140) or (b < 120 and b > 80) or (b < 60 and b > 20)):
            BOARD.newBoard()
            BOARD.setPits()
            BOARD.setNeighbors()
            BOARD.modifyOBSV("adversary")
            cols = BOARD.side
            row = BOARD.side
            w = 720 / cols
            h = 720 / row
            for i in range(cols):
                for j in range(row):
                    showBoardUnit(screen, BOARD.board, i, j)
                    
            selectSecond = False
            playerTurn = True
            validDestination = False
            currentplayer = "adversary"
            fogStatus = False
            unitSelected = BOARD.board[0][0]
            destination = BOARD.board[0][0]
            autoAgentMove = True
            oneMoveOnly = False
            prevTile = None
            
            pygame.draw.rect(screen, (0,0,0), [800, 320, 200, 360])
            pygame.display.update()
            


        #OPTION 5: Shows the p values by selecting a tile when in the fog of war
        elif (g1 < cols and fogStatus == True):

            tileSelected = BOARD.board[g1][g2]
            if (tileSelected.player == "agent" and playerTurn == False) or (tileSelected.player == "adversary" and playerTurn == True):
                pygame.draw.rect(screen, (250,250,250), [800, 640, 200, 40])
                text4 = font.render("KNOWN TILE", True, (0,0,0))
                screen.blit(text4, (810, 640))

                if prevTile is not None:
                    screen.fill((80, 80, 0), prevTile, pygame.BLEND_RGB_SUB)
                prevTile = None

                pygame.display.update()
                return
                                
            #Note: tile.colval corresponds to the visualization's row, and vice versa:

            pygame.draw.rect(screen, (250,250,250), [800, 400, 200, 40])
            text4 = font.render('P(hero):' + str(tileSelected.pValues[0]), True, (255,120,120))
            screen.blit(text4, (810, 400))

            pygame.draw.rect(screen, (250,250,250), [800, 460, 200, 40])
            text4 = font.render('P(mage):' + str(tileSelected.pValues[1]), True, (102,204,0))
            screen.blit(text4, (810, 460))

            pygame.draw.rect(screen, (250,250,250), [800, 520, 200, 40])
            text4 = font.render('P(wumpus):' + str(tileSelected.pValues[2]), True, (120,120,255))
            screen.blit(text4, (810, 520))

            pygame.draw.rect(screen, (250,250,250), [800, 580, 200, 40])
            text4 = font.render('P(pit):' + str(tileSelected.pValues[3]), True, (210,105,30))
            screen.blit(text4, (810, 580))

            pygame.draw.rect(screen, (250,250,250), [800, 640, 200, 40])
            text4 = font.render("Current Tile: " + str(tileSelected.colval) + "," + str(tileSelected.rowval), True, (0,0,0))
            screen.blit(text4, (810, 640))

            
            tilerect = pygame.Rect(g1 * h, g2 * h, h, h)
            screen.fill((80, 80, 0), tilerect, pygame.BLEND_RGB_ADD)

            if prevTile is not None:
                screen.fill((80, 80, 0), prevTile, pygame.BLEND_RGB_SUB)
            prevTile = tilerect

            pygame.display.update()



        #OPTION 6: select unit
        elif (g1 < cols):
            if playerTurn == False:
                print("not your turn")
                return
            unitSelected = BOARD.board[g1][g2]
            #tests if player clicks on one of their own units, or not
            if unitSelected.player != "adversary":
                print("invalid unit")
                return
            else:
                print("selected unit")
                selectSecond = True

                tilerect = pygame.Rect(g1 * h, g2 * h, h, h)
                screen.fill((80, 80, 0), tilerect, pygame.BLEND_RGB_ADD)
                prevTile = tilerect

                pygame.display.update()

        #OPTION 7: toggle agent moving automatically
        elif (a < 1000 and a > 800 and b < 300 and b > 260):
            if fogStatus == True:
                print ("Turn off fog to toggle agent auto")
                return
            if autoAgentMove == True:
                print('toggling agent auto off')

                pygame.draw.rect(screen, (250,250,250), [800, 320, 200, 40])
                text4 = font.render('Advance Agent', True, (0,0,0))
                screen.blit(text4, (810, 320))
                pygame.display.update()

                autoAgentMove = False
                return

            if autoAgentMove == False:
                print('toggling agent auto on')
                pygame.draw.rect(screen, (0,0,0), [800, 320, 200, 40])
                pygame.display.update()
                autoAgentMove = True
                return

        #OPTION 8: advance agent move by one move
        elif (a < 1000 and a > 800 and b < 360 and b > 320 and autoAgentMove == False):
            if fogStatus == True:
                print ("Turn off fog advance the agent")
                return
            if playerTurn == True:
                print('It is your move')
                return
            oneMoveOnly = True
            autoAgentMove = True
            return


        #OPTION 9: clicking elsewhere
        else:
            print("invalid mouse press location")
            return
        



    #Second Click (choose destination of unit)
    else:
        if (g1 >= cols):
            selectSecond = False
            print("invalid destination")
            showBoardUnit(screen, BOARD.board, g2, g1)
            return
        destination = BOARD.board[g1][g2]
        #tests if destination is valid; returns to unit selection if invalid
        for neighbor in unitSelected.neighbors:
            if destination == neighbor:
                print("appropriate destination found")
                validDestination = True
        if validDestination == False:
            selectSecond = False
            print("invalid destination")
            showBoardUnit(screen, BOARD.board, g2, g1)
            return
        if destination.player == "adversary":
            selectSecond = False
            print("invalid destination")
            showBoardUnit(screen, BOARD.board, g2, g1)
            return
        if destination.unit == "pit":
            validDestination = False
            selectSecond = False
            Drow = destination.rowval
            Dcol = destination.colval
            Urow = unitSelected.rowval
            Ucol = unitSelected.colval
            print("you hit a pit")
            BOARD.board[unitSelected.rowval][unitSelected.colval].player = "neutral"
            BOARD.board[unitSelected.rowval][unitSelected.colval].unit = "empty"
            BOARD.setNeighbors()
            #showBoardUnit(screen, BOARD.board, destination., Drow)
            showBoardUnit(screen, BOARD.board, Ucol, Urow)
            pygame.display.update()
            return

        #once verifying destination, unit goes to destination 
        
        validDestination = False
        selectSecond = False
        Drow = destination.rowval
        Dcol = destination.colval
        Urow = unitSelected.rowval
        Ucol = unitSelected.colval
        print(str(unitSelected.player) + "-" + str(unitSelected.unit))
        print(str(destination.player) + "-" + str(destination.unit))

        #checks unit matchup if unit is able to take an agent's unit
        matchup = "winning"
        if destination.player == "agent":
            if destination.unit == unitSelected.unit:
                matchup = "even"
            if destination.unit == "hero" and unitSelected.unit == "wumpus": 
                matchup = "losing"
            if destination.unit == "wumpus" and unitSelected.unit == "mage": 
                matchup = "losing"
            if destination.unit == "mage" and unitSelected.unit == "hero": 
                matchup = "losing"

        #changes board according to action
        if matchup == "even":
            BOARD.board[Drow][Dcol].player = "neutral"
            BOARD.board[Drow][Dcol].unit = "empty"
            BOARD.board[Urow][Ucol].player= "neutral"
            BOARD.board[Urow][Ucol].unit = "empty"
        elif matchup == "losing":
            BOARD.board[Urow][Ucol].player= "neutral"
            BOARD.board[Urow][Ucol].unit = "empty"
        else:
            BOARD.board[Drow][Dcol].player = "adversary"
            BOARD.board[Drow][Dcol].unit = unitSelected.unit
            BOARD.board[Urow][Ucol].player= "neutral"
            BOARD.board[Urow][Ucol].unit = "empty"
        

        BOARD.setNeighbors()
        BOARD.modifyOBSV("agent")
        print("-----------")
        print(str(unitSelected.player) + "-" + str(unitSelected.unit))
        print(str(destination.player) + "-" + str(destination.unit))
        #updates visualization
        showBoardUnit(screen, BOARD.board, Dcol, Drow)
        showBoardUnit(screen, BOARD.board, Ucol, Urow)
        playerTurn = False
        currentplayer = "agent"
        pygame.display.update()






""""
From this point on we are going to include the ai for the game 
""" 

def total_pieces(GB):
    count = 0 
    for i in range(GB.side):
        for j in range(GB.side):
            if GB.board[i][j].unit != "pit" or GB.board[i][j].unit != "empty":
                count+=1
    return count

def total_pieces_player(GB, player):
    count = 0 
    for i in range(GB.side):
        for j in range(GB.side):
            if GB.board[i][j].player == player and (GB.board[i][j].unit != "pit" or GB.board[i][j].unit != "empty"):
                count+=1
    return count

def get_pieces(GB, p_type):
    
    p_loc = [None]*0
    
    if p_type == "all":
        for i in range(GB.side):
            for j in range(GB.side):
                if GB.board[i][j].player == "agent":
                    p_loc.append(GB.board[i][j])
        
    else:
        for i in range(GB.side):
            for j in range(GB.side):
                if GB.board[i][j].player == "agent":
                    if GB.board[i][j].unit == p_type:
                        p_loc.append(GB.board[i][j])
    
    if(len(p_loc)==0):
        return None
    else: 
        return p_loc 
    
def get_ADV_pieces(GB,p_type): 
    p_loc = [None]*0
    for i in range(GB.side):
            for j in range(GB.side):
                if GB.board[i][j].player == "adversary":
                    if GB.board[i][j].unit == p_type:
                        #print(GB.board[i][j].player)
                        p_loc.append(GB.board[i][j]) 
    
    return p_loc
    

def win_matchup(p_type):
    if p_type == "mage":
        return "hero"
    elif p_type == "hero":
        return "wumpus"
    else:
        return "mage"

def euclid_dist(p1,p2):
    return  np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


def closest_m(GB, pos, m_type):
    if m_type == "win": 
        #w_m = [ euclid_dist([pos.rowval,pos.colval],[p.rowval,p.colval]) 
        #for p in get_pieces(GB,win_matchup(pos.unit)) ]  
        w_m = [None]*0
        for p in get_ADV_pieces(GB,win_matchup(pos.unit)): 
            w_m.append(euclid_dist([pos.rowval,pos.colval],[p.rowval,p.colval]))
        print(pos.unit)
        for item in get_ADV_pieces(GB,win_matchup(pos.unit)):
            print([item.rowval,item.colval])
        print("\n")  
        return  min(w_m)
            
    else: 
        d_m = [ euclid_dist([pos.rowval,pos.colval],[p.rowval,p.colval]) 
        for p in get_pieces(GB,pos.unit) ]
        return min(d_m) 


def static_eval(GB,position): 
    
    return closest_m(GB,position,"win")
    #return random.randint(1,100)

def minimax(GB,position, tree_depth, maximizingPlayer):
     if tree_depth == 0 :#or goal(position,p_type):  
         #print(static_eval(GB,position)) 
         print(static_eval(GB,position))
         return static_eval(GB, position), position #static evaluation
     if maximizingPlayer:
         MaxOut = -math.inf
         p_moves = position.neighbors
         bestMove = position
         for move in p_moves:
             if move.player != "agent":
                bestMove = move 
        #print("Made it here")
         for move in p_moves:  # all spaces within one move of current pos
             if move.unit == "pit" or move.player == "agent":
                 #print("this aint good" + move.player + " " + move.unit)
                 continue    
             hold = move.unit 
             GB.board[move.rowval][move.colval].unit  = position.unit
             currEval, bs = minimax(GB,GB.board[move.rowval][move.colval]
             , tree_depth - 1, False) 
             GB.board[move.rowval][move.colval].unit = hold
             
             if MaxOut < currEval:
                 #print("Maxout "+str(MaxOut) + "currEval "+ str(currEval)) 
                 #print("Move " + str([move.rowval,move.colval]))
                 bestMove = move
                 MaxOut = currEval 
                #if tree_depth == 5: 
             #    return MaxOut, bestMove
            #MaxOut = max(MaxOut,currEval)
         return MaxOut, bestMove
     
     else: 
         MinOut = math.inf
         p_moves = position.neighbors
         bestMove = position
         for move in p_moves:
             if move.player != "agent":
                bestMove = move
         for move in p_moves:
             if move.unit == "pit" or move.player == "agent":
                 continue
             hold = move.unit 
             GB.board[move.rowval][move.colval].unit  = position.unit
             currEval, bs = minimax(GB,GB.board[move.rowval][move.colval] 
              , tree_depth - 1, True)
             GB.board[move.rowval][move.colval].unit = hold
             
             if MinOut > currEval:
                 bestMove = move
                 MinOut = currEval
             #MinOut = min(MinOut,currEval)
         return MinOut, GB.board[bestMove.rowval][bestMove.colval]


#visualization loop
while True:
    ev = pygame.event.get()
    for event in ev:

        #Commands called when game is over
        if total_pieces_player(BOARD, "agent") == 0 or total_pieces_player(BOARD, "adversary") == 0:
            print("GAME OVER!!!")
            pygame.display.quit()



        #MAIN FUNCTION FOR AGENT
        
        #most like need to put our functions here


        if playerTurn == False and autoAgentMove == True:
            
            no_pieces = 0
            vec_pieces = [None]*0
            obs_list = [None]*0
            for i in range(BOARD.side):
                for j in range(BOARD.side):
                    if BOARD.board[i][j].player == "adversary":
                        no_pieces+=1
                        vec_pieces.append( [BOARD.board[i][j].unit,[i,j]]) 
                        if BOARD.board[i][j].OBSV[0] == 1 or BOARD.board[i][j].OBSV[1] == 1 or BOARD.board[i][j].OBSV[2] == 1 or BOARD.board[i][j].OBSV[3] == 1:
                            obs_list.append([BOARD.board[i][j].unit, [i,j]]) 

            
            p_o = BOARD.piece_space_map(vec_pieces,no_pieces,obs_list,None) 
            for i in range(BOARD.side):
                for j in range(BOARD.side):
                    if BOARD.board[i][j].pvalues 


            print("agent move")
            if oneMoveOnly == True:
                print("one only")
                autoAgentMove = False
                oneMoveOnly = False
            #the unit(string value) that beats the piece that was just moved
            #pToMove = win_matchup(destination.unit) 
            #possiblePieces = get_pieces(BOARD, pToMove)
            possiblePieces = get_pieces(BOARD,"all") 
            pToMove = random.randrange(len(possiblePieces))
            while True:
                check = False
                for neighbor in possiblePieces[pToMove].neighbors:
                    if neighbor.player != "agent":
                        check = True
                if check == False:
                    pToMove = random.randrange(len(possiblePieces))
                else:
                    break
        
            #dummyVariable, destination = minimax(BOARD, possiblePieces[pToMove] 
            #, 6, True)
            #dummyVariable, destination = alphaBetaPruningPQ(BOARD, possiblePieces[pToMove] 
            #, 3, 0, 0, True)
            unitSelected = possiblePieces[pToMove] 
            #print("output from minimax"+ str(dummyVariable))
            print("final move"+ str([destination.rowval,destination.colval]))
            Drow = destination.rowval
            Dcol = destination.colval
            Urow = unitSelected.rowval
            Ucol = unitSelected.colval
            
            mp = "winning"
            if destination.player == "adversary":
                if destination.unit == unitSelected.unit:
                    mp = "even"
                if destination.unit == "hero" and unitSelected.unit == "wumpus": 
                    mp = "losing"
                if destination.unit == "wumpus" and unitSelected.unit == "mage": 
                    mp = "losing"
                if destination.unit == "mage" and unitSelected.unit == "hero": 
                    mp = "losing"

            #changes board according to action
            if mp == "even":
                BOARD.board[Drow][Dcol].player = "neutral"
                BOARD.board[Drow][Dcol].unit = "empty"
                BOARD.board[Urow][Ucol].player= "neutral"
                BOARD.board[Urow][Ucol].unit = "empty"
            elif mp == "losing":
                BOARD.board[Urow][Ucol].player= "neutral"
                BOARD.board[Urow][Ucol].unit = "empty"
            else:
                BOARD.board[Drow][Dcol].player = "agent"
                BOARD.board[Drow][Dcol].unit = unitSelected.unit
                BOARD.board[Urow][Ucol].player= "neutral"
                BOARD.board[Urow][Ucol].unit = "empty"
            

            BOARD.setNeighbors()
            BOARD.modifyOBSV("adversary")
            #updates visualization
            showBoardUnit(screen, BOARD.board, Dcol, Drow)
            showBoardUnit(screen, BOARD.board, Ucol, Urow)
            pygame.display.update()

            playerTurn = True
            currentplayer = "adversary"









        #Extraneous code
        if event.type == pygame.QUIT:
            pygame.display.quit()


        #MAIN FUNCTION FOR MOUSE CLICKING
        if pygame.mouse.get_pressed()[0]:
            try:
                pos = pygame.mouse.get_pos()
                mousePress(pos)
            except AttributeError:
                pass

        #Extraneous code
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                loop = False
                break
