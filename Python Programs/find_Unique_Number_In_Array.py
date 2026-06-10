# Find the unique number in the given array if other numbers are repeated
# Using the XOR 
# a ^ a = 0
# a ^ 0 = a

array = [2,3,4,7,7,3,2]

def repeat(a):
    unique = 0
    for i in a:
        unique ^= i
    return unique

print(repeat(array))

# OUTPUT
# 4
