l = 23
w = 11
h = 5

surface_area = 0
wrapping_paper = 0
area = 0 
surface_area += 2*l*w + 2*w*h + 2*h*l
wrapping_paper += surface_area + l*w
area = 3 * l * w + 2 * w * h + 2 * h * l

#for line in lines:
    #print(line)
    #l, w, h = line.split('x')
    #l = int(l)
    #w = int(w)
    #h = int(h)
    #print(l, w, h)
    #surface_area += 2*l*w + 2*w*h + 2*h*l   


    #surface_area += 2*l*w + 2*w*h + 2*h*l
    #wrapping_paper += surface_area + l*w


print(surface_area)
print(wrapping_paper)
print(area)