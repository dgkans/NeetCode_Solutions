class Solution:
    def isHappy(self, n: int) -> bool:
        num = n  # No need to convert to string initially
        sum = 0
        arr = []
        
        # Loop until we find if the number is happy or enters a cycle
        while sum != 1:
            sum = 0  # Reset sum for the current number
            
            # Calculate the sum of the squares of the digits
            for dig in str(num):  # Use the current number, convert to string for iteration
                digit = int(dig)
                sum += digit ** 2
            
            # Check if we've seen this sum before (cycle detection)
            if sum in arr:
                return False
            
            arr.append(sum)  # Track the current sum
            num = sum  # Update the number to the new sum of squares
        
        return True  # If we reach 1, the number is happy
