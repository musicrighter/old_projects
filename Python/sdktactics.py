"""
Tactics and checks for Sudoku.

Authors: David Gustafson
Consulted with Xingtian Meng

sdktactics.py winter 2014

A tactic is a rule that can be used to determine and/or constrain the
possible choices for a Sudoku tile.

A check determines whether a given Sudoku board
(whether complete or incomplete) is legal.  A board is
legal if it contains only digits and open spaces, and
if all of the digits are unique in each row, column,
and 3x3 block.
"""
import sdkboard

# The following variables are private but global to the module
global groups
global progress

def prepare(board):
    """ 
    Prepare for checking and solving a sudoku board.
    Args:
       board:  An sdkboard.Board object
    Returns:
       nothing
    Effects:
       prepared for check(board) and solve(board)
    """
    global groups  # rows, columns, and blocks

    groups = [ ]

    # Rows  (we can reuse them from the board)
    for row in range(9):
        groups.append(board.tiles[row])

    # Columns (we need new lists for these)
    for col in range(9):
        columns = []
        for row in range(9):
            columns.append(board.tiles[row][col])   # make up a full column
        groups.append(columns)   # Add each full column to groups

    # Blocks  (we need new lists for these, too)
    for start_row in [0, 3, 6]:
        for start_col in [0, 3, 6]:
            sq_tiles = [ ] 
            for row in range(3):
                for col in range(3): 
                    t = board.tiles[start_row + row][start_col+col]
                    sq_tiles.append(t)
            groups.append(sq_tiles)

    # We need to know when we are making progress 
    for row in board.tiles:
        for tile in row:
            tile.register(progress_listener)
 
def progress_listener(tile, event):
    """
    An event listener, used to determine whether we have made
    some progress in solving a Sudoku puzzle.  This listener
    will be attached to Sudoku Tile objects, and informed when
    "determined" and "constrained" events occur.
    Args:
       tile:  The tile on which an event occurred
       event: What happened.  The events we listen for are "determined"
         and "constrained"
    Returns:  nothing
    Effects: module-global variable progress may be set to True
    """
    global progress 
    if event == "determined" or event == "constrained":
       progress = True

def good_board(): 
    """Check that every group (row, column, and block)
    contains unique elements (no duplicate digits).
    Args:
       none  (implicit through prepare_board)
    Returns:
       Boolean True iff all groups contain unique elements
    Effects:
       Will announce "duplicate" event on tiles that are
       not unique in a group.
    Requires:
       prepare(board) must be called before good_board
    """
    ok = True
    for group in groups:   # cycle through every group
        used = set()
        duplicates = set()
        for tile in group:    # cycle through every tile
            if tile.symbol not in used:
                used.add(tile.symbol)    # build up already used list
            elif tile.symbol != '.':
                duplicates.add(tile.symbol)    # build up duplicates list
                ok = False
        for tile in group:   # announce that tile is duplicate
            if tile.symbol in duplicates:
                sdkboard.Tile.announce(tile, 'duplicate')
    return ok

def solve():
    """
    Keep applying naked_single and hidden_single tactics to every
    group (row, column, and block) as long as there is progress.
    Args: 
        none
    Requires:
        prepare(board) must be called once before solve()
        use only if good_board() returns True
    Effects: 
        May modify tiles in the board passed to prepare(board), 
        setting symbols in open tiles, and reducing the possible
        sets in some tiles. 
    """
    global progress
    progress = True
    while(progress):
        progress = False
        for group in groups:
            naked_single(group)
            hidden_single(group)

def naked_single(group):
        """Constrain each tile to not contain any of the digits 
        that have already been used in the group.
        Args: 
            group: a list of 9 tiles in a row, column, or block
        Returns:
            nothing
        Effects:
            For each tile in the group, eliminates "possible" elements
            that match a digit used by another tile in the group.  If 
            this reduces it to one possibility, the selection will be 
            made (Tile.remove_choices does this), and progress may be 
            signaled.
        """
        for tile in group:
            if tile.symbol == '.':   # only look at unfinished tiles 
                for other in group:
                    if len(tile.possible) > 1 and other.symbol != '.':
                        tile.remove_choices(other.possible)   # remove if not possible
        return
        
def hidden_single(group):
        """Each digit has to go somewhere.  For each digit, 
        see if there is only one place that digit should 
        go.  If there is, put it there. 
        Args: 
           group:  a list of 9 tiles in a row, column, or block
        Returns: 
           nothing
        Effects: 
           For each tile, if it is the only tile that can accept a 
           particular digit (according to its "possible" set), 
           
        """
        digits = frozenset('123456789') 
        for tile in group:
            if tile.symbol in digits:   
                digits -= set(tile.symbol)   # remove duplicated digits
        for number in digits:
            others = 0
            for tile in group:
                if number in tile.possible:   # if there are other options
                    others += 1
                    prev = tile
            if others == 1:   # when there is no other option
                prev.determine(number)
        return
