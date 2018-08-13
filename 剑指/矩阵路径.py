'''
题目描述
请设计一个函数，
用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，
每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。

例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中
包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，
路径不能再次进入该格子。
'''

# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        for i in range(rows):
            for j in range(cols):
                if matrix[i * cols + j] == path[0]:
                    if self.func(list(matrix), rows, cols, path[1:], i, j):
                        return True
        return False

    def func(self, matrix, rows, cols, path, i, j):
        if len(path) == 0:
            return True
        matrix[i * cols + j] = '0'
        print(path[0])

        #底下先判断 向前或向上 再判断 向后向左
        if j + 1 < cols and matrix[i * cols + j + 1] == path[0]:
            print('right')
            return self.func(matrix, rows, cols, path[1:], i, j + 1)
        if j - 1 >= 0 and matrix[i * cols + j - 1] == path[0]:
            print('left')
            return self.func(matrix, rows, cols, path[1:], i, j - 1)
        if i + 1 < rows and matrix[(i + 1) * cols + j] == path[0]:
            print('down')
            return self.func(matrix, rows, cols, path[1:], i + 1, j)
        if i - 1 >= 0 and matrix[(i - 1) * cols + j] == path[0]:
            print('up')
            return self.func(matrix, rows, cols, path[1:], i - 1, j)

        return False