"""
Leetcode 1213: Intersection of Three Sorted Arrays

Given three arrays sorted in the ascending order, return their intersection sorted array in the ascending order.

Example One
{
"arr1": [2, 5, 10],
"arr2": [2, 3, 4, 10],
"arr3": [2, 4, 10]
}
Output:
[2, 10]

Example Two
{
"arr1": [1, 2, 3],
"arr2": [],
"arr3": [2, 2]
}
Output:
[-1]

Example Three
{
"arr1": [1, 2, 2, 2, 9],
"arr2": [1, 1, 2, 2],
"arr3": [1, 1, 1, 2, 2, 2]
}
Output:
[1, 2, 2]
Notes
If the intersection is empty, return an array with one element -1.

Constraints:
0 <= length of each given array <= 105
0 <= any value in a given array <= 2 * 106
"""


def intersect(arr1, arr2):
    result = []
    # 2 pointer approach
    p1 = 0
    p2 = 0
    while (p1 < len(arr1)) and (p2 < len(arr2)):
        if arr1[p1] < arr2[p2]:
            p1 += 1
        elif arr1[p1] > arr2[p2]:
            p2 += 1
        else:  # arr1[p1] == arr2[p2]
            result.append(arr1[p1])
            p1 += 1
            p2 += 1
    return result


def find_intersection(arr1, arr2, arr3):
    """
    Args:
     arr1(list_int32)
     arr2(list_int32)
     arr3(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    intersect_12 = intersect(arr1, arr2)
    result = intersect(arr3, intersect_12)
    return result if len(result) > 0 else [-1]
