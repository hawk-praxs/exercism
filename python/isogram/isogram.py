'''
Determine if a word or phrase is an isogram.

An isogram (also known as a "nonpattern word") is a word or phrase without a
repeating letter, however spaces and hyphens are allowed to appear multiple 
times.

Examples of isograms:
lumberjacks
background
downstream
six-year-old

The word isograms, however, is not an isogram, because the s repeats.
'''

def is_isogram(string):
    string_char = [char.lower() for char in string if char not in [' ', '-']]
    char_count = [string_char.count(ele) for ele in string_char]
    count_boolean = [False for val in char_count if val != 1]
    
    if False in count_boolean:
        return False
    return True