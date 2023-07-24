class Solution:
    def isPalindrome(self, x: int) -> list[int]:
        arr = [i for i in str(x)]
        arr.reverse()
        a = ''.join(arr)
        if (int(a) == x):
            return True

        return False
        # for i in str(x):


Solution = Solution()

print(Solution.isPalindrome(123))
