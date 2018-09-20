def isCombination(string1, string2):
    if len(string1)!=len(string2):
        return False
    else:
        count1 = dict()
        count2 = dict()
        getCount(string1, count1)
        getCount(string2, count2)
        if count1 == count2:
            return True
        else:
            return False

def getCount(string, dic):
    for items in string:
        if items not in dic:
            dic[items] = 1
        else:
            dic[items] += 1

if __name__=="__main__":
    import sys
    print(isCombination(sys.argv[-1], sys.argv[-2]))
