def printme(mystr, num=10):
    print(mystr+str(num))
    return

printme('This is my first function call ', 20)
printme('This is my second function call ', 15)
printme(num = 20, mystr = 'This is my second function call ')

# 1) Required positional arguments
# printme('This is my first function call ', 20)

# 2) Default argument
# def printme(mystr, num=10):

# 3) Keyword arguments
# printme(num = 20, mystr = 'This is my second function call ')