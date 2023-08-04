import re


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            print(str(x)[::-1])
            return True
        else:
            return False

    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        constant = m + n - 1
        i = m - 1
        j = n - 1
        while j >= 0:
            # print(nums1)
            if (i >= 0 and nums1[i] > nums2[j]):
                nums1[constant] = nums1[i]
                i -= 1
            else:
                nums1[constant] = nums2[j]
                j -= 1
            constant -= 1

    def isPalindromeString(self, s: str) -> bool:
        punctuations = '''!()-[]{};:'`"\,<>./?@#$%^&*_~ '''
        arr = [i for i in punctuations]
        lowerCase = s.lower()
        new_str = ""
        for i in lowerCase:
            if (i not in arr):
                new_str += i

        return new_str[::-1] == new_str


Solution = Solution()

# print(Solution.isPalindrome(121))
print(Solution.isPalindromeString("A man, a plan, a canal: Panama"))
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
Solution.merge(nums1, m, nums2, n)
# print(nums1)


# print(arr)
