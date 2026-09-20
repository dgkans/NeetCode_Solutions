from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # One empty prefix exists before the first element
        prefix_count = {0: 1}

        # Sum from the beginning through the current position
        current_sum = 0

        # Total number of matching subarrays
        count = 0

        for number in nums:
            current_sum += number

            # Earlier prefix needed to leave a subarray sum of k
            needed = current_sum - k

            # Every matching earlier prefix gives one valid subarray
            if needed in prefix_count:
                count += prefix_count[needed]

            # Record this prefix for future positions
            if current_sum in prefix_count:
                prefix_count[current_sum] += 1
            else:
                prefix_count[current_sum] = 1

        return count