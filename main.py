##Q1
##1. Easily read by Python. Input databases.
num = input("Please enter 5 numbers separated by a comma: ")
file.open() = "numList.csv" "w"
file.close();
file.open() = "numList.csv" "r"
print(numList)
dataIn(string(","))
print(numList)
numList.sort()
print(numList)
print(max(numList))
print(min(myList))
import statistics
mean = statistics.mean(numList)
print(mean)
import matpyplot as ply
names = []
pets = []
names = input("Please enter your name: ")
pets = int("How many pets do you have?: ")
ply.bar(names, pets)

##Q2
##(a) Abstraction is taking out unecessary information in a problem.
##(b) Functions can be used to achieve abstraction as you can use them to input the necessary data and leave behind the unecessary data

##Q3
##(a) 01001010 + 10011001 = 11111011
##(b) 11111011 = 251

##Q4
def is_anagram(w1, w2):
  if sorted(w1) == sorted(w2):
    return True
  else:
    return False
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
if (sorted(word1)) == (sorted(word2)):
  print(word1, "is an anagram of", word2)
else:
  print(word1, "is NOT an anagram of", word2)
def is_anagram(w1, w2):
   if sorted(w1) == sorted(w2):
    return True
   else:
     return False
if (sorted(word1)) == (sorted(word2)):
  print(word1, "is an anagram of", word2)
  phrase = input("Enter a phrase: ")
  if (sorted(word1)) == (sorted(phrase)):
    print(word1, "is an anagram of", phrase)
  else:
    print(word1, "is NOT an anagram of", phrase)
  if (sorted(word2)) == (sorted(phrase)):
    print(word2, "is an anagram of", phrase)
  else:
    print(word2, "is NOT an anagram of", phrase)
else:
  print(word1, "is NOT an anagram of", word2)
  phrase = input("Enter a phrase: ")
  if (sorted(word1)) == (sorted(phrase)):
    print(word1, "is an anagram of", phrase)
  else:
    print(word1, "is NOT an anagram of", phrase)
  if (sorted(word2)) == (sorted(phrase)):
    print(word2, "is an anagram of", phrase)
  else:
    print(word2, "is NOT an anagram of", phrase)