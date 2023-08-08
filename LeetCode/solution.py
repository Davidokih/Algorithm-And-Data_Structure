class Solution():
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        dic = {}
        lst = []
        for i in range(len(nums)):
            sec = i + 1
            last = len(nums) - 1
            while sec < last:
                sum = nums[i] + nums[sec] + nums[last]
                if (sum == 0):
                    val = [nums[i], nums[sec], nums[last]]
                    # print(dic)

                    if (str(val) in dic):
                        dic[str(val)] += 1
                    else:
                        dic[str(val)] = 1
                        lst.append(val)
                    sec += 1
                    last -= 1
                elif sum > 0:
                    last -= 1
                else:
                    sec += 1

        return lst

    def removeDuplicates(self, nums: list[int]) -> int:
        duplicate_store = {}
        new_nums = []
        for i in range(len(nums) - 1):
            if (nums[i] in duplicate_store):
                duplicate_store[nums[i]] += 1
            else:
                new_nums.append(nums[i])
                duplicate_store[nums[i]] = 1
        # print(duplicate_store)
        return new_nums


solutions = Solution()

# print(solutions.threeSum([-1, 0, 1, 2, -1, -4]))

print(solutions.removeDuplicates([1, 2, 3, 4, 5, 2, 3, 5]))


def containsDuplicate(nums: list[int]) -> bool:
    hset = {}
    for i in nums:
        if i in hset:
            return True
        hset[i] = 1

    return False


nums = [1, 2, 3, 1]
# print(containsDuplicate(nums))
