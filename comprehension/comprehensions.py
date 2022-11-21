import os
import glob
from pprint import pp


def file_paths():
    file_sizes = {os.path.realpath(p): os.stat(p).st_size for p in glob.glob('*.py')}
    pp(file_sizes)


def is_prime(x):
    from math import sqrt
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def dict_comprehension():
    country_to_capital = {'United Kingdom': 'London',
                          'Brazil': 'Brasília',
                          'Morocco': 'Rabat',
                          'Sweden': 'Stockholm'}

    inverted_dictionary = {capital: country for country, capital in country_to_capital.items()}
    print(inverted_dictionary.items())



prime_square_divisors = {x*x: (1, x, x*x) for x in range(2, 101) if is_prime(x)}
print(prime_square_divisors)

# ------------------------------------------------------
"Given a list of numbers, remove all odd numbers from the list:"
numbers = [3,5,45,97,32,22,10,19,39,43]
numbers = [number for number in numbers if number % 2 ==0]
print(numbers)

# ------------------------------------------------------
"Given a list of numbers, remove floats (numbers with decimals)"
original_list = [2, 3.75, .04, 59.354, 6, 7.7777, 8, 9]
original_list = [number for number in original_list if isinstance(number, int)]


"Find all of the numbers from 1-1000 that are divisible by 7"
numbers = [3,5,45,97,32,22,10,19,39,43, 35, 42, 1, 7, 49]
numbers = [number for number in numbers if number % 7 == 0]

"Find all of the numbers from 1-1000 that have a 3 in them"
numbers = [number for number in range(1,1000) if str(number).__contains__('3') ]


"Find all of the words in a string that are less than 4 letters"
words = ["test", "string", "newspaper", "sami", "s", "ascsafs"]
words = [word for word in words if len(word)<4]

"Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even, " \
"and the word ‘odd’ if the number is odd. Result would look like ‘odd’,’odd’, ‘even’"
list = ['even' if n%2==0 else 'odd' for n in range(20)]


"Get only the numbers in a sentence like ‘In 1984 there were 13 instances of a protest with over 1000 people attending’"
sentence = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
words = sentence.split()
result = [number for number in words if not number.isalpha()]


'Write a Python program to find the occurrences of 10 most common words in a given text. Go to the editor'
from collections import Counter

text = """The Python Software Foundation (PSF) is a 501(c)(3) non-profit 
corporation that holds the intellectual property rights behind
the Python programming language. We manage the open source licensing 
for Python version 2.1 and later and own and protect the trademarks 
associated with Python. We also run the North American PyCon conference 
annually, support other Python conferences around the world, and 
fund Python related development with our grants program and by funding 
special projects."""

words = text.split()
print(Counter(words).most_common(10))


"""Nested comprehension"""
vals = []

for x in range(10):
    v = []
    for y in range(x):
        v.append(y*3)
    vals.append(v)

print(vals)
