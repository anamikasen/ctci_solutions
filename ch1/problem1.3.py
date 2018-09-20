def urlify(string):
    new = ""
    for s in string:
        if s == " ":
            new += "%" + str(20)
        else:
            new += s
    return new

if __name__=="__main__":
    import sys
    var = raw_input("Please enter something: ")
    print(urlify(var))
