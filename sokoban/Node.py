import pygame
import SokobanPuzzle

class Node:
    def __init__(self, state: SokobanPuzzle, parent=None, action=None):
        self.state = state  
        self.parent = parent  
        self.action = action  
        self.f = self.g + self.heuristic()  

    


    def getPath():

        pass


    def getSolution():

        pass

    def setF():

        pass
