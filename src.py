#ASCII art to display the hangman
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#Declare lives = 6
lives  = 6

#Create a random list

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
random_word = random.choice(word_list)

#this is for testing
# print(random_word)

#TODO1.1 - Display the number of letters in the random_word in blanks
output =""
for blank in range (0, len(random_word)) :
    output += "_ "

print(output)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

print("\n")


while "_" in output :
    guess = input("Guess a letter: \n").lower()

    #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

    for pos in range(0,len(random_word)) :
        if (guess == random_word[pos]) :
            # output.replace(f"_ {pos} ", guess, 1)
            # output = output.replace(output[pos], guess)
            #string slicing https://www.w3schools.com/python/python_strings_slicing.asp
            #it will cut the first 2*pos character but not include the 2*pos character


            output = output[:2*pos] + guess + output[2*pos+1:]

    print(output + "\n")

    if guess not in random_word :
        lives -=1
        if lives == 0 :
            print("you lose")
            print(stages[0])
            print("The random word I choose is " + random_word)
            exit()
    print(stages[lives])


print("You win")

