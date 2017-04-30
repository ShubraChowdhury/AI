"""
Defining size of sudoku this is a 9 by 9 sudoku 
"""
cols = '123456789'
rows = 'ABCDEFGHI'
assignments = []

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """

    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

        
def naked_twins(values):
    """
    1. Find the twin value set "found_twins"
    2. Next find the box and peer combination and store in box_peer_combination 
    3. If any box peer combination is zero then directly return the value , if length of any box is zero then return the value
    4. Find the First and second digit in the box
    5. Update the cells for square_units followed by row_units and then column units
    6. Finally return the updated values
    
    """
    
    """
    Find the cells with twin values
    """
    found_twins = [box for box in values.keys() if len(values[box]) == 2]
    box_peer_combination = []
    
    """
    Get the combination of box and peer
    """

    for box in found_twins:
        digit = values[box]
        for peer in peers[box]:
            if digit==values[peer] and peer != box:
                box_peer_combination.append((box,peer))
    
    
    
    if len(box_peer_combination) == 0:
        return values

    for box1,peer1 in box_peer_combination:
        if len(values[box1]) != 2:
            return values
            
        first_digit = values[box1][0]
        second_digit = values[box1][1]
        """
        For the combination of box and peer replace the first and second digits 
        First start with square units followed by rows and columns
        """
        for square in square_units:
            if box1 in square and peer1 in square:
                for cell in square:
                    if (first_digit in values[cell] or second_digit in values[cell] ) and box1 != cell and peer1 != cell:
                            values[cell] = values[cell].replace(first_digit,'')
                            values[cell] = values[cell].replace(second_digit,'')
        if box1[0]==peer1[0]:
            for row in row_units:
                if box1 in row:
                    for cell in row:
                        if (first_digit in values[cell] or second_digit in values[cell] ) and box1 != cell and peer1 != cell:
                            values[cell] = values[cell].replace(first_digit,'')
                            values[cell] = values[cell].replace(second_digit,'')
        if box1[1]==peer1[1]:
            for column in column_units:
                if box1 in column:
                    for cell in column:
                        if (first_digit in values[cell] or second_digit in values[cell] ) and box1 != cell and peer1 != cell:
                            values[cell] = values[cell].replace(first_digit,'')
                            values[cell] = values[cell].replace(second_digit,'')
 
    return values


def cross(A, B):
    "Cross product of elements in A and elements in B."
    """
    Function with input of row and column and it returns the cell number means the 
    intersection of row and column
    """
    return [s+t for s in A for t in B]

"""
   Get the box names , rows, square units , diagonals , units and peers.
"""
boxes = cross(rows, cols)
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
diagonal1 = [[a[0]+a[1] for a in zip(rows,cols)]]
diagonal2 = [[a[0]+a[1] for a in zip(rows,cols[::-1])]]
"""
Now diaognals are also part of list so total units for this program will be 
combination of rows , columns , square units and both diagonals
"""
unitlist = row_units + column_units + square_units+diagonal1+diagonal2
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)



def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """

    
    values = []
    all_digits = '123456789'
    for c in grid:
        if c == '.':
            values.append(all_digits)
        elif c in all_digits:
            values.append(c)
        
    assert len(values) == 81
    return dict(zip(boxes, values))

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """

    """
    This draws a grid to display the sudoku where vertical lines are drawn using "|"
    and horizontal line are drawn using "-", intersection between horizontal and
    vertical lines are connected by a "+" sign
    
    
    """

    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
        


def eliminate(values):
    """
        1. First  get the cells with values as single digits
        2. Look for the peers and replace the single digit found in step 1 
        by '' and then return the values.

    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit,'')
            
    return values


def only_choice(values):
    """
        1. get the units and then check for the values from 1 to 9 in each 
        cell and assign the digit as the first digit

    """
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
#                values[dplaces[0]] = digit # Below line added as per instructions
                assign_value(values,dplaces[0],digit)
    return values

def reduce_puzzle(values):
    """
        Calls are made to naked_twin, only choice and eliminate methods and
        it continues till the flag is True (means the solved before and 
         after are equal)

    """
    stalled = False
    while not stalled:
        """ 
        Check how many boxes have a determined value
        """
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        
        values = naked_twins(values)
        values = only_choice(values)
        values = eliminate(values)
        display(values)
        
        """#
        Check how many boxes have a determined value, to compare
        """
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        """
        If no new values were added, stop the loop.
        """
        stalled = solved_values_before == solved_values_after
        """
        # Sanity check, return False if there is a box with zero available values:
        """
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values
      
def search(values):
    """
     Using depth-first search and propagation, create a search tree and solve the sudoku.
     First, reduce the puzzle using the previous function
     Then it checks if values in all cells , if all cell has single digit number then 
     it returns the value . If the values are greater than 1 (means more than 1 digit 
      number ) then uses recurrence to solve each one of the resulting sudoku

    """
    values = reduce_puzzle(values)
    """
    Check earlier failed status
    """
    if values is False:
        return False 
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!
    """
    Choose one of the unfilled squares with the fewest possibilities
    """
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    """  
    Now use recurrence to solve each one of the resulting sudokus
    
    """
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    
    First get grid value then call reduce which will call naked, eliminate and choice then finally call search    
        
    """
    values = grid_values(grid)
    values = reduce_puzzle(values) 
    values = search(values)
    display(values)
    return values 

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))
    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
    