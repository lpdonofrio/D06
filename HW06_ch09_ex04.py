#!/usr/bin/env python
# HW06_ch09_ex04.py

# (1)
# Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list.
#   - write uses_only
# (2)
# Can you make a sentence using only the letters acefhlo? Other than "Hoe
# alfalfa?"
#   - write function to assist you
#   - type favorite sentence(s) here:
#       1: ohh loofah loca 
#       2: hello fellah
#       3: fool hellhole
##############################################################################
# Import

# Body
def uses_only(word, string_letters):
    for letter in word:
        if letter not in string_letters:
            return False
    return True

#Why is this function returning True all the time?:
# def uses_only(word, string_letters):
#     for letter in word:
#         if letter not in string_letters:
#             return False
#         else:
#             return True

def sentence():
    try:
        fin = open("words.txt")
    except:
        print("File did not open")
    accepted_words = []
    for line in fin:
        word = line.strip()
        if uses_only(word, "acefhlo"):
            accepted_words.append(word)
    print(accepted_words)



##############################################################################
def main():
    
    sentence()

if __name__ == '__main__':
    main()
