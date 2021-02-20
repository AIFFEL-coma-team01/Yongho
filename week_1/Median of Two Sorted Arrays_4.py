
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3=nums1+nums2
        nums3.sort()
        if len(nums3) %2 == 1 : # 홀수 번이라 2로 나눈 후 +1을 한 값을 return 한다.
            return nums3[int(len(nums3)/2)]
        else :
            num_median = (nums3[len(nums3)//2-1] + nums3[len(nums3)//2])/2
            return num_median



nums1,nums2 = [1,3], [2]
nums3, nums4 = [1,2], [3,4]
nums5,nums6 = [0,0,0], [0,0]
res = Solution.findMedianSortedArrays(1,nums1, nums2) # [1,2]
print("res: ",res)