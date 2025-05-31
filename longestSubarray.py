class longestSubarray:
    def longestSubarraywithsumk(self, a, target):
        prefix_map = {}
        current_sum = 0
        max_length = 0
        
        for i in range(len(a)):
            current_sum += a[i]
            
            if current_sum == target:
                max_length = max(max_length, i + 1)
            
            remainder = current_sum - target
            
            if remainder in prefix_map:
                length = i - prefix_map[remainder]
                max_length = max(max_length, length)
            
            if current_sum not in prefix_map:
                prefix_map[current_sum] = i
        
        return max_length
