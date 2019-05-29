# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurrences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

def find_last(s,t):
    first = s.find(t)
    while True:
        sec = s.find(t, first + 1)
        if sec == -1:
            break
        first = sec

    return first

