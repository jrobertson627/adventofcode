def main():
    package_sum, ribbon_sum = read_input("input.txt")
    describePart1()
    print("They need to order", package_sum, "square feet of wrapping paper.")
    describePart2()
    print("They need to order", ribbon_sum, "feet of ribbon.")

def describePart1():
    print("Part 1:")
    print("The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.")
    print("Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.")
    print("For example:")
    print("A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.")
    print("A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.")
    print("All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?")


def describePart2():
    print("Part 2: ")
    print("The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.")
    print("The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.")
    print("For example:")
    print("A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.")
    print("A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.")
    print("How many total feet of ribbon should they order?")


def read_input(filename):
    package_sum = 0
    ribbon_sum = 0
    with open(filename) as f:
        for line in f:
            num_string = line
            num_string = num_string.rstrip('\n')
            dimensions = num_string.split("x")
            for i in range(0, len(dimensions)):
                dimensions[i] = int(dimensions[i])
            area = calculate_area(dimensions)
            slack = calculate_slack(dimensions)
            package_sum += area
            package_sum += slack
            ribbon_sum += calculate_ribbon(dimensions)
    f.close()
    return package_sum, ribbon_sum

def calculate_slack(dim):
    sides = [dim[0]*dim[1], dim[1]*dim[2], dim[0]*dim[2]]
    return min(sides)

def calculate_area(dim):
    # dimensions = [l, w, h]
    return 2*dim[0]*dim[1] + 2*dim[1]*dim[2] + 2*dim[0]*dim[2]

def calculate_ribbon(dim):
    perimeter = 0
    sides = [dim[0]*dim[1], dim[1]*dim[2], dim[0]*dim[2]]
    min_side = min(sides)
    if dim[0] * dim[1] == min_side:
        perimeter = 2*dim[0] + 2*dim[1]
    elif dim[2] * dim[1] == min_side:
        perimeter = 2*dim[2] + 2*dim[1]
    elif dim[0] * dim[2] == min_side:
        perimeter = 2*dim[0] + 2*dim[2]
    
    return perimeter + (dim[0]*dim[1]*dim[2])
    
if __name__== "__main__":
    main()