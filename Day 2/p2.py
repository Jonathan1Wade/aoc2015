with open("input.txt") as f:
    lines = f.readlines()

total_paper = 0
total_ribbon = 0
for line in lines:                                              # For each line in the input file                                     
    l, w, h = list(sorted(map(int, line.strip().split('x'))))   # Get the dimensions of the present  
         
    ribbon = 2*l + 2*w + l*w*h             #noticed that the height is alwasy the longest therefore calculating the two shortest sides was easy 
    surface_area = 2*l*w + 2*w*h + 2*h*l
    wrapping_paper = surface_area + l*w
    total_paper += wrapping_paper
    total_ribbon += ribbon

print('Total Paper', total_paper)
print('Total Ribbon', total_ribbon)