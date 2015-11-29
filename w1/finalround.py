def count_words(arr):

    result = {}

    for word in arr:

        if word in result:
            result[word] += 1

        else:
            result[word] = 1

    return result

# print (count_words(["apple", "banana", "apple", "pie"]))


def nan_expand(times):
    result = ""

    if times == 0:
        result = "\"\""

    else:
        result += "\"" + (times * "Not a ") + " NaN \""

    return result

# c = (nan_expand(2))


def iterations_of_nan_expand(expanded):

    text = expanded.split()

    a = "Not"
    b = "a"
    c = "NaN"

    counter = 0

    if (a in text and b in text and c in text):

        for i in range(0, len(text) - 1):

            if text[i] == b:
                counter += 1

    return counter

# print(iterations_of_nan_expand("Not a Not a Not a Not a NaN"))

# f group takes list of nums and returns list of list of nums

def group(nums):
    result = [[nums[0]]]
    
    for i in range(0, len(nums)-1):
        result


    return result


print(group([1, 1, 1, 2, 3, 1, 1]))

"""def max_consecutive(items):

    result = []
    gr_items = group(items)
    max_item = len(gr_items[0])

    for i in range(0,len(gr_items)-1):
        if len(gr_items[i]) > len(gr_items[i+1]):
            max_item = len(gr_items[i+1])        i


    return result"""







