import random

logo = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
'''
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']
stages.reverse()
word_list = [
    "apple", "banana", "orange", "grape", "kiwi", "pear", "peach", "plum", "melon", "cherry",
    "car", "bike", "train", "plane", "boat", "bus", "rocket", "helicopter", "submarine", "truck",
    "dog", "cat", "elephant", "giraffe", "zebra", "lion", "tiger", "rabbit", "horse", "sheep",
    "mountain", "river", "ocean", "forest", "desert", "lake", "beach", "valley", "hill", "island",
    "book", "pen", "pencil", "notebook", "paper", "marker", "eraser", "stapler", "scissors", "glue",
    "computer", "phone", "tablet", "laptop", "television", "radio", "camera", "microphone", "speaker", "headphones",
    "sun", "moon", "star", "planet", "galaxy", "universe", "comet", "asteroid", "meteor", "telescope",
    "mountain", "hill", "river", "lake", "desert", "valley", "forest", "ocean", "sky", "cloud",
    "pen", "book", "notebook", "paper", "library", "classroom", "school", "university", "teacher", "student",
    "actor", "actress", "musician", "director", "producer", "camera", "stage", "performance", "audience", "theater",
    "cake", "cookie", "pie", "brownie", "icecream", "chocolate", "donut", "cupcake", "popcorn", "soda",
    "friend", "family", "love", "happiness", "joy", "peace", "freedom", "adventure", "journey", "explore",
    "light", "dark", "night", "day", "morning", "afternoon", "evening", "sunrise", "sunset", "twilight",
    "basket", "baboon", "noob", "fortnite", "clipped", "headshot", "fullboxed"
]
print(logo)
print("===============================================")
lives = 6
chosen_word = random.choice(word_list)


placeholder = ""
num_blanks = len(chosen_word)

for blank in range(num_blanks):
    placeholder += "_"
print(f"Word to guess: " + placeholder)

game_over = False
correct_letters = []
while not game_over:


    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(f"Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, which is not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"The word was {chosen_word}!\n""**********************************YOU "
                  "LOSE**********************************")
    print(stages[lives])
    print(f"**********************************{lives}/6 LIVES LEFT**********************************")
    if "_" not in display:
        game_over = True
        print(
            f"Correct! The word was {chosen_word}\n""**********************************YOU "
            f"WIN!**********************************")