class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_sum, min_sum = 1,1
        res = nums[0]

        for num in nums:
            tmp = max_sum * num
            max_sum = max( max_sum * num, min_sum *num, num)
            min_sum = min( tmp, min_sum *num, num)
            res = max(res, max_sum)
        return res

        