with open("input.txt") as f:
    value = f.readlines() 

floor = 0
pos = 0 

### with this one although I quickly understood what I was doing i needed to also 
### keep count of the position or "count". 
### I'm sure there is a simplier way to do this but today (5/12) I just decided to add an addition
### and if statement. 

for i in value:                 
    for a in i:                
        if a == '(':
            floor += 1
            pos += 1
        elif a == ')':
            floor -= 1
            pos += 1 
        if floor == -1:
            print(pos)
            break