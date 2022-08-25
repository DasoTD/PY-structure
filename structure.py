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
print(' ')
for pos in range(10, 0, -2): #the third value is called step
    print(pos, end=',')
print(' ')


# n = int(input())
# for i in range(n):
#     for j in range(n):
#         if i ==j or n-i-1 ==j:
#             print("*", end='')
#         else:
#             print("", end="")
#         print()
def our_min(a,b):
    if a<b:
        return a
    else:
        return b
def our_max(a, b):
    if a>b:
        return a
    else:
        return b
a,b = 5,10
our_min(a,b)
our_max(a,b)
