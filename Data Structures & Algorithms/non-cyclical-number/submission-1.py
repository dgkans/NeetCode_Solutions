class Solution:
    def isHappy(self, n: int) -> bool:
        num = str(n)  # Convert the input number to a string
        sum = 0
        arr = []  # To track previously seen sums
        
        # First pass: Calculate the sum of squares of the digits of the initial number
        for i, dig in enumerate(num):
            digit = int(dig)
            sum += digit ** 2  # Accumulate the square of each digit
        
        if sum == 1:  # If the sum becomes 1, return True immediately
            return True
        
        # Continue until sum becomes 1 or a cycle is detected
        while sum != 1:
            if sum in arr:  # Check for cycles
                return False
            arr.append(sum)  # Track the current sum
            
            # Recalculate the sum of the squares of the digits
            num = str(sum)  # Convert sum to string for digit iteration
            sum = 0  # Reset sum for the new calculation
            for i, dig in enumerate(num):
                digit = int(dig)
                sum += digit ** 2  # Accumulate the square of each digit
        
        return True  # If we reach 1, the number is happy
