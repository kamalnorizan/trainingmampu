inputStr = input('Please enter your age : ')
print('Received input for age is : ',inputStr)

fo = open("myTxtfile.txt", 'a')
fo.write('Test write in file your age '+str(inputStr)+'\n')
fo.close()