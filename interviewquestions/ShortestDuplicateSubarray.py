# 1779 最短重复子数组Shortest Duplicate Subarray
#
# English
# Given an array, return the shortest subarray length which has duplicate elements.
#
# If the array doesn't ha the subarray which has duplicate elements, return -1.
#
# 0 <= arr.length <= 10^6

# Example 1:
#
# Input: [1,2,3,1,4,5,4,6,8]
# Output: 3
# Explanation: The the shortest subarray which has duplicate elements is [4,5,4].
# Example 2:
#
# Input: [1,1]
# Output: 2
# Explanation: The the shortest subarray which has duplicate elements is [1,1].

class Solution:
    """
    @param arr: The array you should find shortest subarray length which has duplicate elements.
    @return Return the shortest subarray length which has duplicate elements.
    """
    def getShort(selef,arr):
        hashMap = {}
        for i in range(len(arr)):
            hashMap[i]=len(arr)
            temp=1
            for value in arr[i+1:]:
                if value == arr[i]:
                    hashMap[i]=temp
                    break
                temp+=1
        sortedHashMap = sorted(hashMap.items(),key=lambda x:x[1],reverse=False)
        shortItem = sortedHashMap.pop(0)
        startIndex = shortItem[0]
        endIndex = shortItem[0]+shortItem[1]+1
        return len(arr[startIndex:endIndex])


if __name__ == '__main__':
    solution = Solution()
    print(solution.getShort([1,2,3,1,4,5,4,6,8]))
    print(solution.getShort([1,1]))
    print(solution.getShort([1,7,345,3,5,7,1,5]))
