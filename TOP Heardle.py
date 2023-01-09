# You will need:
# Python 3.9.6 or higher 
# pygame (you can install it with pip install pygame)
# to change the file directory on line 30 to the file directory you saved the songs folder to

# Imports
from pygame import mixer
import random
import time

mixer.init() # Initializing pygame mixer

# Variables
# Each number is the amount of seconds
songs = ["Addict With A Pen", "Air Catcher", "Anathema", "Bandiot", "Be Concerned", "Before You Start Your Day",
         "Bounce Man", "Cancer", "Car Radio", "A Car A Torch A Death", "Chlorine", "Choker", "Christmas Saves The Year",
         "Clear", "Cut My Lip", "Doubt", "Fairly Local", "Fake You Out", "Fall Away", "Forest", "Formidable",
         "Friend Please", "Glowing Eyes", "Goner", "Good Day", "Guns For Hands", "Heathens", "Heavydirtysoul",
         "Holding On To You", "Hometown", "House Of Gold", "The Hype", "Implicit Demand For Proof",
         "Isle Of Flightless Birds", "Johnny Boy", "The Judge", "Jumpsuit", "Kitchen Sink", "Lane Boy",
         "Leave The City", "Legend", "Level Of Concern", "Levitate", "Lovely", "March To The Sea", "Message Man",
         "Migraine", "Morph", "Mulberry Street", "My Blood", "Neon Gravestones", "Never Take It", "Nico And The Niners",
         "No Chances", "Not Today", "Ode To Sleep", "Oh Ms Believer", "The Outside", "The Pantaloon", "Pet Cheetah",
         "Polarize", "Redecorate", "Ride", "Ruby", "The Run And Go", "Saturday", "Screen", "Semi-Automatic", "Shy Away",
         "Slowtown", "Smithereens", "Stressed Out", "Taxi Cab", "Tear In My Heart", "Trapdoor", "Trees", "Truce", "Two",
         "We Dont Believe Whats On Tv"]

song = random.choice(songs) # Selects a random song
level = 1
mixer.music.load('D:\Code Stuffs\Python\Twenty-One Pilots Heardle Clone\Songs/' + song + '.mp3') # Loading Music File
# Functions

# Prints the instructions
def instructions():
    print(">>> Listen to the intro, then type the correct song into the prompt!")
    print(">>> Skipped or incorrect attempts unlock more of the intro (to skip press enter)")
    print(">>> Answer in as few tries as possible (some songs may have the first couple seconds in silence")

def question(): # Asks the user for the song
    global level
    guess = input("What do you think the song is? ")
    if guess.lower() == song.lower(): # Checks if the guess is correct
        print("Well done! You got it right in " + str(level) + " tries!")
        quit()
    else:
        level += 1
        if level == 7:
            print("Unlucky, the song was " + song)
            quit()
        print("Incorrect, Onto guess " + str(level) + "!")
        play()



def play(): # Plays the music
    mixer.music.play()  # Playing Music with Pygame
    time.sleep(level)  # stops the music after the level determined time
    mixer.music.stop()
    question()


instructions()

input("Press any key to start!") # Gives the user a button to press when ready
play()
question()
