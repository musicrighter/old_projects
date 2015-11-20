# By David Gustafson
# Lab 2-4.py

def celsius_to_fahrenheit(celsius):
    '''Converts degrees in Celsius to degrees in Fahrenheit
       The only input argument is "celsius"
       The only output is "farenheit"
       To test the accuaracy of this program, I included examples:
       100 degrees C -> 212 degress F
       34 degrees C -> 93.2 degrees F, and
       -40.0 degrees C -> -40.0 degrees F
    '''
    fahrenheit = (9*celsius/5)+32
    return fahrenheit

print(celsius_to_fahrenheit(100))
f = celsius_to_fahrenheit(34)
print(f)
print(celsius_to_fahrenheit(-40.0))


