   
class piece_pacakge_info: 
     
     def __init__(self,piece_type,coors,obs): 
        self.piece = peice 
        sellf.piece_type = piece_type
        self.coors = coors 
        self.obs = obs 
 

   def map_check(piece_mappings,obs_locs): 
        """checks that given piece map satisfies contrains of obervation"""
        for piece in piece_mappings:
            for obs_pieces in obs_locs:  
                if piece[0] == obs_pieces[0]: #match in piece type i.e both have same tag (wumpus, hero, mage) 
                    for neighs in self.board[obs_pieces[1][0]][obs_pieces[1][1]]: #checks that piece in obs is in corresponding range specfied by obs
                        if piece[1] == neights:
                            return True 
       
       # if don't verify that the piece locations in map lie within the constrained range given by the observation list, the list is invalid 
        return False  
                       

            



   def piece_space_map(vec_piece,no_pieces,obs_loc): 
        """" this function will take a set of pieces and map them to all posiblle lcoations on the board  """
        open_spaces = [None]*0 
        
        for i in range(self.side): 
            for j in range(self.side): 
                if self.board[i][j].player == "neutral" and self.board[i][j].unit != "pit": 
                    open_spaces.append([i,j])  
        
        """each for loop correpodns to the number of pieces that we have to generate spaces for. 
           We are mapping a fector of pieces that are represented by chars to the generated positions."""
        
        if no_pieces == 2:  
            for op in open_spaces: 
                for op2 in open_spaces: 
                    if( map_check(obs_loc, [[vec_piece[0],op ], [vec_piece[1], op2]])):
                        prob_func([[vec_piece[0],op ], [vec_piece[1], op2]])
        
        elif no_pieces == 3: 
            for op in open_spaces: 
                for op2 in open_spaces:
                    for op3 in open_spaces:
                        if( map_check(obs_loc, [[vec_piece[0],op ], [vec_piece[1], op2], [vec_piece[2],op3] ])):
                            prob_func([[vec_piece[0],op ], [vec_piece[1], op2],[vec_piece[2],op3]])
        
        elif no_pieces == 4: 
            for op in open_spaces: 
                for op2 in open_spaces:
                    for op3 in open_spaces:
                        for op4 in open_spaces:
                            if( map_check(obs_loc, [[vec_piece[0],op ], [vec_piece[1], op2], [vec_piece[2],op3], [vec_piece[3],op4] ])):
                                prob_func([[vec_piece[0],op ], [vec_piece[1], op2],[vec_piece[2],op3],[vec_piece[3],op4]]) 
            
        elif no_pieces == 5: 
            for op in open_spaces: 
                for op2 in open_spaces:
                      for op3 in open_spaces:
                            for op4 in open_spaces:
                                for op5 in open_spaces: 
                                    if( map_check(obs_loc, [[vec_piece[0],op ], [vec_piece[1], op2], [vec_piece[2],op3], [vec_piece[3],op4], [vec_piece[4],op5] ])):
                                        prob_func([[vec_piece[0],op ], [vec_piece[1], op2],[vec_piece[2],op3], [vec_piece[3],op4], [vec_piece[4],op5]]) 
 

        else: 
            for op in open_spaces: 
                for op2 in open_spaces:
                      for op3 in open_spaces:
                            for op4 in open_spaces:
                                for op5 in open_spaces:
                                    for op6 in open_spaces:
                                        if( map_check(obs_loc, [[vec_piece[0],op ], [vec_piece[1], op2], [vec_piece[2],op3], [vec_piece[3],op4], [vec_piece[4],op5],[vec_piece[5],op6]])):
                                            prob_func([[vec_piece[0],op ], [vec_piece[1], op2], [vec_piece[2],op3], [vec_piece[3],op4], [vec_piece[4],op5],[vec_piece[5],op6]])






        #self.pValues = [0, 0, 0, 0]
        #Legend:
        #first(0) index corresponds to probability of enemy hero in adjacent tile
        #second(1) index corresponds to probability of enemy mage in adjacent tile
        #third(2) index corresponds to probability of enemy wumpus in adjacent tile
        #fourth(3) index corresponds to probability of pit in adjacent tile













    object list piece_map: 
	
	tuple: ( (M,(x,y)) , (H,(x',y')) ...) 
	piece_types: [M, W, H]   

    def prob_function(piece_map):
	
        
        m = number of mages on board 

        w = number of wumpuses on board
        h = number of heros on board

        for type in piece_map.piece_types:
            norm_f = norm_factor(piece_type)
            norm_factors.append(norm_f)

        "We have now compute all the normalization factors we need above" 

        prod = 1
        
        for t in tuple:
            if t.p_type == W:
                prod*= norm_w * P(W,x,y) * w 
                w = w -1 
            else if t.p_type == H: 
                prob *=  norm_h * P(H,x,y) * h 
                h = h - 1 
            else: 
                prob *=  norm_m * P(M,x,y) * m
                m = m - 1 

        return prod





























































































