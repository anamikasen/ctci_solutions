def isUnique(string):
    letters = set([])
    for s in string:
        if s in letters:
            return False
        else:
            letters.add(s)
    return True

if __name__=="__main__":
    import sys
    print(isUnique(sys.argv[-1]))
