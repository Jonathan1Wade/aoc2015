with open("input.txt") as f:
    lines = f.readlines()

total_paper = 0

for line in lines:                                              
    l, w, h = list(sorted(map(int, line.strip().split('x'))))       
    
    surface_area = 2*l*w + 2*w*h + 2*h*l
    wrapping_paper = surface_area + l*w
    total_paper += wrapping_paper

print(total_paper)
