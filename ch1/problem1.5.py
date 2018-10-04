def oneAway(string1, string2):
    if len(string1) == len(string2):
        print('checkReplacement')
        return checkReplacement(string1, string2)

    elif len(string1) -1 == len(string2):
        print('checkInsert')
        return checkInsert(string1, string2)

    elif len(string2) - 1 == len(string1):
        print('checkInsert')
        return checkDel(string2, string1)

    else:
        return False

def checkAdd(string1, string2):
    new = ""
    newlst = []
    new = string1+string2
    for items in new:
        newlst.append(items)
    odd = 0
    newlst.sort()
    for i in range(len(newlst)):
        if newlst[i]!=newlst[i+1]:
            if odd > 1:
                return False
            else:
                odd += 1

    return True

# def checkDel(string1, string2):
#
#
# def checkReplacement(string1, string2):


if __name__=="__main__":
    import sys
    print(oneAway(sys.argv[-1], sys.argv[-2]))
