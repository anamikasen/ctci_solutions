def isPermutation(string):
    count = dict()
    for s in string:
        if s in count and s is not " ":
            count[s] += 1
        else:
            if s is not " ":
                count[s] = 1
    odd_count = 0
    for k, _ in count.items():
        odd_count += count[k]%2

    if odd_count > 1:
        return False

    return True

if __name__=="__main__":
    var = raw_input("Please enter something: ")
    print(isPermutation(var))
