import random


def get_word(wordlist="/usr/share/dict/words"):
    the_words=[]
    with open(wordlist) as f:
 #This reads each line from the file, strips leading and trailing whitespaces, and stores the resulting list of words in the variable words.

        words=[x.strip() for x in f] 
        
        for word in words:
            if not word.islower():  #Skips words that are not all lowercase.
                continue
            elif not word.isalpha():  #Skips words that are not all alphabetic.
                continue
            elif len(word) < 5:      #Skips words that are less than 5 characters long.
                continue
            the_words.append(word)
            
    secret_word= random.choice(the_words)  #Randomly chooses a word from the list.
    return secret_word
    
def mask_word(word, guesses):
    mask=[]
    for i in word:   
        if i in guesses:  
            mask.append(i)
        else:
            mask.append("-")
    return "".join(mask)  
    
def display(secret_word, turns_remaining, guesses):  #Displays the status of the game.
    masked_word = mask_word(secret_word, guesses)   #Creates a masked version of the secret word.
    guesses = "".join(guesses)     #Joins the list of guesses into a string.
    return f"""Secret word : {masked_word}
Turns remaining : {turns_remaining}
Guesses so far : {guesses}
"""



def play_round(secret_word, guesses, guess, turns_remaining):   #Plays one round of the game.
    action = "Keep Guessing"  #Initializes the action variable to "Keep Guessing"
    #Checks if the guess is valid.
    if len(guess) >= 2:
        return guesses, turns_remaining, "Invalid Entry -----> Keep Guessing"
    if not guess.isalpha():   #Checks if the guess is alphabetic.
        return guesses, turns_remaining, "Invalid Entry -----> Keep Guessing"
    if not guess.islower():   #Checks if the guess is all lowercase.
        return guesses, turns_remaining, "Invalid Entry -----> Keep Guessing"
    if guess in guesses:      #Checks if the guess has already been guessed.
        return guesses, turns_remaining, action  
    guesses.append(guess)  #Adds the guess to the list of guesses.
    if "-" not in mask_word(secret_word, guesses):  
        return guesses, turns_remaining, "CONGRATULATIONS YOU WON"
    if guess not in secret_word:
        turns_remaining -=1
        if turns_remaining == 0:
            return guesses, turns_remaining, "GAME OVER" 
    return guesses, turns_remaining, action    

def get_pic(turns_remaining):
    if turns_remaining == 6:
    
        return """
      
----------
|        |
|
|
|
|
--------------
"""

    elif turns_remaining == 5:
    
        return """
      
----------
|        |
|        0
|
|
|
|
--------------
"""
    
    elif turns_remaining == 4:
    
        return """
      
----------
|        |
|        0
|        |
|
|
|
--------------
"""  

    elif turns_remaining == 3:
    
        return """
      
----------
|        |
|        0
|       /|
|
|
--------------
"""             

    
    elif turns_remaining == 2:
    
        return """
      
----------
|        |
|        0
|       /|\\
|
|
|
--------------
""" 

    elif turns_remaining == 1:
    
        return """
      
----------
|        |
|        0
|       /|\\
|       /
|
|
--------------
"""     
    
    elif turns_remaining == 0:
    
        return """
      
----------
|        |
|        0
|       /|\\
|       / \\
|
|
--------------
""" 


def main():


    print("+---------+\n  |      |\n  0      |\n / \\     |\n  |      |\n / \\     |\n         |\n+---------+")

    print("WELCOME HANGMAN GAME")
    print("Are you ready?")

    answer = input("Type 'y' if you are ready: ")
    answer = answer.lower()
    if answer == "y":
        print("LET THE GAME BEGIN")
    


        secret_word = get_word()
        turns_remaining = 6
        guesses = []
        action=""  #For displaying the status of the game.
        while True: 
            status = display(secret_word, turns_remaining, guesses)
            image = get_pic(turns_remaining)
            print(image)
            print (status)
            print(action)
            guess = input("Enter your guess--->")
            guesses, turns_remaining, next_action = play_round(secret_word, guesses, guess, turns_remaining)  
            action=next_action
            #Checks if the game is over.
            if next_action == "GAME OVER":
                image = get_pic(turns_remaining)
                print(image)
                print (f"You lost. The word is {secret_word}")
                print(next_action)
                break
            #Checks if the game is won.
            if next_action == "CONGRATULATIONS YOU WON":
                print (f"You won. The word is {secret_word}")
                print(next_action)
                break
    else:
        print("EXIT")
        exit()

    
if __name__ == "__main__":
    main()
        
    
    