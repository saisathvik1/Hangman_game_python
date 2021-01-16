from random import randint
"""
Hangman problem
"""
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
kill=0
words = ["dictionary","elephant","hackerman","zookeeper"]
word = words[randint(0,len(words)-1)]
final = ["_" for i in range(len(word))]
print(" ".join(final))
life = 6
while "".join(final)!=word and life!=0:
    c = input("Enter any character: ")
    if c in word and c not in final:
        for i in range(len(word)):
            letter = word[i]
            if letter == c:
                final[i] = c
        print(" ".join(final))
    else:
        life-=1
        kill-=1
        print(" ".join(final))
        print(stages[kill])
if "".join(final)==word:
    print("You won!")
else:
    print(stages[0])
    print("You failed")


