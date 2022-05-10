#if statement or decision making os required if a certain condition is satisfied
a=10

if a==10:
    print("it is ten")

#-------------------------------------------------------------------------------------------------------------------------

b=5
if a<0:
    print("it is negative number")
else:
    print("it is positive number")
#-------------------------------------------------------------------------------------------------------------------------
c=6

if c<0:
    print("it is negative number")
elif c>0:
    print("it is positive number")
else:
    print("error")

#-------------------------------------------------------------------------------------------------------------------------

d=-56

if d>5:
    if d>10:
        print("d is greater then 10")
    else:
        print("d is lesser then 10")
elif d<5:
    if d<5:
        print("d is lesser then 5")
    else:
        print("d is greater then 5")
else:
    print("error")

#-------------------------------------------------------------------------------------------------------------------------

e=4
f=6

if e>f:
    print("e id greater")
elif e==f:
    print("it is equal")
else:
    print("e is lesser ")

#-------------------------------------------------------------------------------------------------------------------------
g=3
h=6
i=4

if g>h:
    if g>i:
        print("g is greater then h and ")
    else:
        print("i is greater ")
else:
    if h>i:
        print("h is greater ")
    else:
        print("error")

#-------------------------------------------------------------------------------------------------------------------------
# one line if statement

j=10
k=11
l=12

print("j is grester ") if j>k else print("k is greater ")

#-------------------------------------------------------------------------------------------------------------------------

m=10
n=9

if m>9 and n>11: # it means that there are 2 condition. if ther are any one condition is wrong, it will not execute
    print("first ")
else:
    print("someone is perfect   ")

#-------------------------------------------------------------------------------------------------------------------------

o,p,q=10,12,-1

if a and b and c:
    print("boolean value ")
else:
    print("no boolean value ")

#-------------------------------------------------------------------------------------------------------------------------
r = False

if r:
    print("boolean value is True ")
else:
    print("false ")

data = False
if not data:
    print("data is false ")
    print(type(data))
else:
    print("true ")

datax=[]

if datax:
    print("true")
else:
    print("flase")

#-------------------------------------------------------------------------------------------------------------------------

s=10
t=10
u=10
v=11

if s==t or u==v:
    print("s==t")
else:
    print("u==v")

aa=False

if aa :
    print("true ")
else:
    print("false ")

#-------------------------------------------------------------------------------------------------------------------------
w=20
x=30
y=20
z=40

if w==y or x==40: # if any condition is true, then it will execute
    print("one is right ")
else:
    print("none is right ")

