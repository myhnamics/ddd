memos = [None for _ in range(100)]
memos[0] = 0
memos[1] = 1

count_memo_recu = 0
def fibo_memo_recu(n):
    global memos, count_memo_recu
    count_memo_recu += 1
    if n <= 1:
        return memos[n]

    if memos[n] is not None:
        return memos[n]

    memos[n] = fibo_memo_recu(n-2) + fibo_memo_recu(n-1)
    return memos[n]



memo = list() # 전역 변수로 한 번 처리한 결과 값을 저장
def fibo_memo(n):
    global memo
    memo = [0, 1]
    """
    memorization(dp)을 사용한 피보나치 수열 처리 함수
    :param n: 
    :return: 
    """
    if n <= 1:
        return memo[n]
    else:
        for i in range(2, n+1):
            memo.append(memo[i-1] + memo[i-2])
        return memo[n]


count_recu = 0
def fibo_recu(n):
     global count_recu
     count_recu += 1
     if n <= 1:
         return n
     else:
         return fibo_recu(n - 1) + fibo_recu(n - 2)




def fibo_iter(n):
    r = list()
    p1, p2 = 1, 1
    for _ in range(n):
        r.append(p1)
        p1, p2 = p2, p1 + p2
    return r[-1]

print('피보나치 수 -> 0 1 ', end = '')
for i in range(1,40):
    print(f'{i} : {fibo_recu(i)}',end = '')
    # print(f'{fibo_recu(i)}',end = ' ')
    # print(f'{i} : {fibo_memo(i)}')  # recursion
print()
print(count_recu)
for i in range(1,40):
    print(f'{i} : {fibo_memo_recu(i)}')  # recursion
print(count_memo_recu)

