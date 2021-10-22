def printme(mystr, num=50):
    print(mystr+str(num))
    return

printme('This is my first function call ', 20)
printme('This is my second function call ', 15)
printme('This is my third function call without num param ')
printme(num = 20, mystr = 'This is my fourth function call using keword argument ')

def printwithvarlength(arg1, *args):
    print('Output for arg1 = '+str(arg1))

    print(args)
    for var in args:
        print(var)

    return


# printwithvarlength(20)
printwithvarlength(20,30,40,50,60)

# 1) Required positional arguments
# printme('This is my first function call ', 20)

# 2) Default argument
# def printme(mystr, num=10):

# 3) Keyword arguments
# printme(num = 20, mystr = 'This is my second function call ')

# 4) Variable-length argument