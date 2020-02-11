# challenge 4
def challenge4(nums):
    l = nums.split(',')
    print(l)
    print(tuple(l))

challenge4('1,2,4,3,5,6,3,2')

# challenge 5
class Challenge5():
    def __init__(self):
        self.str = ''

    def get_string(self):
        self.str = input('please enter a string')

    def print_string(self):
        print(self.str)

# test
# obj = Challenge5()
# obj.get_string()
# obj.print_string()


# challenge 6
import math
def challenge6(num_list):
    nums = [int(n) for n in num_list.split(',')]
    results = [str(int(round(math.sqrt((2*50*n)/30)))) for n in nums]
    print(','.join(results))

challenge6('100,150,180')


# challenge 7
def challenge7(row, col):
    grid = []
    for r in range(row):
        grid.append([])
        for c in range(col):
            grid[r].append(r * c)
    print(grid)

challenge7(3,5)

# challenge 8
def challenge8(word_list):
    print(','.join(list(sorted(word_list.split(',')))))

challenge8('without,hello,bag,world')


# challenge 9
def challenge9(s):
    print(s.upper())

challenge9("""Hello world
Practice makes perfect""")

def challenge9_2(*strings):
    for s in strings:
        print(s.upper())

challenge9_2('hello world', 'practice makes perfect', 'fo sho')