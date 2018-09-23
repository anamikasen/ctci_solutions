# matrix = [[1,2,3,4, 5],[6,7,8,9,10],[11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]]
#
# size = len(matrix)
# print(matrix)
# for i in range(0, (size//2)):
#     for k in range(i, size-1-i):
#         top = matrix[i][k]
#         right = matrix[k][size - 1-i]
#         bottom = matrix[size - 1 -i][size -k-1]
#         left = matrix[size-k-1][i]
#         print(top, right, bottom, left)
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)

        for i in range(0, (size//2)):
            for k in range(i, size-1-i):
                temp = matrix[i][k]
                matrix[i][k] = matrix[size-k-1][i]
                matrix[size-k-1][i] = matrix[size - 1 -i][size -k-1]
                matrix[size - 1 -i][size -k-1] = matrix[k][size - 1-i]
                matrix[k][size - 1-i] = temp
