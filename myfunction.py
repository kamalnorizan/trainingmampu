# pass by value
def printme(str):
    print(str)
    return

printme('This is my first function call')
printme('This is my second function call')

# pass by reference
def updateval(thelist):
    print("Values inside the function before change: ", thelist)
    thelist[3]=70
    print("Values inside the function after changed: ", thelist)
    return

mylist = [10,20,30,40,50]
updateval(mylist)
print("Values outside the function after changed: ", mylist)