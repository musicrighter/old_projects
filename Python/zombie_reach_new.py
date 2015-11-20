#
# zombie_reach.py
#
# This program takes in a floor plan, starting coordinates, and target coordinates then
# computes if the target is reachable from the start.

import sys

# Constants to help with processing the floor plan
WALL='#'
OPEN='.'

def readMap(filename):
    """Returns a 2D list representing the floor plan in the file named filename"""
    map=list()
    mapfile=open(filename)
    for line in mapfile:
        line=line.strip()
        map.append(list(line))
    return map

def readLoc(map,x,y):
    """Returns the symbol to location x,y in the 2D list map"""
	# Since we shouldn't consider squares off of the map, treat them as walls
    if x<0 or x>len(map[0]):
        return WALL
    if y<0 or y>len(map):
        return WALL
		
    return map[y][x]

def setLoc(map,x,y,sym):
    """Sets the symbol at location x,y in the 2D list map to sym"""
	# deal with off-map squares too, like in the readLoc

    map[y][x]=sym

def printMap(map):
    """Prints the map to the terminal"""
    for y in range(len(map)):
        for x in range(len(map[0])):
            print(readLoc(map,x,y),end='')
        print('')
        
def zombieSearch(map,zombie_x,zombie_y,target_x,target_y):
    """Recursive function to search from zombie_x,zombie_y to target_x,target_y in map
    
       Returns True if the zombie can reach the target, false otherwise
    
       You'll need to implement this function"""
	   
	# Zombie reached the target
    if zombie_x==target_x and zombie_y==target_y:
        return True
        
    sym=readLoc(map,zombie_x,zombie_y)
    
	# Zombie reached a wall
    if sym==WALL:
        return False
        
    # Zombie reached somewhere he's already been
    if sym=='Z':
        return False
        
    # Mark that the zombie reached this location
    setLoc(map,zombie_x,zombie_y,'Z')
    
    # Zombie moves up
    if zombieSearch(map,zombie_x,zombie_y-1,target_x,target_y):
        return True
        
    # Zombie moves down
    if zombieSearch(map,zombie_x,zombie_y+1,target_x,target_y):
        return True

    # Zombie moves left
    if zombieSearch(map,zombie_x-1,zombie_y,target_x,target_y):
        return True

    # Zombie moves right
    if zombieSearch(map,zombie_x+1,zombie_y,target_x,target_y):
        return True

    # If the zombie can't reach the target from anywhere the zombie
    # can reach from here, then the zombie can't reach the target from here
    return False

def main():
    """Reads a map file and prints a message when there is a way to get from the start 
       coordinates to the target coordinates.
       
       You don't need to make any changes to the main function this week."""
       
    # check the args, abort if there aren't enough
    if len(sys.argv) != 6:
        print("Usage: python3 "+sys.argv[0]+" <filename.map> <zombie x> <zombie y> <target x> <target y>")
        exit(1)
    
    # covert from sys.argv list to easier names
    mapfile=sys.argv[1]
    zombiex=int(sys.argv[2])
    zombiey=int(sys.argv[3])
    targetx=int(sys.argv[4])
    targety=int(sys.argv[5])
    
    # Read the map file
    map=readMap(mapfile)
    
    # Use the recursive function to complete the search
    canReach=zombieSearch(map,zombiex,zombiey,targetx,targety)
    
    # Print the correct message to the user based on the search results
    if canReach:
        print("**************************************************")
        print("* !!! DANGER - Zombie risk detected - DANGER !!! *")
        print("**************************************************")
    else:
        print("Floor plan appears safe.")

if __name__=="__main__":
    main()
