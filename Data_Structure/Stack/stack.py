
class Stack():
    def __init__(self):
        self.items = []

    def push(self, element):
        self.items = self.items + [element]

    def pop(self):
        return self.items.pop()

    def peek(self):
        count = len(self.items)
        if (self.items == 0):
            return

        return self.items[count - 1]

    def print(self):
        print(self.items)


stack = Stack()

stack.push(10)
stack.push(14)
stack.push(20)

stack.print()

# class Solution():
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         for i in range(len(nums) - 1):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return 1


# solutions = Solution()

# print(solutions.twoSum([2, 7, 11, 15], 9))
# class Solution():
#     def threeSum(self, nums: list[any]) -> list[list[any]]:
#         arr = []
#         for i in range(len(nums) - 1):
#             for j in range(i + 1, len(nums)):
#                 for k in range(j + 1, len(nums)):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         arr.append([nums[i], nums[j], nums[k]])
#         return arr


# solutions = Solution()

# print(solutions.threeSum([-1, 0, 1, 2, -1, -4]))
