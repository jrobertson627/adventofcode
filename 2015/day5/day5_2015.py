def main():
    nice_string = 0
    new_good = 0
    with open("input.txt") as f:
        for line in f:
            if check_bad_strings(line) == 1:
                if check_doubles(line) == 1:
                    if check_vowels(line) == 1:
                        nice_string += 1
            if check_pairs(line) == 1:
                if check_repeat_letters(line) == 1:
                    new_good += 1
    f.close()
    describePart1()
    print("Under these rules,", nice_string, "strings are nice")
    describePart2()
    print("Under these rules,", new_good, "strings are nice")

def describePart1():
    print("Part 1:")
    print("Santa needs help figuring out which strings in his text file are naughty or nice.")
    print("A nice string is one with all of the following properties:")
    print("It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.")
    print("It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).")
    print("It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.")

def describePart2():
    print("Part 2:")
    print("Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.")
    print("Now, a nice string is one with all of the following properties:")
    print("It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).")
    print("It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.")

def check_vowels(phrase):
    count = 0
    for char in phrase:
        if "a" in char:
            count += 1
        
        if "e" in char:
            count += 1
        
        if "i" in char:
            count += 1
        
        if "o" in char:
            count += 1

        if "u" in char:
            count += 1

    if count >= 3:
        return 1
    
    else:
        return 0

def check_doubles(phrase):
    #check using ASCII characters 97 - 122
    value = 97
    str_val = ""
    while value < 123:
        str_val = chr(value)
        str_val += chr(value)
        if str_val in phrase:
            return 1
        value += 1
    return 0

def check_bad_strings(phrase):
    if "ab" in phrase:
        return 0

    elif "cd" in phrase:
        return 0

    elif "pq" in phrase:
        return 0

    elif "xy" in phrase:
        return 0

    else:
        return 1

def check_pairs(phrase):
    str_val = ""
    for value1 in range(97, 123):
        for value2 in range(97, 123):
            str_val = chr(value1)
            str_val += chr(value2)
            str_val_reverse = str_val[::-1]
            if phrase.find(str_val) == -1:
                if phrase.find(str_val_reverse) == -1:
                    count = 0

            else:
                index1 = phrase.find(str_val)
                index3 = phrase.find(str_val, index1 + 2)
                if index1 != index3 and index3 != -1:
                    return 1
                    
                index2 = phrase.find(str_val_reverse)
                index4 = phrase.find(str_val_reverse, index2 + 2)
                if index2 != index4 and index4 != -1:
                    return 1   
    return 0

def check_repeat_letters(phrase):
    str_val = ""
    for value1 in range(97, 123):
        for value2 in range(97, 123):
            str_val = chr(value1)
            str_val += chr(value2)
            str_val += chr(value1)
            if phrase.find(str_val) != -1:
                return 1
    return 0

if __name__== "__main__":
    main()