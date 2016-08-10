#!/usr/bin/env python3
# HW06_ch09_ex05.py

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all
# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou: 598
#   - # of words that use all aeiouy: 42
##############################################################################
# Imports

# Body
def uses_all(word, letters_req):
    for letter in letters_req:
        if letter not in word:
            return False
    return True

def all_vowels():
    try:
        fin = open("words.txt")
    except:
        print("File not found")
    count_vowels = 0
    count_y = 0
    count_vow = []
    count_yy = []
    for line in fin:
        if uses_all(line, "aeiou"):
            count_vowels += 1
        if uses_all(line, "aeiouy"):
            count_y += 1
    print("# of words that use all aeiou: {}".format(count_vowels))
    print("# of words that use all aeiouy: {}".format(count_y))       
                


##############################################################################
def main():

    all_vowels()

if __name__ == '__main__':
    main()
