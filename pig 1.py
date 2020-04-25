#done
breaks = int (input ("get 3 digits number:"))
hon = (breaks // 100)
don = ((breaks % 100) // 10)
lon = (breaks % 100 % 10)
al = (hon + don + lon)
print (al)
print (int (al / 3))
print (al % 3)
print (al % 3 == 0)

#done
print ('"Shuffle, Shuffle, Shuffle", say it together!\n Change colors and directions,\n Don\'t back down and stop the player!\n \tDo you want to play Taki?\n \tPress y\\n')

#done
import math
math.sqrt (4)

dir (str)

"MYNAMEISMENDI"[-2::-4]

#done
star = input ("give a string: ")
num = len (star)
num2 = (num//2)
botl = star [0:num2].lower()
botl2 = star [num2:].upper()
bol = botl + botl2
print (bol)

#done
benu = input ("give a string: ")
benu1 = benu[0:1]
benu.replace(benu1, "e")
benu.replace("e", benu1, 0)

#done
wordy = input ("give a word: ")
wordy_back = wordy[-1::-1]
if wordy == wordy_back:
    print ("ok")
else:
    print ("not filandrom")

#done
change_deegres = input ("enter a deegre: ")
change_deegres_number = change_deegres[:-1]
if 'f' in change_deegres:
    print ((float (change_deegres_number) * 5 - 160) / 9)
else:
    print ((float (change_deegres_number) * 9 + 160) / 5)

#done
def last_early(name):
  last_early_lower = name.lower()
  if last_early_lower.count(last_early_lower[-1], 0, -2):
    print ("y")
  else:
      print ("n")
last_early("benle")

#not done
def distance(num1, num2, num3):
    if abs(num1)  abs(num2) or abs(num3):
        print ("yes")
    else:
        print ("no")
distance(1, 2, 10)

#early version of hangman game
  def is_valid_input(letter):
    if (letter_guessed.islower() or letter_guessed.isupper()) and len (letter_guessed) == 1 :
     return (letter_guessed.lower())
    elif (letter_guessed.islower() or letter_guessed.isupper()) ==False and len (letter_guessed) != 1 :
      return ("E1")
    elif (letter_guessed.islower() or letter_guessed.isupper()) == False and len (letter_guessed) == 1 :
     return ("E2")
    else:
     return ("E3")
  letter_guessed = input ("Guess a letter: ")
  resolt_letter = is_valid_input(letter_guessed)
  print (resolt_letter)

  def is_valid_input(letter):
    """verify if the latter is valid
    :param latter: what is the letter that guessd
    :type latter: str
    :return: true or false
    :type return: str
   """
    if (letter_guessed.islower() or  letter_guessed.isupper()) and len (letter_guessed) == 1:
      chek = letter_guessed.lower()
    elif (letter_guessed.islower() or letter_guessed.isupper()) ==False and len (letter_guessed) != 1:
      chek = ("E1")
    elif (letter_guessed.islower() or letter_guessed.isupper()) == False and len (letter_guessed) == 1:
      chek = ("E2")
   else:
      chek = ("E3")
    return (letter_guessed.lower() == chek)
  #a letter for the game v-1
  letter_guessed = input ("Guess a letter: ")
  resolt_letter = is_valid_input(letter_guessed)
  print (resolt_letter)

  #Function to verify if the latter is valid v1
  def check_valid_input(l_guessed, old_letters_guessed):
    """verify if the latter is valid and did not guessed before
    :param l_guessed: what is the letter that guessd :param old_letters_guessed: list of old letters 
    :type l_guessed: str :type old_letters_guessed: list of str
    :return: true or false
    :type return: str
     """
    if (letter_guessed.islower() or  letter_guessed.isupper()) and len (letter_guessed) == 1 and letter_guessed not in old_letters:
      check = letter_guessed.lower()
    elif (letter_guessed.islower() or letter_guessed.isupper()) ==False and len (letter_guessed) != 1:
      check = ("E1")
    elif (letter_guessed.islower() or letter_guessed.isupper()) == False and len (letter_guessed) == 1:
      check = ("E2")
    else:
      check = ("E3")
   return (letter_guessed.lower() == check)

  #a letter for the game v-2
  letter_guessed = input ("Guess a letter: ")
  old_letters = ['a','b','c']
  resolt_letters = check_valid_input(letter_guessed, old_letters)
  print (resolt_letters)

#not done
def shift_left(my_list):
  from collections import deque
  s = my_list
  s_deq = deque(s.split())
  s_deq.rotate(1)
  return (' '.join(s_deq))

print (shift_left('menu'))

#not done
from collections import deque
s = 'I Me You'
s_deq = deque(s.split())
s_deq.rotate(1)
print (' '.join(s_deq))

#not done
def format_list(my_list):
  even_list = my_list[0:-1:2]
  last_list = my_list[-1]
  liste = [even_list] + [last_list]
  return ' '.join(liste)
my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
print (format_list(my_list))

#done
def are_lists_equal(list_1, list_2):
  lisi1 = sorted(list_1)
  lisi2 = sorted(list_2)
  return lisi1 == lisi2
list1 = [1, 2, 8 , 5, 4]
list2 = [1, 2, 5 , 8, 4]
list3 = [1, 2, 8 , 6, 4]
are_lists_equal(list1, list2)

#done
def longest_word(list):
  order_list = sorted(list, key=len)
  return (order_list[-1])
list4 = ["111", "234", "2000", "goru", "birthday", "09"]
print (longest_word(list4))

#done
def squared_numbers(start, stop):
  i = start
  x = stop
  while i <= x:
    print (i * i)
    i = i + 1
squared_numbers(2, 9)

#done
def is_greater(my_list, n):
  big_num = []
  for (number) in my_list:
    if number > n:
      big_num.append(number)
    else:
      continue
  return big_num
list5 = [1, 4, 3, 23, 67]
is_greater(list5, 5)

#not done
def numbers_letters_count(my_str):
  num = my_str.count(range= 10)
my_str = [1, 4, 'meni', 'beli0']
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
my_str.count(int)

#done
def seven_boom(num):
  i = 0
  for i in range(num):
    if int (i) % 7 == 0 or  i % 10 == 7:
      print ('boom')
    else:
      print (i)
    i += i
seven_boom(150)

#done
data = ("self", "py", 1.543)
format_string = "Hello %s.%s learner, you have only %.2f units left before you master the course!"
print(format_string % data)

#done
def my_key(s):
  return s[-1]
def sorted_prices(tuple_list):
 sort_tuple = sorted(tuple_list, key=my_key)
 print (sort_tuple[::-1])
prodocts = [('milk', '19.5'), ('bary', '15.4'), ('rury', '12')]
sorted_prices(prodocts)

#done (50/50) tuple resolt are missing
def mult_tuple(tuple1, tuple2):
  two_num = []
  for i in tuple1:
    for s in tuple2:
      print (i, s)
      print (s, i)
first_tuple = (1, 2)
second_tuple = (4, 5)
mult_tuple(first_tuple, second_tuple)

#done
def are_files_equal(file1, file2):
  file_1 = open(file1,'r')
  file_2 = open(file2,'r')
  file_1_r = file_1.read()
  file_2_r = file_2.read()
  return file_1_r == file_2_r
are_files_equal("C:\\a.txt", "D:\m.txt")

#done
def control_digit(id):
    s = 0
    ide = str(id)
    for i in range(8):
        digit = ide[i]
        digit1 = int(digit) * 2
        if i % 2 == 1:
            if digit1 > 9:
                digit1 = (digit1 % 10) + 1
            else:
                digit1 = digit1
            s = s + digit1
        else:
            s = s + int(digit)
        i = i + 1
    m = 10 - (s % 10)
    if m == 10:
      m = 0
    return m
print(control_digit('02441596'))

#done
def ciser(ple, k):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = ""
    for i in ple:
        if i.islower() == True:
            loc = (alphabet.find(i) + k) % 26
            boc = alphabet[loc]
            cipher = cipher + boc
        else:
            cipher = cipher + i
    return cipher
print(ciser('abcdefghijklmnopqrstuvwxyz', 5))

#done
def dciser(ple, k):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = ""
    for i in ple:
        if i in alphabet:
            loc = (alphabet.find(i) - k) % 26
            boc = alphabet[loc]
            cipher = cipher + boc
        else:
            cipher = cipher + i
    return cipher
print(dciser('axo', 3))

#done
def poiny(ple):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    kalphabet = "pqmxayjwgcnirzsevuoldfkhbt"
    cipher  = ''
    for i in ple:
      a = alphabet.find(i)
      b = kalphabet[a]
      cipher = cipher + b
    return cipher
print(poiny('abal'))

#done
def dpoiny(ple):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    kalphabet = "pqmxayjwgcnirzsevuoldfkhbt"
    cipher  = ''
    for i in ple:
      a = kalphabet.find(i)
      b = alphabet[a]
      cipher = cipher + b
    return cipher
print(dpoiny('pqpi'))

#done
def conti(txt):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = ""
    for i in alphabet:
      m = txt.count(i)
      if m > 0:
        p = int(m * 100 / len(txt))
        print(i, "is", p, "% in text")
conti('abbaleu')







        
