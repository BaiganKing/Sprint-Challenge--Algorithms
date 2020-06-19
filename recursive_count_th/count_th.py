'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
"""
I need to go through each 2 letters of the sequence
If those letters are not 'th', I need do the same function, but
one index forward
"""
def count_th(word):
    # Creating a base case. if there are fewer than 2 letters
    # They they can't be 'th'
    if len(word) < 2:
        return 0
    # If they are 'th' add 1 to the count
    if word[0:2] == 'th':
        # then use recursion on the whole word, but one index forward
        return 1 + count_th(word[1:])
    else:
        # Otherwise, I still need to return the recursion,
        # but without adding 1
        return count_th(word[1:])
