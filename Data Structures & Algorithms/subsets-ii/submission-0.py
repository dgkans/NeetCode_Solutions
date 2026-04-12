class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result_list = []
        nums.sort()

        def backtrack(temp_set, start):
            # If already present, skip
            if temp_set in result_list:
                return

            # Add a copy of current subset
            result_list.append(temp_set[:])

            for i in range(start, len(nums)):
                # Include nums[i]
                temp_set.append(nums[i])

                # Recurse
                backtrack(temp_set, i + 1)

                # Remove last element (backtrack)
                temp_set.pop()

        backtrack([], 0)
        return result_list