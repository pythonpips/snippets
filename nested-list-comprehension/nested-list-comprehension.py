"""author: @pythonpips"""

numbers = [1, 2, 3]
multi_table = [[num*n for n in range(1, 6)] for num in numbers]

# outputs [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15]]