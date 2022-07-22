def main():
    filename = "input.txt"

def read_input(filename):
    with open(filename) as f:
        for char in f:
            x = 0
    f.close()
    pass

def calculate_movement(input, x_pos, y_pos):
    if input == "^":
        return y_pos + 1
    if input == ">":
        return x_pos + 1
    if input == "<":
        return x_pos - 1
    if input == "v":
        return y_pos - 1

def add_houses(houses, x_pos, y_pos):
    houses[x_pos][y_pos] = [1]
    return houses

def calculate_unique_houses():
    #count 1s in the full array
    pass

if __name__== "__main__":
    main()