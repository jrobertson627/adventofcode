import numpy

def main():
    filename = "input.txt"
    calculate_unique_houses_pt2("^v")

def read_input(filename):
    with open(filename) as f:
        input = f.read()
        count = calculate_unique_houses_pt2(input)
    f.close()
    print(count)

def calculate_movement(input, houses, x_pos, y_pos):
    if input == "^":
        houses = add_houses(houses, x_pos, y_pos + 1)
        return houses, x_pos, y_pos + 1
    if input == ">":
        houses = add_houses(houses, x_pos + 1, y_pos)
        return houses, x_pos + 1, y_pos
    if input == "<":
        houses = add_houses(houses, x_pos - 1, y_pos)
        return houses, x_pos - 1, y_pos
    if input == "v":
        houses = add_houses(houses, x_pos, y_pos - 1)
        return houses, x_pos, y_pos - 1

def add_houses(houses, x_pos, y_pos):
    houses[x_pos][y_pos] = 1
    return houses

def calculate_unique_houses_pt1(string_input):
    x_pos, y_pos, count = (0, 0, 0)
    char_count = len(string_input)
    print(char_count)
    if char_count == 1:
        char_count += 1
    houses = [[0]*char_count]*char_count
    houses = numpy.asarray(houses)
    houses[0][0] = 1
    # print(houses)
    for char in string_input:
        # print("char: ", char, "x", x_pos, "y", y_pos)
        houses, x_pos, y_pos = calculate_movement(char, houses, x_pos, y_pos)
        
    for row in houses:
        for col in row:
            if col == 1:
                count += 1
    # print(houses)
    return count

def calculate_unique_houses_pt2(string_input):
    x_pos_1, y_pos_1, count = (0, 0, 0)
    char_count = len(string_input)
    print(char_count)
    if char_count == 1:
        char_count += 1
    x_pos_2, y_pos_2 = (char_count-1, char_count-1)
    houses_1 = [[0]*char_count]*char_count
    houses_2 = [[0]*char_count]*char_count
    houses_1 = numpy.asarray(houses_1)
    houses_1[0][0] = 1
    houses_2 = numpy.asarray(houses_2)
    houses_2[char_count-1][char_count-1] = 1
    santa_indicator = 1
    # print(houses)
    for char in string_input:
        print(char)
        print(houses_1)
        print(houses_2)  
        if santa_indicator % 2 == 0:
            print("robo")
            houses_2, x_pos_2, y_pos_2 = calculate_movement(char, houses_2, x_pos_2, y_pos_2)
        else:
            print("santa")
            houses_1, x_pos_1, y_pos_1 = calculate_movement(char, houses_1, x_pos_1, y_pos_1)
        santa_indicator += 1
    print(houses_1)
    print(houses_2)  
    houses = numpy.add(houses_1, houses_2)
    for row in houses:
        for col in row:
            if col == 1 or col == 2:
                count += 1
    print(houses)
    return count


if __name__== "__main__":
    main()