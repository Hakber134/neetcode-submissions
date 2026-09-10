class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []                      # Final list of triplets
        nums.sort()                   # Step 1: Sort the input array

        for i, a in enumerate(nums):  # Step 2: Iterate through the array
            if i > 0 and a == nums[i - 1]:
                continue              # Skip duplicate values for `a`

            l, r = i + 1, len(nums) - 1  # Step 3: Two-pointer approach
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1            # If sum too big, move right pointer left
                elif threeSum < 0:
                    l += 1            # If sum too small, move left pointer right
                else:
                    res.append([a, nums[l], nums[r]])  # Valid triplet found
                    l += 1
                    r -= 1
                    # Skip duplicates for nums[l]
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res