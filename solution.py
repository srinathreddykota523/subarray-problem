from collections import defaultdict
from typing import List

class Solution:
    def maxSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n
        ans = 2
        l = 0
        new_l = 0
        seen = defaultdict(int)
        seen[nums[0]] += 1
        seen[nums[1]] += 1
        r = 2
        
        while r < n:
            k = r
            
            for i in range(l, r-1):
                if (abs(nums[k] - nums[i]) in seen) or ((nums[k] + nums[i]) in seen):
                    if abs(nums[k] - nums[i]) == nums[i] and seen[nums[i]] == 1 and nums[k] + nums[i] not in seen:
                        continue
                        
                    else:  
                        
                        for x in range(new_l, i+1):
                            seen[nums[x]] -= 1
                            if seen[nums[x]] == 0:
                                del seen[nums[x]]
                        new_l = i+1
            
            seen[nums[r]] += 1       
            ans = max(ans, r-new_l+1)
            l = new_l
            r += 1
        
        return ans