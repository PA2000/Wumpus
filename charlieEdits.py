class piece_pacakge_info: 
     
    def __init__(self,piece_type,coors,obs): 
        self.piece = piece 
        self.piece_type = piece_type
        self.coors = coors 
        self.obs = obs 
 

   '''def map_check(piece_mappings,obs_locs): 
        """checks that given piece map satisfies contrains of obervation"""
        for piece in piece_mappings:
            for obs_pieces in obs_locs:  
                if piece[0] == obs_pieces[0]: #match in piece type i.e both have same tag (wumpus, hero, mage) 
                    for neighs in self.board[obs_pieces[1][0]][obs_pieces[1][1]]: #checks that piece in obs is in corresponding range specfied by obs
                        if piece[1] == neighs:
                            return True 
        


       return True             
       # if don't verify that the piece locations in map lie within the constrained range given by the observation list, the list is invalid 
       # return False  '''
    def map_check(piece_mappings, ops_list):
        for map in piece_mappings:
            for neighbor in self.board[map[1][0]][map[1][1]].neighbors:
                if self.board[neighbor[0]][neighbor[1]].player == "agent":
                    is_in = 0
                    for obs_piece in obs_list:
                        if map[0] == obs_piece[0]:
                            for neighbor2 in self.board[obs_piece[1][0]][obs_piece[1][1]].neighboors:
                                if map[1] is neighbor2:
                                    is_in = 1
                    if(is_in == 0):
                        return False
        return True                      
    

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


    def norm_factor(piece_type):
        prob_sum = float(0)
        for i in self.board.side:
            for j in self.board.side:
                if piece_type == self.board[i][j].unit:
                    if piece_type == "hero":
                        prob_sum += self.board[i][j].pValues[0]
                    elif piece_type == "mage":
                        prob_sum += self.board[i][j].pValues[0]
                    elif piece_type == "wumpus":
                        prob_sum += self.board[i][j].pValues[2]
        return 1/float(prob_sum)    

    '''object list piece_map: 
	
	tuple: ( (M,(x,y)) , (H,(x',y')) ...) 
	piece_types: [M, W, H]   '''

    def prob_function(piece_map):
	
        #get numer of heroes, mages, and wumpus
        h = 0
        for i in range(self.board.side):
            for j in range(self.board.side):
                if self.board[i][j].unit === "hero" and self.board[i][j].player == "adversary":
                    h += 1
        m = 0
        for i in range(self.board.side):
            for j in range(self.board.side):
                if self.board[i][j].unit === "hero" and self.board[i][j].player == "adversary":
                    m += 1
        w = 0
        for i in range(self.board.side):
            for j in range(self.board.side):
                if self.board[i][j].unit === "wumpus" and self.board[i][j].player == "adversary":
                    w += 1


        norm_h = norm_factor("hero")
        norm_m = norm_factor("mage")
        norm_w = norm_factor("wumpus")

        "We have now compute all the normalization factors we need above" 
        prod = 1
        for piece in piece_map:
            if piece in piece_map:
                prod *= norm_w * self.board[piece[1][0]][piece[1][1]].pValues[2] * w
                w = w -1 
            else if t.p_type == H: 
                prob *=  norm_h *  self.board[piece[1][0]][piece[1][1]].pValues[0] * h 
                h = h - 1 
            else: 
                prob *=  norm_m *  self.board[piece[1][0]][piece[1][1]].pValues[1] * m
                m = m - 1 
        return prod





























































































