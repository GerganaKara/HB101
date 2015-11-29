# sum_digits.py

def sum_of_digits(n): 
    sum = 0 

    if n < 0:
        n = -1 * n

    while n % 10 >= 0 and n != 0:
        sum = sum + n%10
        n = n//10 
    
    return sum

# to_number 

def to_number(digits):
    result = 0


    for i in range (0,len(digits)):
        
        digit = digits[i]
        result *= 10 ** i
        result += digit


    return result 

#print(to_number([21, 2, 33]))


def to_digits(n):

    result = []

    while n != 0 and n >0:
        result = [ n % 10] + result
        n = n // 10 

    return result

#print ( to_digits(123023))


def fibonacci(n):

    result = []

    a = 1
    b = 1

    while len(result) < n :
        result. append(a)
        next_number = a + b
        a = b
        b = next_number

    return result

#print(fib(3))

def fib_number(n):
    digits = fibonacci(n)

    result = to_number(digits)

    return result

#print(fib_number(4))

def fact(n):
    result = 1

    for num in range (1,n+1):
        result *= num


    return result 

#print(fact(4))

def fact_digits(n):

    result = 0
    digits = to_digits(n)

    for digit in digits:
        result += fact(digit)

    return result

#print(fact_digits(999))

def palindrome(n):
    return str(n) == str(n) [::-1]

#print(palindrome("kapak"))

def count_vowels(text):
    vowels = 'aeiouy'
    found_vowels = []

    for char in text:
        if char in vowels:
            found_vowels += [char]

    return len(found_vowels) 

#print(count_vowels('aba'))

def count_consonants(text):
    consonants = 'bcdfghjklmnpqrstvwxz'
    found_cons = []

    for char in text:
        if char.lower() in consonants:
            found_cons += [char]

    return len(found_cons) 

#print(count_consonants('aba')) 


def count_occurances(text, ch):
    count = 0

    for item in text:
        if item == ch:
            count += 1 

    return count

#print(count_occurances('asba','s'))

def char_histogram(text):
    d = {}

    
    for ch in text:
        d[ch] = count_occurances(text, ch)

    return d

#print(char_histogram("Python!"))







