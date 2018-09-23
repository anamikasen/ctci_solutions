class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        zeros = []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeros.append((i, j))

        for items in zeros:
            matrix[items[0]] = [0 for i in range(n)]
            # matrix[items[1]] = [0 for i in range(m)]
            for i in range(m):
                matrix[i][items[1]] = 0
