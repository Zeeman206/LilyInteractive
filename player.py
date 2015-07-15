from text_to_speech import *
from speech_recog import *

class Player:
    def __init__(self, list_of_StoryNodes):
        #requires that first StorNode in list is start node
        self.location = list_of_StoryNodes[0]
        self.completed = {}

        self.name = self.setName()

        #put all nodes in story in dictionary as not completed
        for node in list_of_StoryNodes:
            self.completed[node.name] = False

    def getLoc(self):
        return self.location
 
    def addCompleted(self, current):
        self.completed.append(current.name)

    def setName(self):
        yes = "no"
        while yes.lower() == "no":       
            speak("What is your name?")
            s = getInputString()
            speak("Is your name " + s + "?")
            yes = getInputString()
            while yes.lower() != "no" and yes.lower() != "yes":
                speak("Please say yes or no")
                yes = getInputString()
        return s
