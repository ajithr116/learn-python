# dictionary also a type of lists, tuples and sets but in dictionary we can set a keyword to access the elements
# ( key : value )
dict = {
    1:"hallo",
    2:"world"
           }
dict2 = {
    "one":"first",
    "two":"second"
}

print(dict[1])
print(dict2["two"])

#------------------------------------------------------------------------------------------------------------------------

dict3 = {
    "age":26,
    "name":["a","b","c"]
}

print(*dict3["name"]) #a b c
print(*dict3) #age name

#------------------------------------------------------------------------------------------------------------------------

dict4={
    "name":"alice",
    "age": 34
}
dict4["age"]= 24  #changing value

print(dict4["age"])

dict4["address"] = "new york city" # adding key and item

print(dict4["address"])
print(*dict4)

print("working")
print(dict4)
del dict4   #deleted dict4
#print(dict4) ---------------------------------------------------------
#print("not working")   -----------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------

dict5={
    1:"first",
    2:"second",
    3:"third",
    4:"fourth",
    5:"fifth"
}
print(dict5)
print(type(dict5))   #<class 'dict'>
print(len(dict5))   # 5

print(dict5.pop(2))  #{1: 'first', 3: 'third', 4: 'fourth', 5: 'fifth'}
print(dict5)
# print(dict5.pop(7))   #KeyError: 7
dict5.pop(4)
print(dict5)  #{1: 'first', 3: 'third', 5: 'fifth'}

print(dict5.popitem())
print(dict5)  # {1: 'first', 3: 'third'}

dict5.clear()
print(dict5)

#del dict5
#print(dict5) #NameError: name 'dict5' is not defined. Did you mean: 'dict'?

#----------------------------------------------------------------------------------------------------------------------


marks={
    "maths":49,
    "english": 50,
    "chemistry":39
}

print(*marks)
print(marks.get("english"))   #using in dictionary
print(marks["maths"])


persons={
    "name" :"katy",
    "age": 21
}

print("name : ", persons.get("name")) #name :  katy
print("age : ", persons.get("age"))  #age :  21
print("salary : ",persons.get("salary ", 0.0))  #salary :  0.0

#----------------------------------------------------------------------------------------------------------------------

#from creates new dictionary from given sequence of elements

keys= {"a","e","i","o","u"}

vowels = dict.fromkeys(keys)
print(vowels)  # {'o': None, 'a': None, 'i': None, 'u': None, 'e': None}
print(*keys) #o a i u e


# create a dictionary with sequence of keys with value

keys={"a","e","i","o"}
value="vowels"

vowels=dict.fromkeys(keys,value)
print(vowels)  #{'o': 'vowels', 'e': 'vowels', 'a': 'vowels', 'i': 'vowels'}

#----------------------------------------------------------------------------------------------------------------------

# copy from old to new

org_marks={"eng": 42,
           "maths":35,
           "phy": 56
           }
new=org_marks.copy()
print(new)

#----------------------------------------------------------------------------------------------------------------------

temp={
    "december":12,
    "january":23,
    "feb":34,
    "mar":45
}

for temp2 in temp:
    print("working")
    print(temp2)   # working december working january working feb working marworking

for temp3 in temp.items():
    print("working 2 ")
    print(temp3,end="") #working 2  ('december', 12)working 2  ('january', 23)working 2 ('feb', 34)working 2 ('mar', 45)

temp2={}.fromkeys(["sep","oct","nov"],0)
print(temp2) #('mar', 45){'sep': 0, 'oct': 0, 'nov': 0}

