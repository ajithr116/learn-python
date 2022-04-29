'''fruits=["apple","mango","pineapple"]
for i in fruits: #print all the fruits
    print(i)
---------------------------------------------------------------------------------------------------------------------------
for i in "banana":
    print(i) #print alphabet of the fruit her banana so b a n a n a

#----------------------------------------------------------------------------------------------------------------------------


fruits2=["apple","orange","sweet","banana","cherry"]
for i in fruits2:
    print(i) #print all the fruits
    if i == "banana": #if it reach it bananit will break
        break

---------------------------------------------------------------------------------------------------------------------------
#multiple if codition statement
fruits3=["apple","orange","sweet","banana","cherry"]
for i in fruits3: #print fruits
    if i=="apple": #remove apple
        continue #it will display except banana and continue the loop
    if i=="banana": #remove banana
        continue
    print(i)
----------------------------------------------------------------------------------------------------------------------------

for i in range(2,6):
    print(i) #start from 2 and end in 6

-----------------------------------------------------------------------------------------------------------------------

for i in range(2,30,3):
    print(i) #print third numbers   2 5 8 11 14 17 20 23 26 29

-----------------------------------------------------------------------------------------------------------------------'''
for i in range(6):
    print(i) #print  numbers
else: #after loop else will execute
    print("finish")
