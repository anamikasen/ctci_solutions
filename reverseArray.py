# array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for i in range(len(array)/2):
#     array[i] = array[len(array)-i-1] + array[i]
#     array[len(array)-i-1] = array[i] - array[len(array)-i-1]
#     array[i] = array[i] - array[len(array)-i-1]
#
# for items in array:
#     print(items)


string = "Anamika Sen"
strng = []
for letters in string:
    strng.append(letters)

for i in range(len(strng)/2):
    temp = strng[i]
    strng[i] = strng[len(strng)-i-1]
    strng[len(strng)-i-1] = temp

print("".join(letters for letters in strng))
