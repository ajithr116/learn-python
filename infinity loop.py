''''#infinity loop
count=0
while True: #condition is True , execute infinit times
    num=int(input("enter the number"))
    print("number is ",num)
    #if num==0: #using if to stop
        #break
    count+=1 #using count to stop a number of loop
    if count==3:
        break

------------------------------------------------------------------------------------------------------------------------
vowel="aeiouAEIOU"
while True:
    v=input("enter a vowel")
    if v in vowel:
        print("its vowel ")
        break
    else:
        print("its not")

#--------------------------------------------------------------------------------------------------------------------------'''

import random2

while True:
 input("enter the number to roll the dice  ")
 num=random2.randint(1,6)
 print("you got ", num)
 option=input("roll again ? .....yes (y) or no (n)  ")

 if option=="n":
   break
 #if option== "No"or option=="NO" or option=="nO" or option=="no" or option=="n" or option=="o":
  #break
