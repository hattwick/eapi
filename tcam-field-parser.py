# Open file of key-fields from TCAM profiles and create unique set

from collections import Counter

with open('inputdoc.txt', 'r') as file:
    lines = file.readlines()

print(lines)
