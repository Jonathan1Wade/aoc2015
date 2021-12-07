with open('input.txt', 'r') as file:
    data = file.read()

def every_second_element(values):
    second_values = []

    for index in range(1, len(values), 2):
        second_values.append(values[index])

    return second_values 


loc = [0, 0]        #understood I needed a starting location 
visited = []        #Thought I was first looking for a count of visited locations, not an empty list

for n in data[::2]:     
    if n == '^':            
        loc[1] += 1
    elif n == '>':
        loc[0] += 1
    elif n == '<':
        loc[0] -= 1
    elif n == 'v':
        loc[1] -= 1
    else:
        break

    if str(loc) not in visited:         #if the location is not in the visited list
        visited.append(str(loc))  

robo = [0, 0]       #I needed a starting location for the second robot  
visited2 = [] 

for b in data[1::2]:     
    if b == '^':            
        robo[1] += 1
    elif b == '>':
        robo[0] += 1
    elif b == '<':
        robo[0] -= 1
    elif b == 'v':
        robo[1] -= 1
    else:
        break

    if str(robo) not in visited2:         #if the location is not in the visited list
        visited2.append(str(robo))        #add it to the list. This was new for me, working out how to append to a list not just count a number. 


print((len(visited)+1)+ (len(visited2)))

