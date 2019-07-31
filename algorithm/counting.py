arr = [0, 4, 1, 3, 1, 2, 4, 1]
# 양의 정수이고, 최대값을 알아야 함
# 최대값 = 4
tmp = [0] * len(arr)
cnt = [0] * 5  # 배열의 인덱스 0 ~ 4

# 빈도수 계산
for val in arr:
    cnt[val] += 1
# 누적 빈도수 계산
for i in range(1, len(cnt)):
    cnt[i] = cnt[i - 1] + cnt[i]

for j in range(len(arr)-1, -1, -1):
    cnt[arr[j]] -= 1
    tmp[cnt[arr[j]]] = arr[j]

# sorted = []
# for i in range(len(cnt)):
#     for j in range(cnt[i]):
#         sorted.append(i)
print(tmp)