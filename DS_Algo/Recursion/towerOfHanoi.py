def towerOfHanoi(n: int, src, dst, aux, moves) -> int:
    if n <= 1:
        return 1
    moves += towerOfHanoi(n-1, src, dst, aux, moves)
    moves += 1  # 1 move required to move nth disk from src to dst
    moves += towerOfHanoi(n-1, aux, dst, src, moves)
    return moves


def movesForTowerOfHanoi(n):
    src = []
    dst = []
    aux = []
    moves = 0
    return towerOfHanoi(n, src, dst, aux, moves)


if __name__ == "__main__":
    n = 5
    print(movesForTowerOfHanoi(n))
