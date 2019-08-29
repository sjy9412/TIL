import sys
def clac(result):
    global max_num, min_num
    cnt = 0
    tmp = ''
    for i in result:
        if isinstance(i, int):
            if not tmp or tmp == '0':
                cnt += i
            elif tmp == '1':
                cnt -= i
            elif tmp == '2':
                cnt *= i
            else:
                if cnt < 0 and i >= 0:
                    cnt = -(abs(cnt) // i)
                else:
                    cnt //= i
        else:
            tmp = i
    max_num = max(cnt, max_num)
    min_num = min(cnt, min_num)
    if max_num == cnt:
        print(result)
    if min_num == cnt:
        print('min', result)

def back(result, chk):
    global n
    if len(result) == (N * 2) - 1:
        n += 1
        clac(result)
        return
    elif chk:
        for i in range(N):
            if used[i] == 0:
                used[i] = 1
                result.append(nums[i])
                back(result, False)
                used[i] = 0
                result.pop()
    else:
        for i in range(4):
            if op[i] != 0:
                op[i] -= 1
                result.append(str(i))
                back(result, True)
                op[i] += 1
                result.pop()

I = sys.stdin.readline
N = int(I())
nums = list(map(int, I().split()))
op = list(map(int, I().split()))
min_num = 1000000000
max_num = -1000000000
used = [0] * N
n = 0
back([], True)
print(max_num)
print(min_num)
print('n', n)