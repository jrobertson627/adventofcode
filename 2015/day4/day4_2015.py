from hashlib import md5

def main():
    init = 'iwrupvqb'
    myFiveInt = find_five_zeroes(init)
    print(myFiveInt)
    mySixInt = find_six_zeroes(init)
    print(mySixInt)

def find_five_zeroes(init):
    for i in range(10000000):
        h = md5((init + str(i)).encode()).hexdigest()
        if h[:5] == '00000':
            return i

def find_six_zeroes(init):
    for i in range(10000000):
        h = md5((init + str(i)).encode()).hexdigest()
        if h[:6] == '000000':
            return i

if __name__== "__main__":
    main()
