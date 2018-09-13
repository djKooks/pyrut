import re
import string
import numpy as np
import random
import libpyrust


def count_doubles(val):
    """Count repeated pair of chars ins a string"""
    total = 0
    for c1, c2 in zip(val, val[1:]):
        if c1 == c2:
            total += 1
    return total


def search_word(target, val):
    word_list = val.split(' ')
    total = 0
    for word in word_list:
        if word == target:
            total += 1

    return total

def sum_list(val):
    num_list = random_list
    sum = 0
    for num in num_list:
        sum += num
    
    return sum

def sum_np_list(val):
    sum = val.sum(0)
    
    return sum


double_re = re.compile(r'(?=(.)\1)')


def count_doubles_regex(val):
    return len(double_re.findall(val))


val = ''.join(random.choice(string.ascii_letters) for i in range(1000000))

ny_data = ''
with open('nystreet.txt', 'r') as myfile:
    ny_data = myfile.read().replace('\n', '')

random_list = random.sample(range(1, 99999), 10)
np_random_list = np.array(random_list)

def test_python(benchmark):
    benchmark(sum_list, random_list)

def test_rust(benchmark):   #  <-- Benchmark the Rust version
    benchmark(libpyrust.sum_list, random_list)


'''
def test_python(benchmark):
    benchmark(sum_list, random_list)

def test_rust(benchmark):   #  <-- Benchmark the Rust version
    benchmark(libpyrust.sum_list, random_list)

def test_np(benchmark):
    benchmark(sum_np_list, np_random_list)
'''
'''
def test_python(benchmark):
    benchmark(search_word, 'NY', ny_data)

def test_rust(benchmark):   #  <-- Benchmark the Rust version
    benchmark(libpyrust.search_text, 'NY', ny_data)
'''


'''



def test_pure_python(benchmark):
    benchmark(count_doubles, val)


def test_regex(benchmark):
    benchmark(count_doubles_regex, val)


def test_rust(benchmark):   #  <-- Benchmark the Rust version
    benchmark(librust2py.count_doubles, val)
'''
