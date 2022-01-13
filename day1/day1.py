def read_input(filename):
    numbers = []
    with open(filename) as f:
        list_of_lines = f.read().splitlines()
        f.close()
    numbers = list(map(int, list_of_lines))
    return numbers

def getNumLarger_Part1(src_array):
    src_size = len(src_array)
    prevnum = src_array[0]
    counter = 0
    for curr_index in range(1, src_size):
        thisnum = src_array[curr_index]
        if thisnum > prevnum:
            counter+=1
        prevnum = thisnum
    return counter

def getLargerTrio_Part2(src_array):
    src_size = len(src_array)
    counter = 0
    firstnum = src_array[0]
    secondnum = src_array[1]
    thirdnum = src_array[2]
    prevsum = firstnum + secondnum + thirdnum
    for index in range(3, src_size):
        firstnum = secondnum
        secondnum = thirdnum
        thirdnum = src_array[index]
        thissum = firstnum + secondnum + thirdnum
        if thissum > prevsum:
            counter +=1
        prevsum = thissum
    return counter

def runDay():
    src_array = read_input("input.txt")
    count1 = getNumLarger_Part1(src_array)
    count2 = getLargerTrio_Part2(src_array)  
    print('There are %s measurements that are larger than the previous' % count1)
    print('There are %s measurement trios that are larger than the previous' % count2)
    return 0
