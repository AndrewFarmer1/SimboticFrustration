from random import randrange
val = input('Please enter a Word>>>').lower()
charVals = list()
alp = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
shifted = list()
key = randrange(1,25)
ccSto = list()
ccSto=alp[key::]
front = alp[0:key:]
ccSto.extend(front)
for character in val:
    charVals.append(character)
    tmp = alp.index(character)
    Cypher = ccSto[tmp]
    shifted.append(Cypher)
keyVal = key.__str__()
shifted.append(keyVal)
final =''.join([str(item) for item in shifted])
print(final)