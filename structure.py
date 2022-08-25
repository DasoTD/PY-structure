pos =0
while pos < 5:
    print(pos, end='')
    pos +=1
print(' ')

for pos in range(5):
    print(pos, end=',')
print(' ')

for pos in range(5, 10):
    print(pos, end=',')
print(' ')
for pos in range(5, 10, 2): #the third value is called step
    print(pos, end=',')