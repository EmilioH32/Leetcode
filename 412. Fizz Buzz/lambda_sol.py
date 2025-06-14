class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        remainder_three = lambda x: x % 3
        remainder_five = lambda y: y % 5
        ans = []
        for i in range(n):
            i += 1
            if remainder_three(i) == 0 and remainder_five(i) == 0:
                ans.append("FizzBuzz")
            elif remainder_three(i) == 0:
                ans.append("Fizz")
            elif remainder_five(i) == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans