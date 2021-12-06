with open('input.txt', 'r') as file:
    data = file.read()


loc = [0, 0]        #understood I needed a starting location 
visited = []        #Thought I was first looking for a count of visited locations, not an empty list

for n in data:     
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
        visited.append(str(loc))        #add it to the list. This was new for me, working out how to append to a list not just count a number. 

print(len(visited)+1)