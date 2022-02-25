def lower_left_triangle(s):
    '''
    this function prints a triangle using the characters from the string argument "s"
    Args:
        s - is a string variable
    return:
        none
    '''
    index= 0
    while index< len(s):
        index= index+ 1
        print(s[0:index])
def lower_right_triangle(s):
    '''
    this function prints a right hand triangle using the characters from the string argument "s"
    Args:
        s - is a string argument
    return:
        none
    '''
    index= len(s)-1
    e = 0
    o = len(s)
    while index>=0:
        e = e - 1
        print(" "*(len(s)+e), end="")
        print(s[index:o])
        index = index - 1
def wordly(word,guess ):
    '''
    This function checks to see if the guess argument is the same as the word argument. It returns a string depending on
    the amount of characters match in the two strings.
    Args:
        word - is a string argument that is the right answers
        guess - is a string argument that is compaird to see what characters in the string match the ones in word

    return:
        correct - is a string built from the correcct characters in the guess argument
    '''
    index= 0
    correct=""
    while index< len(guess):
        if word[index] == guess[index]:
            correct = correct+word[index]
        elif word[index] in guess:
            correct = correct + "+"
        else:
            correct = correct + " "
        index= index+1
    return correct
def first_repetition(s):
    '''
    this functions check to see when the first set of rpepeating sharacters in the string argument "s" and returns a
    variable depending on the index of the first character in the set
    Args:
        s - is a string variable that is checked
    return:
        an int depending on the index of the string characters
    '''
    index= 0
    while index< len(s):
        if s[index] == s[index+1]:
            return index
        ndex= index+1
    return -1
def last_repetition(s):
    '''
    this functions check to see when the last set of rpepeating sharacters in the string argument "s" and returns a
    variable depending on the index of the last character in the set
    Args:
        s - is a string variable that is checked
    return:
        an int depending on the index of the string characters
    '''
    index= len(s)-1
    while index> 0:
        if s[index] == s[index-1]:
            return index-1
        index= index-1
    return -1
def begins_with(s,prefix):
    if prefix == s[0:len(prefix)]:
        return True
    else:
        return False
def ends_with(s,suffix):
    index= len(s)
    if suffix == s[index-len(suffix):index]:
        return True
    else:
        return False
def main():
    lower_left_triangle("abcd")
    lower_right_triangle("abcd")

main()
