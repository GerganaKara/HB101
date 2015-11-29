#sum_nums.py

import sys

def main():
    filename = sys.argv[1]
    data = open(filename, 'r')
    sum1 = 0

    a = data.read()

    result = a.split(' ')
    result = [ x for x in result if x != '']
    print(result)

    for item in result:
        sum1 += int(item)

    print(sum1) 
   

if __name__ == '__main__':
    main()