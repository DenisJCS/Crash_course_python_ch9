from random import choice

values = [1,4,3,7,10,4,3,2,'a','f','c','r','w','l']

print("The following tickets won the prize")
for i in range(0, 4):
    print(choice(values))
