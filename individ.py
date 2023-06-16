coords = [(10,12),(8,6),(9,12),(9,9),(13,13)]
all_x = []
all_y = []
for coord in coords:
    all_x.append(coord[0])
    all_y.append(coord[1])

first_point = (min(all_x), min(all_y))
second_point = (max(all_x), max(all_y))
print(first_point)
print(second_point)
