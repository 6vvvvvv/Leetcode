# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.
##############################################################3
# firstly find out the shortest string in the list 
# secondly iterate letter from left to right based on the length of the shortest string for all the other element
# if not equal then break(once occur then true) else until return the shortest string

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        else:
            # lengthtemp=[]

            # for item in strs:
            #     lengthtemp.append(len(item))
            #     innerlength=min(lengthtemp)

            min_length_in_strs = min(strs, key=len)
            for key, char in enumerate(min_length_in_strs):
                for other in strs:
                    if other[key]!=char:
                        return min_length_in_strs[:key]
            return min_length_in_strs
