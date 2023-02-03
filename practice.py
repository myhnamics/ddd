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

if __name__ == "__main":
    pokemons = ["파이리", "피카츄", "망냐뇽", "찌르꼬","이상해씨"]

    print(len(pokemons))
    new_pokemon(2, '피츄')
    print(pokemons)
    new_pokemon(6, '왕자리')
    print(pokemons)
