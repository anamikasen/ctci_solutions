def main():
    return isRotation(s1, s2)

def isRotation(s1, s2):
    if len(s1)!=len(s2):
        return False
    else:
        return isSubstring(s1, s2)

def isSubstring(s1, s2):
    s1 += s1
    return s1.find(s2)>-1

if __name__ == "__main__":
    s1 = "body"
    s2 = "dybo"
    print(isRotation(s1, s2))
