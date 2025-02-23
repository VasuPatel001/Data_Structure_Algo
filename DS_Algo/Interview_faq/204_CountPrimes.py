"""
Leetcode 204. Count Primes
Medium

Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0

Constraints:
0 <= n <= 5 * 106
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        """
        The Sieve of Eratosthenes is the fastest algorithm for finding primes up to ( n ). The improvements come from:
            - Avoiding unnecessary loops.
            - Marking multiples efficiently starting from ( p^2 ), since smaller multiples would already be marked.

        Approach:
        1. Base Case:
            - Return ( 0 ) if ( n \leq 2 ), as no primes exist in this range.
        2. Efficient Marking:
            - Use an arrayis_primeof size ( n ), initialized toTrue.
            - Iterate only up to ( \sqrt{n} ), as factors repeat beyond this range.
            - Mark multiples of each prime starting from ( p^2 ), as smaller multiples would have been marked by smaller primes.
        3. Count Primes:
            - CountTruevalues inis_prime.
        Complexity:
            - Time Complexity: O(N(log(logN)), as the sieve is extremely efficient.
            - Space Complexity: O(N), due to theis_primearray.

        """
        if n == 0 or n == 1:
            return 0

        is_prime = [1 for _ in range(n+1)]
        is_prime[0] = 0
        is_prime[1] = 0

        for i in range(2, int(n**0.5)+1):  # Iterate only up to sqrt{N}, as factors repeat beyond this range
            if is_prime[i] == 1:
                for j in range(i*i, n, i):  # Mark multiples of each prime starting from ( p^2 ), as smaller multiples would have been marked by smaller primes.
                    is_prime[j] = 0
        return sum(is_prime) - 1
