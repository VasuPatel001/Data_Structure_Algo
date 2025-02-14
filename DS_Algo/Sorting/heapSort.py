import heapq


def heapSort(nums: list[int]) -> list[int]:
    # NOTE: heappq.heapify() converts list to heap priority queue in-place in time O(n) hence we don't store in a new variable
    heapq.heapify(nums)  # note this is min heapq or min priority queue
    result = []
    while nums:
        result.append(heapq.heappop(nums))
    return result
