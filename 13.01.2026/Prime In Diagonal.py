class Solution:
    def diagonalPrime(self, nums):
        diagonal_vals = set()
        max_prime = 0
        n = len(nums)

        for i in range(n):
            diagonal_vals.add(nums[i][i])
            diagonal_vals.add(nums[i][n-1-i])

        for val in diagonal_vals:
            if val > 1 and all(val % i != 0 for i in range(2, int(val ** 0.5) + 1)):
                max_prime = max(max_prime, val)

        return max_prime
