repeat = 'y'
fo = open("addressbook.txt", 'a+')
while repeat=='y':
    inputName = input('Please enter name : ')
    inputPhone = input('Please enter phone number : ')
    fo.write(inputName+'|'+str(inputPhone)+'\n')
    print('Phone number recorded')
    repeat = input('Do you want to enter another phone number? (y/n)')

position = fo.seek(0,0)
line2 = fo.readlines()

for line in line2:
    print(line)
fo.close()
