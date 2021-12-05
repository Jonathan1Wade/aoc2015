
with open("input.txt") as f:
    value = f.readlines() 
print(value)

floor = 0 

for i in value:                 # i is each line in the file
#
#     
### a is each character in the line <<< this is the part that was causing the problem. 
### I needed to go one level deeper to get the value of each character in the line. 
# 
#     
    for a in i:                
        if a == '(':
            floor += 1
        elif a == ')':
            floor -= 1  

print(floor)
