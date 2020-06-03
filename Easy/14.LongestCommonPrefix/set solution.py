# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# zip(*strs)
# >>>a = [1,2,3]
# >>> b = [4,5,6]
# >>> c = [4,5,6,7,8]
# >>> zipped = zip(a,b)     # 打包为元组的列表
# [(1, 4), (2, 5), (3, 6)]
# >>> zip(a,c)              # 元素个数与最短的列表一致
# [(1, 4), (2, 5), (3, 6)]
# >>> zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
# [(1, 2, 3), (4, 5, 6)]

# nums = ['flower','flow','flight']
# for i in zip(*nums):
#     print(i)

# ('f', 'f', 'f')
# ('l', 'l', 'l')
# ('o', 'o', 'i')
# ('w', 'w', 'g')

# return based on the set length, if larger than 1 means there exist same elements then should break, else then continue

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sz, ret = zip(*strs), ""
        # looping corrected based on @StefanPochmann's comment below
        for c in sz:
            if len(set(c)) > 1: break
            ret += c[0]
        return ret