strng = "Today is a good day"
lst = [ tchar for tchar in strng ]


def reverseList(lst):
    for i in range(len(lst)/2):
        temp = lst[i]
        lst[i] = lst[len(lst)-i-1]
        lst[len(lst)-i-1] = temp

    return lst


if __name__=="__main__":
    lst = reverseList(lst)
    first = 0
    second = first
    import pdb; pdb.set_trace()
    while second!=len(lst)-1:
        while lst[second]!=" ":
            second+=1
            if second == len(lst):
                break
        print(lst[first:second])
        first = second+1
        second+=1
