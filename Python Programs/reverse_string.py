'''
Reverse a String

Write a Python program to reverse a string.

Sample String: "1234abcd"
Expected Output: "dcba4321"
'''

string = "123Hello"

def reverse(a):
    store = ""
    index = len(a)
    while index > 0:
        store += a[index-1]
        index = index - 1
    return store
print(reverse(string))

# OUTPUT
# olleH321




#! USING SLICING METHOD

def str_reverse(string):

    return string[::-1]

print(str_reverse(string))

# Output
# olleH321