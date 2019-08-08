arr = [[9, 20, 2, 18, 11],
[19, 1, 25, 3, 21],
[8, 24, 10, 17, 7],
[15, 4, 16, 5, 6],
[12, 13, 22, 23, 14]]

ix = [-1, 1, 0, 0]
iy = [0, 0, -1, 1]

result = 0
for i in range(5):
    for j in range(5):
        sum_num = 0
        for k in range(4):
            arr_ix = i + ix[k]
            arr_iy = j + iy[k]
            if arr_ix >= 0 and arr_iy >= 0 and arr_ix < 5 and arr_iy <5:
                sum_num += abs(arr[i][j] - arr[arr_ix][arr_iy])
        result += sum_num
print(result)