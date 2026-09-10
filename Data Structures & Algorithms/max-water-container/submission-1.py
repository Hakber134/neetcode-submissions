class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1  # Start with pointers at both ends
        res = 0  # This will hold the max area found

        # Continue until the two pointers meet
        while l < r:
            # Calculate the height and width of the container
            h = min(height[l], height[r])  # Limiting height is the shorter line
            w = r - l  # Distance between the lines is the width
            area = h * w  # Area of the current container

            res = max(res, area)  # Update max area if this one is bigger

            # Move the pointer at the shorter line inward
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return res  # Return the maximum area found