#
# @lc app=leetcode id=1390 lang=python3
#
# [1390] Four Divisors
#

# @lc code=start
# precompute all valid numbers with exactly four divisors
# a valid number with exactly four divisors is a number that is producted by two prime numbers

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def generate_valid_numbers(limit):
            is_prime = [True] * (limit + 1)
            is_prime[0] = is_prime[1] = False
            for i in range(2, int(limit**0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, limit + 1, i):
                        is_prime[j] = False

            primes = [i for i in range(2, limit + 1) if is_prime[i]]
            valid_numbers = {}

            for i in range(len(primes) - 1):
                for j in range(i + 1, len(primes)):
                    product = primes[i] * primes[j]
                    if product > limit:
                        break
                    divisors_sum = 1 + primes[i] + primes[j] + product
                    valid_numbers[product] = divisors_sum

            for p in primes:
                number = p ** 3
                if number > limit:
                    break
                divisors_sum = 1 + p + p * p + number
                valid_numbers[number] = divisors_sum

            return valid_numbers
        valid_numbers = generate_valid_numbers(100001)
        ans = 0
        for num in nums:
            ans += valid_numbers.get(num, 0)
        return ans
# @lc code=end

