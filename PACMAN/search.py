# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first
  [2nd Edition: p 75, 3rd Edition: p 87]
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm 
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  
  fringe = util.Stack()
#  print("fringe ",fringe)
  fringe.push( (problem.getStartState(), [], []) )
  while not fringe.isEmpty():
        print("fringe.isEmpty() =",fringe.isEmpty())
        node, actions, visited = fringe.pop()
        print("node, actions, visited  ",node, actions, visited )
        #('node, actions, visited  ', (8, 1), ['West'], [(9, 1)])
        print "Current successors:", problem.getSuccessors(node)
#        Current successors: [((9, 1), 'East', 1), ((7, 1), 'West', 1)]
        for coord, direction, steps in problem.getSuccessors(node):
            print(" coord, direction, steps ",coord, direction, steps)
            
#            (' coord, direction, steps ', (9, 1), 'East', 1)
#            (' coord, direction, steps ', (7, 1), 'West', 1)
            if not coord in visited:
                if problem.isGoalState(coord):
                    return actions + [direction]
                fringe.push((coord, actions + [direction], visited + [node] ))
            if  coord in visited:
                continue

  return []
#  return genericSearch(problem, util.Stack())
#  fringe = util.Stack();
#  expanded = set();
#  fringe.push((problem.getStartState(),[],0));
#
#  while not fringe.isEmpty():
#        curState, curMoves, curCost = fringe.pop();
#
#        if(curState in expanded):
#            continue;
#
#        expanded.add(curState);
#
#        if problem.isGoalState(curState):
#            return curMoves;
#
#        for state, direction, cost in problem.getSuccessors(curState):
#            fringe.push((state, curMoves+[direction], curCost));
#  return [];

#  util.raiseNotDefined()

def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """
  "*** YOUR CODE HERE ***"
#  util.raiseNotDefined()
  fringe = util.Queue()
  print("breadthFirstSearch")
  fringe.push( (problem.getStartState(), []) )
    
  visited = []
  while not fringe.isEmpty():
        node, actions = fringe.pop()
        print("node, actions  ",node, actions )
    
        for coord, direction, steps in problem.getSuccessors(node):
            if not coord in visited:
                if problem.isGoalState(coord):
                    return actions + [direction]
                fringe.push((coord, actions + [direction]))
                visited.append(coord)
    
  return []
      
def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
#    util.raiseNotDefined()
    fringe = util.PriorityQueue()
    print("uniformCostSearch")
    fringe.push( (problem.getStartState(), []), 0)
    explored = []
    
    while not fringe.isEmpty():
        node, actions = fringe.pop()
    
        if problem.isGoalState(node):
            return actions
    
        explored.append(node)
    
        for coord, direction, steps in problem.getSuccessors(node):
            if not coord in explored:
                new_actions = actions + [direction]
                fringe.push((coord, new_actions), problem.getCostOfActions(new_actions))
    
    return []

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
#    util.raiseNotDefined()
    print("aStarSearch")
    closedset = []
    fringe = util.PriorityQueue()
    start = problem.getStartState()
    fringe.push( (start, []), heuristic(start, problem))

    while not fringe.isEmpty():
        node, actions = fringe.pop()

        if problem.isGoalState(node):
            return actions

        closedset.append(node)

        for coord, direction, cost in problem.getSuccessors(node):
            if not coord in closedset:
                new_actions = actions + [direction]
                score = problem.getCostOfActions(new_actions) + heuristic(coord, problem)
                fringe.push( (coord, new_actions), score)

    return []    


def genericSearch(problem, fringe, heuristic=None):
    """
    Generic search algorithm that takes a problem and a queuing strategy
    and performs a search given that strategy
    Written Answers for Question 1
    1. The exploration order is what I would have expected. The search goes as
       deep as it can, before exploring other paths (as would be expected with 
       depth first search).
    2. No, Pacman does not go to all of the explored squares on the way to the 
       goal. He follows a path that does not lead him to any dead-ends, even if
       dead ends were explored. In my implementation, the length for a 
       MediumMaze was 130.
    3. This is not the least-cost solution -- there is clearly a cheaper 
       solution that Pacman does not take on the MediumMaze. This is because
       DFS will return the first solution that it finds that solves the problem,
       not the best solution.
    Written Answers for Question 4
    1. With OpenMaze, BFS, UCS, and A* all find the shortest path to the goal, 
       with BFS and UCS expanding the same number of search nodes (682) and A*
       expanding the least amount of nodes (535). All paths have a cost of 54.
       DFS does find the solution as well, but is not the shortest -- the cost
       of the path found with DFS was 298. This is because DFS does not look 
       for the shortest path.
    """

    visited = []        # List of already visisted nodes
    action_list = []    # List of actions taken to get to the current node
    initial = problem.getStartState()   # Starting state of the problem

    # Push a tuple of the start state and blank action list onto the given
    # fringe data structure. If a priority queue is in use, then calculate
    # the priority using the heuristic
    if isinstance(fringe, util.Stack) or isinstance(fringe, util.Queue):
        fringe.push((initial, action_list))
    elif isinstance(fringe, util.PriorityQueue):
        fringe.push((initial, action_list), heuristic(initial, problem))

    # While there are still elements on the fringe, expand the value of each 
    # node for the node to explore, actions to get there, and the cost. If the
    # node isn't visited already, check to see if node is the goal. If no, then
    # add all of the node's successors onto the fringe (with relevant 
    # information about path and cost associated with that node)
    while fringe: 
        if isinstance(fringe, util.Stack) or isinstance(fringe, util.Queue):
            node, actions = fringe.pop() 
        elif isinstance(fringe, util.PriorityQueue):
            node, actions = fringe.pop()
        
        if not node in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return actions
            successors = problem.getSuccessors(node)
            for successor in successors:
                coordinate, direction, cost = successor
                newActions = actions + [direction]
                if isinstance(fringe, util.Stack) or isinstance(fringe, util.Queue):
                    fringe.push((coordinate, newActions))
                elif isinstance(fringe, util.PriorityQueue):
                    newCost = problem.getCostOfActions(newActions) + \
                               heuristic(coordinate, problem)
                    fringe.push((coordinate, newActions), newCost)                  

    return []
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
