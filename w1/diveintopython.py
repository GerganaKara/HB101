from firstday import to_digits, palindrome


def is_number_balanced(n):
    is_balanced = False

    digits = to_digits(n)
    l = len(digits)

    if l == 1:
        is_balanced = True

    elif l % 2 == 0:
        left_s = sum(digits[: l / 2 - 1])
        right_s = sum(digits[l / 2:])

        if left_s == right_s:
            is_balanced = True

    else:
        left_s = sum(digits[: l // 2])
        right_s = sum(digits[l // 2 + 1:])

        if left_s == right_s:
            is_balanced = True

    return is_balanced

# print(is_number_balanced(28471))


def is_increasing(seq):
    is_up = True

    for i in range(0, len(seq) - 1):
        if seq[i] >= seq[i + 1]:
            is_up = False

    return is_up

# print(is_increasing([1]))


def is_decreasing(seq):
    is_down = True

    for i in range(0, len(seq) - 1):
        if seq[i] <= seq[i + 1]:
            is_down = False

    return is_down


# print(is_decreasing([100]))


def get_largest_palindrome(n):
    n -= 1

    while n >= 0:
        if palindrome(n):
            break
        n -= 1

    return n


# print(get_largest_palindrome(994687))


def prime_numbers(n):

    all_num = [i for i in range(2, n + 1)]

    for i in range(2, n + 1):
        not_primes = [x for x in range(i * 2, n + 1, i)]
        all_num = set(all_num) - set(not_primes)

    return sorted(list(all_num))


# print(prime_numbers(10))


def is_anagram(a, b):
    a = a.lower()
    b = b.lower()

    letters_a = [l for l in a]
    letters_b = [l for l in b]

    return len(set(letters_a) - set(letters_b)) == 0

#print(is_anagram("TOP_CODER", "COTO_PRODE"))


def birthday_ranges(birthdays, ranges):

    result = []

    for pair in ranges:

        counter = 0

        for day in birthdays:
            if day in range(pair[0], pair[1] + 1):
                counter += 1

        result += [counter]

    return result

#print(
#birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]))

def sum_matrix(m):
    sum1 = 0

    for item in m:
        sum1 += sum(item)
        
    return sum1

#m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
#print(sum_matrix(m))

