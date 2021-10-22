# Forloop
# Read each element in list
# Iterator object
# Menggunakan for loop
import sys

list = [1,'',3,4,5,'',7,8]
it = iter(list)
it2 = iter(list)
for x in it:
 if x == '':
  continue
 print(x, end='\n')

print('end "forloop"')

# Menggunakan for next
print('Start while loop')
while True:
 try:
  print(next(it2))
 except StopIteration:
  #sys.exit()
  break

print('End while loop')





