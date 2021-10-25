a = ['1','2','3']
try:
    # fo=open('testopen.txt','r')
    test = input('Enter : ')
    print(a[1])
except IOError:
    print('Error: File not found')
except NameError:
    print('Error: Variable not declared')
except IndexError:
    print('Error: No Index')
except KeyboardInterrupt:
    print('Error: User Interrupted the process')
else:
    print('File oppened')
