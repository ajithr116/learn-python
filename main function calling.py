def get_integer():
    result = int(input("enter integer "))
    return result #return to get_integer

def main():
    print("started... ")
    output = get_integer() #go to get_integer function and store in output variable
    print("integer is ", output)


if __name__ == "__main__": #__name__ is special variable builtin python that shows current module
    main()#go to main function













