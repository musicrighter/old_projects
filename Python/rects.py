import graphics  # Because what fun are rectangles without drawing

#
# Very simple graphical depiction.  Virtual coordinates to 50,50
#

global WIN, CUR_COLOR  # Sloppy but expedient.  How should we handle these? 

WIN = graphics.GraphWin("Rectangles", 800, 800)
WIN.setCoords(0,0,50,50)
background = graphics.Rectangle( graphics.Point(0,0), graphics.Point(1024,768))
background.setFill( graphics.color_rgb(255,255,255) ) # white

CUR_COLOR = graphics.color_rgb(0,0,0) # black

def draw_rect(llx, lly, urx, ury, color=""):
    """Display a rectangle in the graphics window.
    Arguments:
       llx, lly:  Coordinates of lower left corner
       urx, ury:  Coordinates of upper right corner
       color: fill color of rectangle drawn on screen
    Returns:
       nothing
    Effects:
       rectangle is drawn on screen
    """
    view = graphics.Rectangle( graphics.Point(llx,lly), graphics.Point(urx,ury))
    view.setFill( CUR_COLOR )
    view.draw(WIN)
    return

##### End of kludgy graphics


class Rect(object):
    """A rectangle, defined by a lower-left corner
    and an upper-right corner.  All coordinates are 
    integers in range 0..50.  Immutable, and with a
    graphical depiction. 
    """
    
    def __init__(self, llx, lly, urx, ury):
        """Create Rect with lower left corner (llx,lly) and upper
           right corner (urx,ury).
           Arguments:
              llx, lly:  Integer lower left corner in range 0..50
              urx, ury:  Integer upper right corner in range 0..50,
                  such that urx > llx, ury > lly
           Effects:
              In additon to initializing the Rect object, draw a
              corresponding rectangle on the screen.
        """
        if llx >= urx :
            raise ValueError("Width must be positive (urx > llx)")
        if lly >= ury : 
            raise ValueError("Height must be positive (ury > lly)")
        self.llx = llx
        self.lly = lly
        self.urx = urx
        self.ury = ury
        draw_rect(llx, lly, urx, ury, color=CUR_COLOR)

    def overlap(self, other):
        '''Checks if rectangles overlap. Returns T or F'''
        if self.leftof(other):
            return False
        if other.leftof(self):
            return False
        if self.below(other):
            return False
        if other.below(self):
            return False
        return True

    def intersection(self, other):
        lly = max(self.lly, other.lly)
        llx = max(self.llx, other.llx)
        ury = min(self.ury, other.ury)
        urx = min(self.urx, other.urx)
        return Rect(lly, llx, ury, urx)
        
    def leftof(self, other):
        '''Checks if a rectangle is to the left of self, returns T or F'''
        return self.urx <= other.llx

    def below(self, other):
        '''Checks if a regtangle is below another'''
        return self.ury <= other.lly
        
    def __str__(self):
        return ("Rect(" + str(self.llx) + "," + str(self.lly) + "," + 
                str(self.urx) + "," + str(self.ury) + ")" )
                
class RectList:
    '''Basically a list of Rect, but with an intersection
       operation added'''
    def __init__(self):
        self.rects = []

    def addrect(self, rect):
        self.rects.append(rect)

    def intersect(self, other):
        result = Rectlist()
        for rectangles in self.rects:
            for other_rects in other.rects:
                if (rectangle.overlap(other_rect)):
                    result.addrect(rectangle.intersection(other_rect))



def main():
    global WIN            # Window for graphics
    global CUR_COLOR      # Current color. (Is there a better way to do this?)
    CUR_COLOR = graphics.color_rgb(0, 128, 0) # dull green? 
    
    sample = Rect(5, 5, 20, 20)
    other_rect = Rect(10, 10, 20, 25)
    non_overlap_rect = Rect(25, 25, 30, 30)

    first_rectlist = Rectlist()
    first_rectlist.addrect(sample)
    first_rectlist.addrect(other_rect)
    first_rectlist.addrect(non_overlap_rect)

    second_rectlist = Rectlist()
    second_rectlist.addrect(Rect(27, 27, 30, 30))
    second_rectlist.addrect(Rect(0, 6, 19, 10))
    
    if sample.overlap(other_rect):
        print('Overlap (expected)')
    else:
        print('No overlap (somethings wrong)')
        
    if sample.overlap(non_overlap_rect):
        print('Overlap (expected)')
    else:
        print('No overlap (somethings wrong)')

    CUR_COLOR = graphics.color_rgb(128, 0, 0)

    sample.intersection(other_rect)

    input("Press enter to close")

if __name__ == "__main__":
    main()
    
