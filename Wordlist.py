#!/usr/bin/env python3

import sys
import itertools
import datetime

YEAR = datetime.datetime.now().year

LEET = {
    'a': ['a', '@', '4'],
    'e': ['e', '3'],
    'i': ['i', '1'],
    'o': ['o', '0'],
    's': ['s', '$', '5'],
    'l': ['l', '1'],
}

SYMBOLS = ['!', '@', '#', '$', '%']

def leet_all(word):
    pools = []
    for c in word.lower():
        pools.append(LEET.get(c, [c]))
    for combo in itertools.product(*pools):
        yield ''.join(combo)

def case_all(word):
    pools = []
    for c in word:
        pools.append([c.lower(), c.upper()])
    for combo in itertools.product(*pools):
        yield ''.join(combo)

def number_suffixes():
    yield ''
    for i in range(0, 10000):
        yield str(i)
    for y in range(1970, YEAR + 1):
        yield str(y)
    yield '123'
    yield '1234'
    yield '123456'
    yield '0123456789'

def symbol_suffixes():
    yield ''
    for s in SYMBOLS:
        yield s
        yield s * 2
        yield s * 3
    for combo in itertools.product(SYMBOLS, repeat=2):
        yield ''.join(combo)

def all_suffixes():
    for n in number_suffixes():
        yield n
    for s in symbol_suffixes():
        yield s
    for s in symbol_suffixes():
        for n in number_suffixes():
            yield s + n

def generate(word):
    seen = set()
    for l in leet_all(word):
        for c in case_all(l):
            for suf in all_suffixes():
                pwd = c + suf
                if pwd not in seen:
                    seen.add(pwd)
                    yield pwd

def main():
    with open(sys.argv[1]) as f:
        for line in f:
            base = line.strip()
            if not base:
                continue
            for pwd in generate(base):
                print(pwd)

if __name__ == "__main__":
    main()
