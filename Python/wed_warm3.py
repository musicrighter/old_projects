import sys
class Zombie:
    """
    Instantiated with a name and moan

    Variables:
    moan = string of zombie moan
    name = string of the zombie's name

    Methods:
    __init__
    identify
    get_name
    """

    def __init__(self,input_name,input_moan):
        self.name = input_name
        self.moan = input_moan

    def identify(self):
        """
        prints exactly of the form:

        moan My name moan is name 
        """
        print(self.moan + " My name "+ self.moan + " is "+ self.name)       

    def get_name(self):
        """ Returns the name of the zombie"""
        return self.name

class Human:
    """
    Initalized with a name and and an instance of Zombie that it is 
    being chased by.

    Variables:
    name    = string 
    chased_by = instance of Zombie

    Methods:
    __init__
    identify

    """

    def __init__(self,input_name, zombie):
        self.name = input_name
        self.chased_by = zombie

    def identify(self):
        """
        prints exactly of the form

        My name is name I'm being chased by zombie name

        """
        print("My name is " + self.name+ " I'm being chased by " + self.chased_by)

def main():
    args = sys.stdin.readline().rstrip()
    args = args.split()
    zombie_name = args[0]
    zombie_moan = args[1]
    human_name = args[2]
    

    # print(zombie_moan + " My name "+ zombie_moan + " is "+ zombie_name) 
    # print("My name is "+human_name+ " I'm being chased by "+ zombie_name)

    ##create an instance of zombie
    z = Zombie(zombie_name, zombie_moan)
    ##create an instance of human
    h = Human(human_name, zombie_name)
    ##make the zombie identify
    Zombie.identify(z)
    ##make the human identify
    Human.identify(h)
    
if __name__ == '__main__':
    main()
