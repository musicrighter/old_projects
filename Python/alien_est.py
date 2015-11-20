# Program to help O-SNAP estimate cities lost and number of casualties from alien attack

# Libraries we need to read arguments and get trig functions
import math
import sys

# Radius of the earth, needed for distance computation
EARTH_RAD = 6371 # km

# Capture the user input
# You'll need to write this... recall that the program will be invoked as
# python alien_est.py <file> <latitude> <longitude> <radius>
# where 
# <file> is the name of the city data file
# <latitude> is a target latitude in degrees
# <longitude> is a target longitude in degrees
# <radius> is the affected distance from the target in km

# get the name of the file from the command line argument:
filename = sys.argv[1]

# get (and name) the other command line arguments:
lat_from_CL = float(sys.argv[2])
long_from_CL = float(sys.argv[3])
radius_from_CL = float(sys.argv[4])

# open the file whose name we just got:
get_file = open(filename)

# Setup a counter for summing the population effected
est_casualties=0

# Function to handle the conversion from degrees to radians
# You'll need to write the function body
def deg_to_rad(deg):
    # Conversion formula: divide degrees by 180, then multiply by pi
    # pi is provided by the math library; math.pi
    radians = deg * math.pi / 180
    print(str(radians))
    return radians

# Function to compute distances
# You may need to add code to this function
def distance(lat_a,lng_a,lat_b,lng_b):
    # Spherical law of cosines -- retrieved from
    # http://www.movable-type.co.uk/scripts/latlong.html
    # dist = acos(sin(lat1)*sin(lat2)+cos(lat1)*cos(lat2)*cos(long2-long1)*R
    # The formula requires that the latitude and longitude be given in
    # radians
    dist = math.acos(math.sin(lat_a) * math.sin(lat_b) + math.cos(lat_a) * math.cos(lat_b) * math.cos(lng_b-lng_a)) * EARTH_RAD
    return dist


# You'll need to write the main part of the program that
# 1. Opens the file
# 2. for each line in the file
#   a. splits the line into a list of values based on the '|' character
#   b. compute the distance between the target and city
#   c. print the city and state if the distance is less than the radius
#   d. add the population of the city to the counter
# 3. print the value of the counter
