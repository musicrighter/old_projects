import sys

class Tile(object):
    def __init__(self,data):
        self.data = data


class Board(object):
    """Board, contains 2 lists holdint the rows and columns of the board populated with Tile objects"""
    def __init__(self,tile_data):
        self.tile_data = tile_data ## a list of 9 ints
        self.rows = []  ##2D list 
        self.cols = [] ## 2D list 

    def make_rows(self):
        """
        Creates self.rows from tile_data
        """
        j = 0 ##initialize j
        for i in range(3,10,3): ## count from 3 to 10 by 3's
            row = []
            while j < i:
                data = self.tile_data[j]
                new_tile = Tile(data)
                row.append(new_tile)
                j+=1

            self.rows.append(row) ##append the row to the collection of rows


    def make_cols(self):
        """
        Creates the columns from the rows.
        """
        for i in range(3): 
            column = []
            for j in range(3):
                new_tile = self.rows[j][i]  ## keep the col value the same iterate thru rows for each col. ex: 00 10 20
                ## the value at rows[j[]i] is just a Tile object so we just need to add the tile object to column
                column.append(new_tile) ## the instance of Tile at rows[i][j] is now in column as well

            self.cols.append(column) ##append column to the collection of columns


    def create_board(self):
        """makes the rows and columns of the board in one call"""
        self.make_rows()
        self.make_cols()


    def isCorrect(self,collection):
        for group in range(len(collection)):
            num = []
            for tile in range(3):
                if Tile(tile) not in num:
                    num.append(Tile(tile))
                elif Tile(tile) in num:
                    return False
        return True
        
    def print_collection(self,collection):
        for group in collection:
            lst = []
            for e in group:
                lst.append(e)
            print(lst)

    
    def check_board(self):
        """Uses isCorrect to see check if valid Board"""
        
        if self.isCorrect(self.cols) and self.isCorrect(self.rows):
            return "This is a valid board."
        
        else:
            return "This is not a valid board."



def main():
    stdin = sys.stdin.readline().strip()
    input_tiles = [int(char) for char in stdin]
    b = Board(input_tiles)
    b.create_board()
    result = b.check_board()
    print(result)
    
if __name__ == '__main__':
    main()