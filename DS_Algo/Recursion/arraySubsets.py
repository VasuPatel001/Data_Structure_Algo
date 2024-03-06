def subsetA(arr: list[int]):
    """_summary_

    Parameters
    ----------
    arr : list[int]
        _description_
    """
    arr = sorted(arr)
    total_sum = sum(arr)
    set_A = []

    def helper(arr: list[int], cur_idx: int, cur_sum: int, total_sum: int, slate: list[int], set_A: list[int]):

        # back tracking case
        if cur_sum <= total_sum - cur_sum:
            return

        # Base case
        if cur_idx == len(arr):
            set_A = slate[:]
            return

        count = 0
        for i in range(cur_idx, len(arr)):
            if arr[i] == arr[cur_idx]:
                count += 1
            else:
                break

        # inclusion
        for _ in range(count):
            slate.append(arr[cur_idx])
            helper(arr, cur_idx + count, cur_sum + arr[cur_idx], total_sum, slate, set_A)

        for _ in range(count):
            slate.pop(arr[cur_idx])

        # exclusion
        helper(arr, cur_idx + count, cur_sum, total_sum, slate, set_A)

    helper(arr, 0, 0, total_sum, [], set_A)
    return set_A
