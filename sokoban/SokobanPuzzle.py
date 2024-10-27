import pygame
from box import Box
from typing import List
class SokobanPuzzle:
    def __init__(self, board, position , boxes : List[Box]):
        self.row, self.column = position
        self.board = board
        self.boxes = boxes


    def is_goal_state(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == 'b':
                    if self.board[row][col] != 's':
                        return False 
        return True  
    
    def move(self, direction):

        # Move UP
        if direction == pygame.K_UP:
            if self.board[self.row - 1][self.column] == "v":
                self.board[self.row][self.column] = "v"
                self.row -= 1  # Update the player's row position
                self.board[self.row][self.column] = "p"
            elif self.board[self.row -1][self.column] == "b" : 
                self.board = self.boxes[0].move(direction=direction)
                return self.move(direction)

        # Move DOWN
        elif direction == pygame.K_DOWN:
            if self.board[self.row + 1][self.column] == "v":
                self.board[self.row][self.column] = "v"
                self.row += 1  # Update the player's row position
                self.board[self.row][self.column] = "p"
            elif self.board[self.row +1][self.column] == "b" : 
                self.board = self.boxes[0].move(direction=direction)        
                return self.move(direction)

        # Move RIGHT
        elif direction == pygame.K_RIGHT:
            if self.board[self.row][self.column + 1] == "v":
                self.board[self.row][self.column] = "v"
                self.column += 1  # Update the player's column position
                self.board[self.row][self.column] = "p"
            elif self.board[self.row][self.column +1] == "b" : 
                self.board = self.boxes[0].move(direction=direction)
                return self.move(direction)

        # Move LEFT
        elif direction == pygame.K_LEFT:
            if self.board[self.row][self.column - 1] == "v":
                self.board[self.row][self.column] = "v"
                self.column -= 1  # Update the player's column position
                self.board[self.row][self.column] = "p"
            elif self.board[self.row][self.column -1] == "b" : 
                self.board = self.boxes[0].move(direction=direction)
                return self.move(direction)
            
        return self.board
    
