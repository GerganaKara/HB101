import json
import sys


def read_json(m):
    with open(m, 'r') as f:
        data = json.load(f)

    return data

#print(read_json())

string = read_json(sys.argv[1])
n = string['people']

print (n[1][1])

rank = {}
 
