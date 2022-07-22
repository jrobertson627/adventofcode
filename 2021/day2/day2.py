import os

def changeDepth(olddepth, change):
    newdepth = olddepth + change
    return newdepth

def changePos(oldpos, change):
    newpos = oldpos + change
    return newpos

def take_input(filename):
    with open(filename) as f:
        directions = f.read().splitlines()
        f.close()
    fulldirections = map(text_num_split, directions)
    return fulldirections

def text_num_split(piece):
    for index, letter in enumerate(piece, 0):
        if letter.isdigit():
            return [piece[:index], piece[index:]]
            
def runDay():
    if os.getcwd() != "day2":
        os.chdir("day2")
    directions = take_input("test2.txt")
    for x in directions:
        print(directions)