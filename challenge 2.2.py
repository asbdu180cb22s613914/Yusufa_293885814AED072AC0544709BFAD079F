'''Implement a class called player that represents a cricket player.The player class should have a
method called play() which prints"The player is playing cricket".Derive two classes, Batsman and
Bowler,from the player class.Override the play() method in each derived class to print"the batsman
is batting" and "the bowler is bowling", respectively.write a program to create object of both the
Batsman and Bowler classes and call the play()mathod for each object.'''


# Define the base class player
class player:
    def play(self):
        print ("the player is playing cricket.")

#Define the derived class Batman
class Batsman(player):
    def play(self):
        print ("the batsman is batting.")
        
# Define the derived class Bowler 
class Bowler(player):
    def play(self):
        print ("the bowler is bowling.")

#create a objects of Batsman and Bowler classes
batsman=Batsman()
bowler=Bowler()

# call the play() method for each object 
batsman.play()
bowler.play()