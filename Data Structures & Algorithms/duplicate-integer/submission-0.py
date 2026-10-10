class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()            # empty set to remember numbers
        for n in nums:          # go through each number
            if n in seen:       # seen it before?
                return True     # duplicate found
            seen.add(n)         # otherwise remember it
        return False            # got through the whole list, no duplicates