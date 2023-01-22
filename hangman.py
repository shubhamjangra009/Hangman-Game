import random
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
word_list=['ardvark','baboon','camel']
chosen_word=random.choice(word_list)
print(chosen_word)
display=[]
blank=['_']
for l in range(len(chosen_word)):
    display+=blank
print(display)

list_cw=[i for i in chosen_word]
#print(list_cw)
lives=6

while display!=list_cw:
    while lives>0:
        guess=input('Guess a letter: ')
        for pos in range(len(chosen_word)):
            if chosen_word[pos]==guess:
                display[pos]=guess
        if guess not in list_cw:
            lives-=1
                            
        print(display)
        print(f'Lives remaining {lives}')
        print(stages[lives])
        if lives==0:
            print('You lose')
            quit()

        if display==list_cw:
            print('You Won')
            
