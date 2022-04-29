'''# nested loop
i=["red","blue","yellow"]
j=["1","2","3"]

for x in i:
    for y in j:
        print(x,y) #prints red 1, red 2,red 3 , blue 1, blue 2,.....

------------------------------------------------------------------------------------------------------------------------

row=5
for i in range(1,row+1): #starts from 1 and ends in 5
    for j in range(1,i+1):
        print("*",end=" ")   #end=" " is using for bydefault print function ends with newline
        print(" ")           #if u dont want to new line u can use end=" "


#output
#*
#* *
#* * *
#* * * *
#* * * * *

--------------------------------------------------------------------------------------------------------------------

for i in range(1,5):
    for j in range(i):
        print(i,end=" ")
    print()

#output

#1
#2 2
#3 3 3
#4 4 4 4
------------------------------------------------------------------------------------------------------------------------

for letter in "elephant":
    if letter=="e" or letter =="h":
        continue
    print("current letter :",letter)

#current letter : l
#current letter : p
#current letter : a
#current letter : n
#current letter : t

------------------------------------------------------------------------------------------------------------------------'''
for letter in "galaxy":
    pass    #pass statement is a null statement
print("last letter",letter)


seq=["a","b","c","d","e"]
for val in seq:
    pass

