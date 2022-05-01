#tuples are used to store multiple items in single variable
#using "(   ) " symbol

my_tuple=("a",222,4.5)
print(my_tuple)
#-----------------------------------------------------------------------------------------------------------------------

#unpacking tuple
my_tuple2=(1,2,3)
a,b,c=my_tuple2 #to access element and store seperate
print(my_tuple2)
print(a)
print(b)
print(c)

#-----------------------------------------------------------------------------------------------------------------------

my_tuple3=("hallo")
my_tuple4=(1,2,3,4,5)
print(type(my_tuple3))  #to get the type
print(type(my_tuple4))

#-----------------------------------------------------------------------------------------------------------------------

my_tuple6=(1,2,3,4,5)
print(my_tuple6[3]) #to access with index number
my_tuple7=("mango",[4,6,7],(2,3,4))
print(my_tuple7[0][2]) #n
print(my_tuple7[0][4]) #o
print(my_tuple7[1][1]) #6
print(my_tuple7[1][2]) #7
print(my_tuple7[2][1]) #3
print(my_tuple7[2][2]) #4


#-----------------------------------------------------------------------------------------------------------------------

#slicing
my_tuple8=('a','s','d','f','g','h')
print(my_tuple8[1:4])  #('s', 'd', 'f')
print(my_tuple8[:4]) #('a', 's', 'd', 'f')
print(my_tuple8[3:])  #('f', 'g', 'h')
print(my_tuple8[:])  #('a', 's', 'd', 'f', 'g', 'h')

#-----------------------------------------------------------------------------------------------------------------------

print((1,2,3,)+(4,5,6))  #(1, 2, 3, 4, 5, 6)
print("repeat "*3) #repeat repeat repeat


#-----------------------------------------------------------------------------------------------------------------------

my_tuple9=("a","s","d","f","f","g","h","j")

print(my_tuple9.count("f")) #2
print(my_tuple9.index("g")) #5

#-----------------------------------------------------------------------------------------------------------------------

#to chech if there is element inside tuple
my_tuple10=("a","s","d","f","g","h","j")

print("b" in my_tuple10) #false
print("s" in my_tuple10) #true

print("j" not in my_tuple10) #false

#-------------------------------------------------------------------------------------------------------------------------

#iteraton (loop) through tuples

my_tuple11=("john","alex","james")
for name in my_tuple11:
    print("hallo" , name)

