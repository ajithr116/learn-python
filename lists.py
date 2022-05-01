#luist also similar like sets and tuples, [] is using to implement

list=["a",11,23.45,]
print(list)

#------------------------------------------------------------------------------------------------------------------------------

#nested array

list2=["mouse",["a","b","c"],[1,2,3]]

print(list2[0]) #mouse
print(list2[2]) # 1 2 3

#------------------------------------------------------------------------------------------------------------------------------

#to get length and type of the lists

list3=[1,2,3,4,5]

print(len(list3))  #5
print(type(list3))  #<class 'list'>

#------------------------------------------------------------------------------------------------------------------------------

#to print from an element from selected start to selected end

list4=[1,2,3,4,5,6,7,8]
list4[1]=9
print(list4)

list4[1:4] = [0,11,22] #[1, 9, 3, 4, 5, 6, 7, 8]
print(list4) #[1, 0, 11, 22, 5, 6, 7, 8]

#------------------------------------------------------------------------------------------------------------------------------

#to attach other elements in already existed lists

list5=[1,2,3,4,5,6,7]
list5.append(4)
print(list5)  #[1, 2, 3, 4, 5, 6, 7, 4]

list5.extend([11,22,33]) #[1, 2, 3, 4, 5, 6, 7, 4, 11, 22, 33]
print(list5)

print(list5+[55,66,77])  #[1, 2, 3, 4, 5, 6, 7, 4, 11, 22, 33, 55, 66, 77]

#------------------------------------------------------------------------------------------------------------------------------

#to delete the lists fully from the cpu

list6=[1,2,3,4,5,6]
del list6[2]
print(list6) #[1, 2, 4, 5, 6]

del list6
#print(list6) #deleted

#------------------------------------------------------------------------------------------------------------------------------

#to clear all the elements

list7=[1,2,3,4,5,6,7,8,9]
list7.clear()
print(list7) #[]
list7=[11,22,33,44,55,33,33,33,66,77,88,99]
print(list7.count(33)) # 4
#------------------------------------------------------------------------------------------------------------------------------

#to print sorted order
list8=[5,7,4,8,2,0,3,5,7,2,1,]
list8.sort()
print(list8) #[0, 1, 2, 2, 3, 4, 5, 5, 7, 7, 8]
list8.sort(reverse=True)
print(list8) #[8, 7, 7, 5, 5, 4, 3, 2, 2, 1, 0]


list9=["john","alex","lincon","lily","daisy","alba"]
list9.sort()
print(list9) #['alba', 'alex', 'daisy', 'john', 'lily', 'lincon']

#------------------------------------------------------------------------------------------------------------------------------
# to print the lists without brackets

list10=[99,88,77,66,55,44,33,22,11]
print(list10) #[99, 88, 77, 66, 55, 44, 33, 22, 11]
print(*list10) # 99 88 77 66 55 44 33 22 11
