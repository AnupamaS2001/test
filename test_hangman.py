import unittest
import test.hangman as hangman
from unittest.mock import patch, call
import builtins
from test.hangman import main
class test_get_word(unittest.TestCase):
        
    def test_get_word(self):
        word = hangman.get_word()  # Call the function to get a word
        
        # Ensure the word meets the criteria
        self.assertTrue(word.islower(), "The word should be all lowercase.")
        self.assertTrue(word.isalpha(), "The word should contain only alphabetic characters.")
        self.assertTrue(len(word) >= 5, "The word should be at least 5 characters long.")

class test_mask_word(unittest.TestCase):
    
    def test_mask_word(self):
        word = "apple"

        mask = hangman.mask_word(word, [])  # Call the function to mask the word
        self.assertEqual(mask, "-----")

        mask = hangman.mask_word(word, ["a", "p", "l", "e"])  # Call the function to mask the word
        self.assertEqual(mask, "apple")

class test_display(unittest.TestCase):
    
    def test_display(self):
        word = "apple"
        turns_remaining = 5
        guesses = ["a", "p", "l", "e"]

        result = hangman.display(word, turns_remaining, guesses)  # Call the function to display the game status
        expected_output = """Secret word : apple
Turns remaining : 5
Guesses so far : aple
"""
        self.assertEqual(result, expected_output)

class test_play_round(unittest.TestCase):
    
    def test_play_round_valid(self):
        guesses = ['a']
        secret_word = 'apple'
        guess = 'p'
        turns_remaining = 5
        expected_guesses = ['a', 'p']
        expected_turns_remaining = 5
        expected_action = "Keep Guessing"
        result = hangman.play_round(secret_word, guesses, guess, turns_remaining)
        self.assertEqual(result, (expected_guesses, expected_turns_remaining, expected_action))
    def test_play_round_invalid(self):
        guesses = []
        secret_word = 'apple'
        guess = 'pp'
        turns_remaining = 5
        expected_guesses = []
        expected_turns_remaining = 5
        expected_action = "Invalid Entry -----> Keep Guessing"
        result = hangman.play_round(secret_word, guesses, guess, turns_remaining)
        self.assertEqual(result, (expected_guesses, expected_turns_remaining, expected_action))
        
    def test_play_round_invalid_non_alpha(self):
        guesses = []
        secret_word = 'apple'
        guess = '1'
        turns_remaining = 5
        expected_guesses = []
        expected_turns_remaining = 5
        expected_action = "Invalid Entry -----> Keep Guessing"
        result = hangman.play_round(secret_word, guesses, guess, turns_remaining)
        self.assertEqual(result, (expected_guesses, expected_turns_remaining, expected_action))
        
    def test_play_round_invalid_non_lowercase(self):
        guesses = []
        secret_word = 'apple'
        guess = 'A'
        turns_remaining = 5
        expected_guesses = []
        expected_turns_remaining = 5
        expected_action = "Invalid Entry -----> Keep Guessing"
        result = hangman.play_round(secret_word, guesses, guess, turns_remaining)
        self.assertEqual(result, (expected_guesses, expected_turns_remaining, expected_action))
    
    def test_play_round_already_guessed(self):
        guesses = ['a']
        secret_word = 'apple'
        guess = 'a'
        turns_remaining = 5
        expected_guesses = ['a']
        expected_turns_remaining = 5
        expected_action = "Keep Guessing"
        result = hangman.play_round(secret_word, guesses, guess, turns_remaining)
        self.assertEqual(result, (expected_guesses, expected_turns_remaining, expected_action))
    
    def test_play_round_won(self):
        guesses = ['a', 'p', 'l']
        secret_word = 'apple'
        guess = 'e'
        turns_remaining = 5
        expected_guesses = ['a', 'p', 'l', 'e']
        expected_turns_remaining = 5
        expected_action = "CONGRATULATIONS YOU WON"
        result = hangman.play_round(secret_word, guesses, guess, turns_remaining)
        self.assertEqual(result, (expected_guesses, expected_turns_remaining, expected_action))
    
    def test_play_round_game_over(self):
        guesses = ['a', 'p']
        secret_word = 'apple'
        guess = 'z'
        turns_remaining = 1
        expected_guesses = ['a', 'p', 'z']
        expected_turns_remaining = 0
        expected_action = "GAME OVER"
        result = hangman.play_round(secret_word, guesses, guess, turns_remaining)
        self.assertEqual(result, (expected_guesses, expected_turns_remaining, expected_action))
        
    def test_play_round_keep_guessing(self):
        guesses = ['a']
        secret_word = 'apple'
        guess = 'z'
        turns_remaining = 5
        expected_guesses = ['a', 'z']
        expected_turns_remaining = 4
        expected_action = "Keep Guessing"
        result = hangman.play_round(secret_word, guesses, guess, turns_remaining)
        self.assertEqual(result, (expected_guesses, expected_turns_remaining, expected_action))

class test_get_pic(unittest.TestCase):

    def test_turns_remaining_6(self):
        expected_output = """
      
----------
|        |
|
|
|
|
--------------
"""
        self.assertEqual(hangman.get_pic(6), expected_output)

    def test_turns_remaining_5(self):
        expected_output = """
      
----------
|        |
|        0
|
|
|
|
--------------
"""
        self.assertEqual(hangman.get_pic(5), expected_output)

    def test_turns_remaining_4(self):
        expected_output = """
      
----------
|        |
|        0
|        |
|
|
|
--------------
"""
        self.assertEqual(hangman.get_pic(4), expected_output)

    def test_turns_remaining_3(self):
        expected_output = """
      
----------
|        |
|        0
|       /|
|
|
--------------
"""
        self.assertEqual(hangman.get_pic(3), expected_output)

    def test_turns_remaining_2(self):
        expected_output = """
      
----------
|        |
|        0
|       /|\\
|
|
|
--------------
"""
        self.assertEqual(hangman.get_pic(2), expected_output)

    def test_turns_remaining_1(self):
        expected_output = """
      
----------
|        |
|        0
|       /|\\
|       /
|
|
--------------
"""
        self.assertEqual(hangman.get_pic(1), expected_output)

    def test_turns_remaining_0(self):
        expected_output = """
      
----------
|        |
|        0
|       /|\\
|       / \\
|
|
--------------
"""
        self.assertEqual(hangman.get_pic(0), expected_output)    

class TestMain(unittest.TestCase):
    
    @patch('hangman.play_round', side_effect=[
        (['p'], 6, 'Keep Guessing'),
        (['p', 'y'], 6, 'Keep Guessing'),
        (['p', 'y', 't'], 6, 'Keep Guessing'),
        (['p', 'y', 't', 'h'], 6, 'Keep Guessing'),
        (['p', 'y', 't', 'h', 'o'], 6, 'Keep Guessing'),
        (['p', 'y', 't', 'h', 'o', 'n'], 6, 'CONGRATULATIONS YOU WON')
    ])
    @patch('hangman.display', side_effect=[
        'Secret word : ------\nTurns remaining : 6\nGuesses so far : \n',
        'Secret word : p-----\nTurns remaining : 6\nGuesses so far : p\n',
        'Secret word : py----\nTurns remaining : 6\nGuesses so far : py\n',
        'Secret word : pyt---\nTurns remaining : 6\nGuesses so far : pyt\n',
        'Secret word : pyth--\nTurns remaining : 6\nGuesses so far : pyth\n',
        'Secret word : pytho-\nTurns remaining : 6\nGuesses so far : pytho\n',
        'Secret word : python\nTurns remaining : 6\nGuesses so far : python\n'
    ])
    @patch('hangman.get_pic', side_effect=[
        """
      
----------
|        |
|
|
|
|
--------------
""",
        """
      
----------
|        |
|        0
|
|
|
|
--------------
""",
        """
      
----------
|        |
|        0
|
|
|
|
--------------
""",
        """
      
----------
|        |
|        0
|
|
|
|
--------------
""",
        """
      
----------
|        |
|        0
|
|
|
|
--------------
""",
        """
      
----------
|        |
|        0
|
|
|
|
--------------
"""
    ])
    @patch('hangman.get_word', return_value='python')
    @patch('builtins.input', side_effect=['y', 'p', 'y', 't', 'h', 'o', 'n'])
    @patch('builtins.print')
    def test_main(self, mock_print, mock_input, mock_get_word, mock_get_pic, mock_display, mock_play_round):
        hangman.main()

        print_calls = [
            call("+---------+\n  |      |\n  0      |\n / \\     |\n  |      |\n / \\     |\n         |\n+---------+"),
            call("WELCOME HANGMAN GAME"),
            call("Are you ready?"),
            call("LET THE GAME BEGIN"),
            call('\n      \n----------\n|        |\n|\n|\n|\n|\n--------------\n'),
            call('Secret word : ------\nTurns remaining : 6\nGuesses so far : \n'),
            call(''),
            call("\n      \n----------\n|        |\n|        0\n|\n|\n|\n|\n--------------\n"),
            call('Secret word : p-----\nTurns remaining : 6\nGuesses so far : p\n'),
            call('Keep Guessing'),
            call("\n      \n----------\n|        |\n|        0\n|\n|\n|\n|\n--------------\n"),
            call('Secret word : py----\nTurns remaining : 6\nGuesses so far : py\n'),
            call('Keep Guessing'),
            call("\n      \n----------\n|        |\n|        0\n|\n|\n|\n|\n--------------\n"),
            call('Secret word : pyt---\nTurns remaining : 6\nGuesses so far : pyt\n'),
            call('Keep Guessing'),
            call("\n      \n----------\n|        |\n|        0\n|\n|\n|\n|\n--------------\n"),
            call('Secret word : pyth--\nTurns remaining : 6\nGuesses so far : pyth\n'),
            call('Keep Guessing'),
            call("\n      \n----------\n|        |\n|        0\n|\n|\n|\n|\n--------------\n"),
            call('Secret word : pytho-\nTurns remaining : 6\nGuesses so far : pytho\n'),
            call('Keep Guessing'),
            call('You won. The word is python'),
            call('CONGRATULATIONS YOU WON')
        ]
        
        mock_print.assert_has_calls(print_calls, any_order=False)
   
 
    
    @patch('hangman.exit')
    @patch('hangman.input', return_value='n')
    def test_exit(self,mock_exit,mock_input):
        hangman.main()
        mock_exit.assert_called_once()

if __name__ == '__main__':
    unittest.main()
