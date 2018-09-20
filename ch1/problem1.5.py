def oneAway(string1, string2):
    if len(string1) == len(string2):
        return checkReplacement(string1, string2)

    elif len(string1) > len(string2):
        return checkAdd(string1, string2)

    else:
        return checkDel(string1, string2)

def checkAdd(string1, string2):
    new = ""
    newlst = []
    new = string1+string2
    for items in new:
        newlst.append(items)
    odd = 0
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
