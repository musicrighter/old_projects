"""
Boggle solver.  Assignment 6, CIS 210
Author: David Gustafson
  
Usage:  python3 boggler.py  "board" dict.txt
where "board" is 16 characters of board, in left-to-right reading order
and dict.txt can be any file containing a list of words in alphabetical order    
"""

from boggle_board import BoggleBoard   
import argparse   # Command line processing
import game_dict  # Dictionary of legal game words

def main():
    """
    Main program: 
    Find all words of length 3 or greater on a boggle 
    board. 
    Args:
        none (but expect two arguments on command line)
    Returns: 
        Nothing (but prints found words in alphabetical
        order, without duplicates, one word per line)
    """
    dict_file, board_text = getargs()
    game_dict.read( dict_file )
    board = BoggleBoard(board_text)
    results = [ ]
    
    for row in range(4):
        for col in range(4):
            find_words(board,row,col,'',results)
    
    single_results = duplicates(results)   # get non-duplicate list 
            
    total_score = 0
    total_num = 0
    for word in single_results:   # print found words with point values
        if score(word) == 11:
            print(word, score(word))
            total_score += score(word)
            total_num += 1
    
    for word in single_results:   # print found words with point values
        if score(word) == 5:
            print(word, score(word))
            total_score += score(word)
            total_num += 1

    for word in single_results:   # print found words with point values
        if score(word) == 3:
            print(word, score(word))
            total_score += score(word)
            total_num += 1

    for word in single_results:   # print found words with point values
        if score(word) == 2:
            print(word, score(word))
            total_score += score(word)
            total_num += 1

    for word in single_results:   # print found words with point values
        if score(word) == 1:
            print(word, score(word))
            total_score += score(word)
            total_num += 1

    print('Total score: ', total_score)
    print('Number of words: ', total_num)

def duplicates(results):
    """
    Remove duplicates from results list.
    Args:
       results: filled result list of found words
    Returns:
       single_results: result list without duplicates
    """
    single_results = []
    sorted_results = sorted(results)   # sort results
    prev = ''
    for word in sorted_results:   # remove duplicates
        if word != prev:
            single_results.append(word)
        prev = word
    return single_results
    
def getargs():
    """
    Get command line arguments.
    Args:
       none (but expects two arguments on program command line)
    Returns:
       pair (dictfile, text)
         where dictfile is a file containing dictionary words (the words boggler will look for)
         and   text is 16 characters of text that form a board
    Effects:
       also prints meaningful error messages when the command line does not have the right arguments
    """
    parser = argparse.ArgumentParser(description="Find boggle words")
    parser.add_argument('board', type=str, help="A 16 character string to represent 4 rows of 4 letters. Q represents QU.")
    parser.add_argument('dict', type=argparse.FileType('r'),
                        help="A text file containing dictionary words, one word per line.")
    args = parser.parse_args()  # will get arguments from command line and validate them
    text = args.board
    dictfile = args.dict
    if len(text) != 16 :
        print("Board text must be exactly 16 alphabetic characters")
        exit(1)
    return dictfile, text

def find_words(board, row, col, prefix, results):
    """Find all words starting with prefix that
    can be completed from row,col of board.
    Args:
        row:  row of position to continue from (need not be on board)
        col:  col of position to continue from (need not be on board)
        prefix: looking for words that start with this prefix
        results: list of words found so far
    Returns: nothing
        (side effect is filling results list)
    Effects:
        inserts found words (not necessarily unique) into results
    """
    if board.available(row, col):   # Continue if square is available
        char = board.get_char(row, col)
        prefix += char
        search_result = game_dict.search(prefix)
        if search_result != game_dict.NO_MATCH:   # Stop if prefix returns no_match
            board.mark_taken(row, col)
            if search_result == game_dict.WORD:   # Add word to dictioary
                results.append(prefix)
            find_words(board, row+1, col, prefix, results)
            find_words(board, row-1, col, prefix, results)
            find_words(board, row, col+1, prefix, results)
            find_words(board, row, col-1, prefix, results)
            find_words(board, row+1, col+1, prefix, results)
            find_words(board, row+1, col-1, prefix, results)
            find_words(board, row-1, col+1, prefix, results)
            find_words(board, row-1, col-1, prefix, results)
            board.unmark_taken(row, col)
    return
    
def score(word):
    """
    Finds the appropriate point value for the length of inputed word.
    Args:
        word: A word of length <= 16 made up of only letters
    Returns:
        integer, 0-11 that acts as a point value
    """
    if len(word) == 3 or len(word) == 4:
        return 1
    elif len(word) == 5:
        return 2
    elif len(word) == 6:
        return 3
    elif len(word) == 7:
        return 5
    elif len(word) >= 8:
        return 11
    return 0

####
# Run if invoked from command line
####

if __name__ == "__main__":
    main()
    input("Press enter to end")
