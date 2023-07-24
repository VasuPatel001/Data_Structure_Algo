"""
Pseudo Random Numbers

Random numbers are genrated using Linear Congruential Method.
https://www.geeksforgeeks.org/linear-congruence-method-for-generating-pseudo-random-numbers/
In this problem we return the length of the cycle.
"""


class Solution:
    def findCycleLen(z: int, i: int, seed: int, m: int) -> int:

        def f(curr_val: int):
            return (z * curr_val + i) % m

        hare = seed
        tortoise = seed
        while True:
            hare = f(f(hare))
            tortoise = f(tortoise)
            if hare == tortoise:  # cycle detected
                # Change in initialization of third_pointer as compared to cycle detection starting node (problem# 142)
                # for problem 142, we initialized third_pointer = head, however he we initialize third_pointer to tortoise
                third_pointer = tortoise
                length = 1
                while f(third_pointer) != tortoise:
                    third_pointer = f(third_pointer)
                    length += 1
                return length
