def main():
    describePart1()
    filename = "input.txt"
    floor, counter = read_file(filename)
    print("Our floor is ", floor)
    describePart2()
    print("At position ", counter, " we reach floor -1")


def describePart1():
    print("Part 1: ")
    print("Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.")
    print("An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor. The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.")
    print("For example: ")
    print("(()) and ()() both result in floor 0.")
    print("((( and (()(()( both result in floor 3.")
    print("))((((( also results in floor 3.")
    print("()) and ))( both result in floor -1 (the first basement level).")
    print(")) and )())()) both result in floor -3.")
    print("To what floor do the instructions take Santa?")
    print("The instructions come in a text file. Parsing this file character by character will allow the floor to be changed as we move through the file. ")

def describePart2():
    print("Part 2: ")
    print("Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.")
    print("For example:")
    print(") causes him to enter the basement at character position 1.")
    print("()()) causes him to enter the basement at character position 5.")
    print("What is the position of the character that causes Santa to first enter the basement?")
    print("Adding a counter to our floor changer will allow us to track position. As we change floors, we check if the floor position is -1. Once the floor is -1 we can check our counter for the position.")

def read_file(filename):
    floor = 0
    counter = 0
    with open(filename) as f:
        for line in f:
            for character in line:
                floor, counter = change_floor(floor, character, counter)
                pos_check = check_floor(floor)
                if pos_check == True:
                    break
    f.close()
    return floor, counter
                
def change_floor(floor, character, counter):
    if character == '(':
        floor += 1
    elif character == ')':
        floor -= 1
    counter += 1
    return floor, counter

def check_floor(floor):
    if floor == -1:
        return True
    else:
        return False


if __name__== "__main__":
    main()