# -*- coding: utf-8 -*-
"""
This is the MiniMax search Algorithm
""" 
import numpy as np
import math

def euclid_dist(p1,p2):
    return  np.sqrt((p1[0]-p2[0])^2 + (p1[1]-p2[1])^2)
    
def matchup(p_type,adv_type):
    if p_type == adv_type:
        return "draw"
    else:
        if adv_type == "Mage":
            if p_type == "Wumpus":
                return "Win"
            else:
                return "Loss"
        elif adv_type == "Wumpus":
            if p_type == "Hero":
                return "Win"
            else:
                return "Loss"
        else:
            if p_type == "Mage":
                return "Win"
            else:
                return "Loss"

                
""" 
def closest_m(pos, peice_type, m_type):
    if m_type = win:
        win_matchups = []  
        for w_m in win_matchups: 
            m_loss = [None]*0
            positions  = move_set(w_m) 
            for moves in position:
                if matchup(moves) == "Loss":
                    m_loss.append(moves) 
        
        if len(m_loss) == 0:
            return min(euclid_dist(pos,m_1),euclid_dist(pos,m_1),\ 
                   euclid_dist(pos,m_3)) 
        else: 
            
    else:
        draw_matchups = [] 
        return min(euclid_dist(pos,m_1),euclid_dist(pos,m_1),\ 
                   euclid_dist(pos,m_3))


def static_eval(position,p_type): 
    
    return 0.25 * pieces_left + 0.25 * closest_m(pos,p_type,"draw") 
    + 0.50 * closest_m(pos,p_type,"win")

"""    
    

def move_set(pos): # possible move
    
    p_m= [[pos[0]-1, pos[1]], [pos[0]+1, pos[1]], [pos[0], pos[1]+1], [pos[0],\
           pos[1]-1], [pos[0]-1, pos[1]+1], [pos[0]+1, 
           pos[1]-1], [pos[0]-1, pos[1]-1],[pos[0]+1, pos[1]+1]]
    
    out_m = [None]*0
    for move in p_m:
        if p_m[0] > 0 and p_m[1] > 0:
            out_m.append(p_m)
            
    return out_m
    
    
#
def minimax(position, tree_depth, maximizingPlayer):
     if tree_depth == 0 or goal(position,p_type): 
         return static_eval(position) #static evaluation
     if maximizingPlayer:
         MaxOut = -inf
         p_moves = mov_set(position)
         for move in p_moves: # all spaces within one move of current pos
             currEval = minimax(move, tree_depth − 1, False)
             MaxOut = max(MaxOut,currEval)
         return MaxOut
     
     else: 
         MinOut = inf
         p_moves = move_set(position)
         for move in p_moves:
             currEval = minimax(move, tree_depth − 1, True)
             MinOut = min(MinOut,currEval)
         return MinOut
 
def AB_minimax(position, tree_depth, alpha, beta, maximizingPlayer):
     if tree_depth == 0 or goal(position,p_type): 
         return static_eval(position) #static evaluation
     if maximizingPlayer:
         MaxOut = -inf
         p_moves = mov_set(position)
         for move in p_moves: # all spaces within one move of current pos
             currEval = minimax(move, tree_depth − 1, False)
             MaxOut = max(MaxOut,currEval) 
             alpha = max(alpha,currEval) 
             
             if beta < alpha or beta == alpha:
                 break
         
         return MaxOut
     
     else: 
         MinOut = inf
         p_moves = move_set(position)
         for move in p_moves:
             currEval = minimax(move, tree_depth − 1, True)
             MinOut = min(MinOut,currEval)
             beta  = min(beta, currEval)
             if beta < alpha or beta == alpha:
                 break
         return MinOut



"""
def alphabeta(node, depth, alpha, beta, maximizingPlayer): 

    if depth = 0 or node is a terminal node: 
        
        return  static_eval(node) #the heuristic value of node
   
    if maximizingPlayer: 
        
        value = −inf 
        prioirty_queue ={}
        
        for each child of node:
                prioirty_queue.push(child,h(child))
        
        while child == prioirty_queue.pop():
                
                value = max(value, alphabeta(child, depth − 1, alpha, beta, FALSE)) 
                alpha = max(alpha, value)
                
                if alpha > beta or alpha = beta:
                      break #(* β cut-off *) 
                
                return value
    else
        
        value = inf 
        prioirty_queue:={}
        
        for each child of node:
            prioirty_queue.push(child, -h(child)) 
        
        while child == prioirty_queue.pop(): 
            
            value = min(value, alphabeta(child, depth − 1, alpha, beta, TRUE))           
            beta = min(beta, value) 
            
            if beta < alpha or beta = alpha:
                    break #(* α cut-off *)
        
        return value
"""