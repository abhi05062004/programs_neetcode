class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        remainder={}
        for i in nums:
            if i in remainder:
                  return True
            remainder[i]=1
        print(remainder)
        return False