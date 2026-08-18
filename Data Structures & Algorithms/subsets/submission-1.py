class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []

        def collect(i):
            if i >= len(nums):
                res.append(sol[:])
                return 

            #include
            sol.append(nums[i])
            collect(i+1)

            #exclude
            sol.pop()
            collect(i+1)


        collect(0)
        return res
