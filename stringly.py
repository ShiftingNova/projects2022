def lower_left_triangle(s):
    i = 0
    while i< len(s):
        i = i + 1
        print(s[0:i])
def lower_right_triangle(s):
    i = len(s)-1
    e = 0
    o = len(s)
    while i>=0:
        e = e - 1
        print(" "*(len(s)+e),end ="")
        print(s[i:o])
        i = i - 1
def wordly(word,guess ):
    i = 0
    correct=""
    while i < len(guess):
        if word[i] == guess[i]:
            correct = correct+word[i]
        elif word[i] in guess:
            correct = correct + "+"
        else:
            correct = correct +" "
        i = i+1
    return correct
def first_repitition(s):
    i = 0
    while i < len(s):
        if s[i] == s[i+1]:
            return i
        i = i+1
    return -1
def last_repitition(s):
    i = len(s)-1
    while i > 0:
        if s[i] == s[i-1]:
            return i-1
        i = i -1
    return -1
def begins_with(s,prefix):
    if prefix == s[0:len(prefix)]:
        return True
    else:
        return False
def ends_with(s,suffix):
    i = len(s)
    if suffix == s[i-len(suffix):i]:
        return True
    else:
        return False
def main():
    lower_left_triangle("abcd")
    lower_right_triangle("abcd")

main()
