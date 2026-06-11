'''
Write a Python function that takes a list and 
returns a new list with distinct elements from the first list.
'''


list1 = [1,1,2,3,3,4,4,5,6,7,9,9]

def dup(a):
    out = []
    for x in a:
        if x not in out:
            out.append(x)
    return out
        
print(dup(list1))   

# OUTPUT
# [1, 2, 3, 4, 5, 6, 7, 9]