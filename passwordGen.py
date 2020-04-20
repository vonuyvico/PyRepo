import random
import re

#change this to false if you don't want numbers on your password
addRandomNumbers = True

#variables
username = str(input("Username: "))
index = 0
upperOrLower = []
finalRes = []
index2a = 0
#make decisions
for x in range(len(username)):
	decision = random.randint(0,1)
	if(decision is 0):
		upperOrLower.append(True)
	else:
		upperOrLower.append(False)
#Apply decisions
for i in range(len(username)):
	if(upperOrLower[index]):
		finalRes.append(username[index].lower())
	else:
		finalRes.append(username[index].upper())
	index+=1
s = ""
#lowkey final
s = s.join(finalRes)

#reset index to 0
index = 0

def enc(that):
	if(that is "a"):
		return "@"
	elif(that is "A"):
		return "4"
	elif(that is "O"):
		return "0" #zero
	elif(that is " "):
		# reduce oof hackedt
		decision2 = random.randint(0,1)
		if(decision2 is 0):
		    return "!"
		else:
			return "_"
	elif(that is "E"):
		return "3"
	else:
		return that

secondVal = []
				
for y in range(len(s)):
	secondVal.append(enc(s[index]))
	index += 1

#real final no lowkey shit	
finalOutput = "".join(secondVal) + "{0}" if addRandomNumbers else "".join(secondVal) 
print(finalOutput.format(random.randint(5000, 10000)))