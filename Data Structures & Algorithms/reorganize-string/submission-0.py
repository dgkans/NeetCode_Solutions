from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        n = len(s)
        
        # Impossibility check
        if max(freq.values()) > (n + 1) // 2:
            return ""
        
        result = []
        prev_char = ''
        
        for _ in range(n):
            # Get top 2 most frequent characters (with count > 0)
            top = freq.most_common(2)
            
            # Pick the first one unless it equals prev_char
            if top[0][0] != prev_char:
                best_char = top[0][0]
            else:
                best_char = top[1][0]
            
            result.append(best_char)
            freq[best_char] -= 1
            
            # Clean up: remove chars with count 0 so most_common stays clean
            if freq[best_char] == 0:
                del freq[best_char]
            
            prev_char = best_char
        
        return ''.join(result)