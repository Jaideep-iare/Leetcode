class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k%len(nums)
        nums[:] = nums[-k:]+nums[:-k]
        return nums
        # n=len(nums)
        # k = k%n
        # nums[0:n-k] = nums[0:n-k][::-1]
        # nums[n-k:] = nums[n-k:][::-1]
        # nums[:]=nums[:][::-1]