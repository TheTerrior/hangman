import os
import sys
from typing import List, Dict, Union
from dataclasses import dataclass


# Global variables
base_chars: str = "abcdefghijklmnopqrstuvwxyzñ" #characters that will be hidden
special_chars: Dict[str, str] = {"à":"a", "è":"e", "ì":"i", "ò":"o", "ù":"u"} #characters that are mapped to base characters
punctuation: str = "!@#$%^&*()_+-=[]{}\\|;:'\",<.>/? `~"    #characters that will be shown by default


# Will hold information about a character in the guessing string
@dataclass
class HChar:
    letter: str
    guessed: bool
    
    # Called when it needs to display
    def display(self) -> str:
        if self.guessed:
            return " " + self.letter
        return " _"

# Same as HChar but for punctuation specifically
@dataclass
class HPunc:
    letter: str
    
    # Called when it needs to display
    def display(self) -> str:
        return self.letter

# Will hold all information about the game, can be passed around
@dataclass
class GameInfo:
    word: str
    chars: List[Union[HChar, HPunc]]
    lives: int


# Gets user input, and verifies before returning
def user_input(message: str) -> str:
    
    #loop until we get a satisfactory input
    while True:
        input_str: str = input(message).lower()
        valid_str: bool = True
        
        #loop through all characters in input, testing for a valid character
        for char in input_str:
            valid_str = valid_str and (char in base_chars or special_chars.get(char) != None or char in punctuation)
            
        if valid_str:
            break

    #return once we are out of the loop
    return input_str


def display_ui(game: GameInfo, status: str):
    print(status)
    print(f"Lives: {game.lives}")
    accum: str = ""

    for i in range(len(game.chars)):
        accum += char.display


# Initializes new games, asks the user if another game should be initiated
def game_loop():
    
    game_running: bool = True   #allows granular control from within the game loop
    while game_running:
        hidden_word: str = user_input("Enter your word: ")
        game_running = False
        
    
# Entry point of the program, calls game_loop
def main():
    game_loop()

if __name__ == "__main__":
    main()
