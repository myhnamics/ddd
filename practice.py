def new_pokemon(idx, pokemon):
    if idx < 0 or idx > len(pokemons):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return

    pokemons.append(None)  # 빈칸 추가
    len_pokemon = len(pokemons)  # 배열의 현재 크기

    for i in range(len_pokemon - 1, idx, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[idx] = pokemon  # 지정한 위치에 친구 추가


pokemons = ["파이리", "피카츄", "망냐뇽", "찌르꼬","이상해씨"]

print(len(pokemons))
new_pokemon(2, '피츄')
print(pokemons)
new_pokemon(2, '왕자리')
print(pokemons)



def delete_pokemon(position):
    if position < 0 or position > len(pokemons):
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return


    kLen = len(pokemons)
    pokemons[position] = None  # 데이터 삭제

    for i in range(position + 1, kLen):
        pokemons[i - 1] = pokemons[i]
        pokemons[i] = None  # 배열의 맨 마지막 위치 삭제

    del (pokemons[kLen - 1])
#
# delete_pokemon(3)
# print(pokemons)
# delete_pokemon(3)
# print(pokemons)


def delete_pokemon2(k):

    len_p = len(pokemons)
    for i in range(1,len_p-k+1):
        delete_pokemon(k)
        print(pokemons)

# delete_pokemon2(3)


