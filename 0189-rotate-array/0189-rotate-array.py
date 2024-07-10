class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k = k%n
        nums[0:n-k] = nums[0:n-k][::-1]
        nums[n-k:] = nums[n-k:][::-1]
        # a=nums[0:-1*k]
        # b = nums[n-k:n]
        # del nums[n-k:n]
        # nums.insert(0,b[::])
        # print(a,b,nums)
        nums[:]=nums[:][::-1]
        return nums