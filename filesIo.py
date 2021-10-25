inputStr = input('Please enter your age : ')
print('Received input for age is : ',inputStr)

fo = open("myTxtfile.txt", 'a+')
fo.write('Test write in file your age '+str(inputStr)+'\n')
position = fo.seek(0,0)
print(fo.tell())

line2 = fo.readlines()

for line in line2:
    print(line)
print('Ended')

position = fo.seek(0,0)
while True:
    next_line = fo.readline()

    if not next_line:
        break
    print(next_line)

fo.close()