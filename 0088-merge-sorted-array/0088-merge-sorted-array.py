class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=0
        j=0
        while i<m and j<n:
            if nums1[i]>nums2[j]:
                nums1[i],nums2[j]=nums2[j],nums1[i]
                i+=1
                j+=1
            else:
                i+=1
        i=m
        j=0
        while i<m+n and j<n:
            nums1[i]=nums2[j]
            i+=1
            j+=1
        nums1.sort()