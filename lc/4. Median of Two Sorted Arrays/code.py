class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr=nums1+nums2
        arr.sort()
        l=len(arr)
        if l%2==1:
            return arr[(l-1)//2]
        else:
            return (arr[(l-2)//2]+arr[l//2])/2
        # nums = []
        # i,j = 0,0
        # n,m = len(nums1),len(nums2)
        # while i < n and j < m:
        #     if nums1[i] < nums2[j]:
        #         nums.append(nums1[i])
        #         i += 1
        #     elif nums2[j] < nums1[i]:
        #         nums.append(nums2[j])
        #         j += 1
        #     else:
        #         nums.append(nums2[j])
        #         nums.append(nums1[i])
        #         i,j = i+1,j+1
        # nums += nums1[i:] if i < n else nums2[j:]
        # #print(nums)
        # l = (m+n) // 2        
        # if (m+n) % 2 == 0:

        #     return (nums[l]+nums[l-1])/2
        # else:
        #     return nums[l]

        

