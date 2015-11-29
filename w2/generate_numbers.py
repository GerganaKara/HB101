# generate_numbers.py

import sys
from random import randint

def main():
    filename = sys.argv[1]
    num = int(sys.argv[2])

    with open(filename, 'w') as data:
        for i in range(0,num):
            n = randint(0,1000)

            data.write(str(n) + " ")



if __name__ == '__main__':
    main()