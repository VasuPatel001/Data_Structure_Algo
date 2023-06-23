from collections import Counter

def countingSort(nums: list[int]) -> list[int]:
    low = min(nums)
    high = max(nums)
    cnt = Counter(nums)
    result = []
    for i in range(low, high+1):
        if i in cnt:
            for _ in range(cnt[i]):
                result.append(i)
    return result
