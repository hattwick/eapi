# Open file of key-fields from TCAM profiles and create unique set

from collections import Counter

with open('inputdoc.txt', 'r') as file:
    # lines = file.readlines()
    lines = [ line.strip() for line in file ]
    unique = set(lines)
 #   counts = Counter(file.split())

# Raw output for troubleshooting
print(lines)
print(unique)

# Generate list of unique combinations for easier viewing
print("\n".join(unique))
