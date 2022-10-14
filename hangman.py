import os
import sys
from typing import List, Dict


# Global variables
lives: int = 6  #starting amount of lives
base_chars: str = "abcdefghijklmnopqrstuvwxyzñ" #characters that will be hidden
special_chars: Dict[str, str] = {"à":"a", "è":"e", "ì":"i", "ò":"o", "ù":"u"} #characters that are mapped to base characters
punctuation: str = "!@#$%^&*()_+-=[]{}\\|;:'\",<.>/? `~"    #characters that will be shown by default


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
