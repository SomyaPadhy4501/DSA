class Solution:
    def twoSum(self, num, target):
        count = 0
        for i in range(len(num)):
            sum = 0
            for j in range(i, len(num)):
                sum += num[j]
                if sum == target:
                    count += 1
        return count
 