class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums1=Counter(nums)
        sa=nums1.most_common()
        print(sa)
        ans=[]
        if len(nums)<=k:
            return nums
        for j in range(k):
            ans.append(sa[j][0])
        return ans
                
        