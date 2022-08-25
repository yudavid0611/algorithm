import copy
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

for col in range(len(matrix[0])):
    for row in range(len(matrix)):
        # 가로로 0이 나오기 전이나 끝에 닿을 때까지 반복
        col_max = copy.deepcopy(col)
        while matrix[row][col_max+1] == "1" and col_max+1 < len(matrix[0]):
            col_max += 1

        # 세로로 0이 나오기 전이나 끝에 닿을 때까지 반복
        row_max = copy.deepcopy(row)
        while matrix[row_max+1][col_max] == "1" and row_max+1 < len(matrix):
            row_max += 1

        print(row_max)
        break
    break