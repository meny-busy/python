import PySimpleGUI as sd


layout = [


]

#ascii game for the open screen
def HANGMAN_ASCII_ART():
  return ("""
   _   _
  | | | | 
  | |_| | _ _ _ __   __ __ _ __ ___   __ _ _ ___
  |  _  |/ _'| '_ \ / _'  | '_ ' _ \ / _' | '_ \|
  | | | | (_|| | | | (_|  | | | | | | (_| | | | |
  |_| |_|\_,_|_| |_|\__,  |_| |_| |_|\__'_|_| |_|
                    __ /  |
                  |______/\n""")
#functiom to find word
def choose_word(file_path, index):
  f = open(file_path, 'r')
  file1 = f.read()
  file11 = file1.split( )
  file1_1 = []
  for word in file11:
    file1_1 += [word],
  file1_12 = file1_1[index]
  return file1_12  
#functiom to make word from list to string
def listToString(s):   
    # initialize an empty string 
    str1 = ""  
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    # return string   
    return str1  
#function to print the hangman ascii man for any num of wrong gussed
def print_hangman(num_of_tries):
  if num_of_tries == 6:
    print (""" 
    x-------x
    """)
  elif num_of_tries == 5:
    print ("""
    x-------x
    |
    |
    |
    |
    |
    """)
  elif num_of_tries == 4:
    print ("""
    x-------x
    |       |
    |       0
    |
    |
    |
    """)
  elif num_of_tries == 3:
    print ("""
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """)
  elif num_of_tries == 2:
    print ("""
    x-------x
    |       |
    |       0
    |      /|\.
    |
    |
    """)
  elif num_of_tries == 1:
    print ("""
    x-------x
    |       |
    |       0
    |      /|\.
    |      /
    |
    """)
  elif num_of_tries == 0:
    print ("""
    x-------x
    |       |
    |       0
    |      /|\.
    |      / \.
    |
    """)
#making the word while living the right letters undeleted
def show_hidden_word(secret_word, old_letters_guessed):
  list_word = list(secret_word)
  new_list= []
  for letter in list_word:
    if letter not in old_letters_guessed:
        letter = '_'
    else:
        letter = letter
    new_list += [letter]
  return ' '.join(new_list)
#Function to verify if the latter is valid
def check_valid_input(l_guessed, old_letters_guessed):
  """verify if the latter is valid and did not guessed before
  :param l_guessed: what is the letter that guessd :param old_letters_guessed: list of old letters 
  :type l_guessed: str :type old_letters_guessed: list of str
  :return: true or false
  :type return: str
  """
  if letter_guessed.islower() and len (letter_guessed) == 1 and letter_guessed not in old_letters:
    check = letter_guessed.lower()
  elif (letter_guessed.islower() or letter_guessed.isupper()) ==False and len (letter_guessed) != 1:
    check = ("E1")
  elif (letter_guessed.islower() or letter_guessed.isupper()) == False and len (letter_guessed) == 1:
    check = ("E2")
  else:
    check = ("E3")
  return (letter_guessed.lower() == check)
#function for checking if the player already won
def check_win(secret_word, old_letters_guessed):
  list_word = list(secret_word)
  final_list = []
  for letter in list_word:
    if letter in old_letters_guessed:
      letter = letter
    else:
      letter = '_'
    final_list += letter
  after_check = ''.join(final_list)
  return after_check == secret_word
tries_left = 6
print (HANGMAN_ASCII_ART(),tries_left)
fil_loc = sd.popup_get_text('path file', 'give the path of the file: ')
fil_word = sd.popup_get_text('chose word', 'give number: ')
f = choose_word(fil_loc, int (fil_word)) 
word = listToString(f)
old_letters = []  
layout = [[sd.Text('Let’s start!')]
          [print_hangman(tries_left)]
          [show_hidden_word(word, old_letters)]]
windwo = sd.Window(layout)         
print ('Let’s start!')
print_hangman(tries_left)
print (show_hidden_word(word, old_letters))
#a letter for the game v-3
while check_win(word, old_letters) != True:
    letter_guessed_up = input ("Guess a letter: ")
    letter_guessed = letter_guessed_up.lower()
    resolt_letters = check_valid_input(letter_guessed, old_letters)
    if resolt_letters is True:
        if letter_guessed in word:
            old_letters += [letter_guessed] 
            print (show_hidden_word(word, old_letters))
        else:
            old_letters += [letter_guessed] 
            print (show_hidden_word(word, old_letters))
            tries_left -= 1
            print_hangman(tries_left)
    else:
        print ('X')
        tries_left -= 1
        print (show_hidden_word(word, old_letters))
        print_hangman(tries_left)
    print (' -> '.join(old_letters))
    if tries_left == 0:
        print ('lose')
        break
if tries_left > 0:
  print ('you win')
input('Press ENTER to exit')


 

f.mainloop()