"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random


class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
#    raise NotImplementedError
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    w, h = game.width, game.height
    y, x = game.get_player_location(player)
    return float((h - y)**2 + (w - x)**2)


def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
#    raise NotImplementedError
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    return float(own_moves - opp_moves)


def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
#    raise NotImplementedError
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    return float(len(game.get_legal_moves(player)))


class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
#            print("self.search_depth ",self.search_depth, game.get_legal_moves())
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
            

        # TODO: finish this function!
#        raise NotImplementedError
        # Get legal moves for active player
#        legal_moves = game.get_legal_moves()
##        print("legal_moves ",legal_moves)
#        # Game over terminal test
#        if not legal_moves:
            # -inf or +inf from point of view of maximizing player
#            return game.utility(self), (-1, -1)
#            return (-1, -1)
#        
#        # Search depth reached terminal test
#        if depth == 0:
            # Heuristic score from point of view of maximizing player
#            return self.score(game, self), (-1, -1)
#            return  (-1, -1)
        
        player = game.active_player
       
      
        Active_Player_Next_Moves = game.get_legal_moves(player)
#        Active_Player_Next_Moves = game.get_legal_moves()
#        print("\n  successors ", Active_Player_Next_Moves, "\n active Player ",game.active_player.__dict__ )
#        print("\n  successors ", Active_Player_Next_Moves, "\n active Player ",game.active_player.__dict__.values() )
        best_move =  (-1, -1)
        max_value = float("-inf")
        min_value = float("inf")
        Active_Player_Next_Moves = game.get_legal_moves(player)
        
        for Active_Player_Next_Move in Active_Player_Next_Moves:
            new_game = game.forecast_move(Active_Player_Next_Move)
            assert(new_game.to_string() != game.to_string())
            if not game.move_is_legal(Active_Player_Next_Move):
                    Active_Player_Next_Move=(-1,-1)
#            new_game_score= self.score(new_game,new_game.active_player)
#            print("depth", depth)
            new_game_score= self.find_min_value(new_game,depth-1)
#            if not game.move_is_legal(Active_Player_Next_Move):
#            print(game.move_is_legal(Active_Player_Next_Move))
                
#            print("New Board Score =",new_game_score, Active_Player_Next_Move)
#            print(new_game.to_string())
#            print(" Utility ",new_game.utility(new_game.active_player))
            if new_game_score > max_value :
#                print("new_game_score ",new_game_score)
                max_value = new_game_score
                best_move = Active_Player_Next_Move
#            print("depth", depth, best_move)
        return best_move     
    
    def find_max_value(self, game, depth):
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
            player = game.active_player
            max_value = float("-inf")
#            print("depth find_max_value", depth)
#            print(self.score(game,self),self.score(game,player), "find_max_value ", depth, game.is_winner(player))
            if  game.is_winner(player) or  game.is_loser(player) or depth == 0 :
#                print(self.score(game,self),self.score(game,player), "find_min_value ", depth, game.is_winner(player))
                return self.score(game,self)
           
            Active_Player_Next_Moves = game.get_legal_moves(player)
#            Active_Player_Next_Moves = game.get_legal_moves()
            if not Active_Player_Next_Moves:
               return game.utility(self), (-1, -1)
           
            for Active_Player_Next_Move in Active_Player_Next_Moves:
#                print(game.move_is_legal(Active_Player_Next_Move))
                if not game.move_is_legal(Active_Player_Next_Move):
                    Active_Player_Next_Move=(-1,-1)
                    
                max_new_game = game.forecast_move(Active_Player_Next_Move)
                assert(max_new_game.to_string() != game.to_string())
#                print("Hello")
                max_new_game_score= self.find_min_value(max_new_game,depth-1)
#                print("max_new_game_score ",max_new_game_score,max_value)
                if max_new_game_score > max_value:
#                    print("max_new_game_score ",max_new_game_score)
                    max_value = max_new_game_score
#            if max_value != "-inf"  or max_value != "inf":
#                print ("best Max Score= ",max_value)   
            return     max_value
               
                
    def find_min_value(self, game, depth):
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
            player = game.active_player
            min_value = float("inf")
#            print("depth find_mmin_value", depth)
#            print("find_min_value ", depth, game.is_loser(player))
            if game.is_winner(player) or  game.is_loser(player) or depth == 0:
#                print(self.score(game,self),self.score(game,player), "find_min_value ", depth, game.is_loser(player))
                return self.score(game,self)
           
            Active_Player_Next_Moves = game.get_legal_moves(player)
#            Active_Player_Next_Moves = game.get_legal_moves()
            if not Active_Player_Next_Moves:
               return game.utility(self), (-1, -1)
           
            for Active_Player_Next_Move in Active_Player_Next_Moves:
#                print(game.move_is_legal(Active_Player_Next_Move))
                if not game.move_is_legal(Active_Player_Next_Move):
                    Active_Player_Next_Move=(-1,-1)
                min_new_game = game.forecast_move(Active_Player_Next_Move)
                assert(min_new_game.to_string() != game.to_string())
                min_new_game_score= self.find_max_value(min_new_game,depth-1)
               
                if min_new_game_score < min_value:
                    min_value = min_new_game_score
#            print("depth find_mmin_value", depth,self.score(game,self),min_value)
#            if min_value != "-inf" or min_value != "inf":
#                print ("best Min Score= ",min_value)   
            return     min_value               



class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # TODO: finish this function!
        if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
#        best_move = (4,4)
#        return best_move
        import itertools
#        import sys
        best_move = (-1, -1)
        depth = 0
#        print("Game Count",game.move_count) 
#        print("self.iterative" ,self.iterative)
        lm = game.get_legal_moves(game.active_player)
        if not lm:
            return (-1,-1)

        
        try:
#         while True:
            for depth in itertools.count():
#            for depth in range(sys.maxsize):
                depth += 1
#             while True:
#            # The try/except block will automatically catch the exception
#            # raised when the timer is about to expire.
#            print("self.search_depth ",self.search_depth, game.get_legal_moves())
                best_move = self.alphabeta(game,depth, alpha=float("-inf"), beta=float("inf"))
#                print(game.move_count,"best_move =", best_move ,"depth =",depth)
#                if best_score == float("inf") or best_score == float("-inf"):
#                    return best_move
#                    break
                if best_move == (-1, -1) :
                    break
                
            return best_move
                
#
        except SearchTimeout:
                pass  # Handle any actions required after timeout as needed
#                return (-1,-1)

        # Return the best move from the last completed search iteration
        return best_move

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # TODO: finish this function!
#        best_move = (4, 4)
#        return best_move
#        pass


        player = game.active_player
       
      
        
#        Active_Player_Next_Moves = game.get_legal_moves()
#        print("\n  successors ", Active_Player_Next_Moves, "\n active Player ",game.active_player.__dict__ )
#        print("\n  successors ", Active_Player_Next_Moves, "\n active Player ",game.active_player.__dict__.values() )
        best_move =  (-1, -1)
        max_value = float("-inf")
        min_value = float("inf")
        Active_Player_Next_Moves = game.get_legal_moves(player)
        for Active_Player_Next_Move in Active_Player_Next_Moves:
            new_game = game.forecast_move(Active_Player_Next_Move)
            assert(new_game.to_string() != game.to_string())
            if not game.move_is_legal(Active_Player_Next_Move):
                    Active_Player_Next_Move=(-1,-1)

            new_game_score= self.find_min_value(new_game,alpha, beta,depth-1)
#            if not game.move_is_legal(Active_Player_Next_Move):
#            print(game.move_is_legal(Active_Player_Next_Move))
                
#            print("New Board Score =",new_game_score, Active_Player_Next_Move)
#            print(new_game.to_string())
#            print(" Utility ",new_game.utility(new_game.active_player))
            
            if new_game_score > max_value :
#                print("new_game_score ",new_game_score)
                max_value = new_game_score
                best_move = Active_Player_Next_Move
                
            if new_game_score > beta:
                return new_game_score
            
            alpha = max(alpha,new_game_score)
#            print("depth", depth, "best move ",best_move,"max_value ", max_value)
#            if max_value == float("inf") or max_value == float("-inf"):
#                        return best_move
#                        break
        return best_move     
    
    def find_max_value(self, game,  alpha, beta, depth):
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
            player = game.active_player
            max_value = float("-inf")
            
            if  game.is_winner(player) or  game.is_loser(player) or depth == 0 :
                return self.score(game,self)
           
            Active_Player_Next_Moves = game.get_legal_moves(player)

            if not Active_Player_Next_Moves:
               return game.utility(self), (-1, -1)
           
            for Active_Player_Next_Move in Active_Player_Next_Moves:
#                print(game.move_is_legal(Active_Player_Next_Move))
                if not game.move_is_legal(Active_Player_Next_Move):
                    Active_Player_Next_Move=(-1,-1)
                    
                max_new_game = game.forecast_move(Active_Player_Next_Move)
                assert(max_new_game.to_string() != game.to_string())
#                print("Hello")
                max_new_game_score= self.find_min_value(max_new_game,alpha, beta,depth-1)
#                print("max_new_game_score ",max_new_game_score,max_value)
                if max_new_game_score > max_value:
#                    print("max_new_game_score ",max_new_game_score)
                    max_value = max_new_game_score
                    
                if  max_value >= beta:
                    return max_value
                
#                alpha = max(alpha,max_value)
                if  max_value > alpha:
                    alpha = max_value
                    
#            if max_value != "-inf"  or max_value != "inf":
#                print ("best Max Score= ",max_value)   
            return     max_value
               
                
    def find_min_value(self, game,  alpha, beta, depth):
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
            player = game.active_player
            min_value = float("inf")

            if game.is_winner(player) or  game.is_loser(player) or depth == 0:
                return self.score(game,self)
           
            Active_Player_Next_Moves = game.get_legal_moves(player)
            if not Active_Player_Next_Moves:
               return game.utility(self), (-1, -1)
           
            for Active_Player_Next_Move in Active_Player_Next_Moves:
                if not game.move_is_legal(Active_Player_Next_Move):
                    Active_Player_Next_Move=(-1,-1)
                    
                min_new_game = game.forecast_move(Active_Player_Next_Move)
                assert(min_new_game.to_string() != game.to_string())
                min_new_game_score= self.find_max_value(min_new_game,alpha, beta,depth-1)
               
                if min_new_game_score < min_value:
                    min_value = min_new_game_score
                    
                if  min_value <= alpha:
                    return min_value
                
                if  min_value < beta:
                    beta = min_value
                
#            print("depth find_mmin_value", depth,self.score(game,self),min_value)
#            if min_value != "-inf" or min_value != "inf":
#                print ("best Min Score= ",min_value)   
            return     min_value               
