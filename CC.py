'This code takes the input of a word performs a ceasar cypher'
from random import *
val = input('Please enter a Word>>>').lower()
charVals = list()
alp = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
CCvals = ["d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c",]
shifted = list()
for character in val:
    charVals.append(character)
    tmp = alp.index(character)
    Cypher = CCvals[tmp]
    shifted.append(Cypher)
final =''.join([str(item) for item in shifted])
print(final)
