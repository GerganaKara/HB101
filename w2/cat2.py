# cat2.py
import sys


def main():
    
    l = len(sys.argv)

    for i in range(1, l):

        filename = sys.argv[i]
        data = open(filename, 'r')
        print(data.read()+"\n")

    data.close()

if __name__ == '__main__':
    main()
