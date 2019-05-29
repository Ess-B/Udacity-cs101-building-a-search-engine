# The range of a set of values is the maximum value minus the minimum
# value. Define a procedure, set_range, which returns the range of three input
# values.


def set_range(a,b,c):
    # Your code here
    if a > b or a > c:
        if b > c:
            ans = a-c
        else:
            if a > c:
                ans = a - b
            else: 
                ans = c - b
    else:
        if b >c:
            ans = b - a
        else:
            ans = c - a
    return ans
    
    
