# Forloop
# Read each element in list
# Iterator object
# Menggunakan for loop
import sys

list = [1,2,3,4,5,6,7,8]
it = iter(list)
it2 = iter(list)
for x in it:
 print(x, end='\n')

print('end "forloop"')

# Menggunakan for next
while True:
 try:
  print(next(it2))
 except StopIteration:
  sys.exit()