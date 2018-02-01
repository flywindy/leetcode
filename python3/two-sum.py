# Time:  O(n)
# Space: O(n)

# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for index1, num1 in enumerate(nums):
            another = target - num1
            if another in nums_dict:
                index2 = nums_dict[another]
                if index1 != index2:
                    return [index1, index2]
            else:
                nums_dict[num1] = index1


if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))