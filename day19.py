def findInsertIdx(ary, data):
    findIdx = -1  # 초깃값은 없는 위치로
    for i in range(0, len(ary)):
        if (ary[i] < data):
            findIdx = i
            break
    if findIdx == -1:  # 큰 값을 못찾음 == 제일 마지막 위치
        return len(ary)
    else:
        return findIdx

before_arr = [107, 152,136,128, 176,24,97,13,102,137]
after_arr = []
for i in range(len(before_arr)):
    num_location = findInsertIdx(after_arr,before_arr[i])
    after_arr.insert(num_location,before_arr[i])

print(before_arr)
print(after_arr)

