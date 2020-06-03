# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"

# #####################################################
# Basic thought is simple. when you increase s by 1 character, you could only 
# increase maxPalindromeLen by 1 or 2, and that new maxPalindrome includes this 
# new character. Proof: if on adding 1 character, maxPalindromeLen increased by 
# 3 or more, say the new maxPalindromeLen is Q, and the old maxPalindromeLen is P, 
# and Q>=P+3. Then it would mean, even without this new character, there would be 
# a palindromic substring ending in the last character, whose length is at least Q-2. 
# Since Q-2 would be >P, this contradicts the condition that P is the maxPalindromeLen without the additional character.

# So, it becomes simple, you only need to scan from beginning to the end, 
# adding one character at a time, keeping track of maxPalindromeLen, and for each 
# added character, you check if the substrings ending with this new character, with 
# length P+1 or P+2, are palindromes, and update accordingly.

# Now, this is O(n^2) as taking substrings and checking palindromicity seem O(n) 
# time. We can speed up it by realizing that strings are immutable, and there are memory 
# slicing tricks will help to speed these operations up. comparing string equality with "==" is O(1), 
# and using slicing to substring and reverse is ̶a̶l̶s̶o̶ ̶O̶(̶1̶)̶ ̶
# (̶n̶o̶t̶ ̶t̶o̶t̶a̶l̶l̶y̶ ̶s̶u̶r̶e̶ ̶a̶b̶o̶u̶t̶ ̶t̶h̶e̶ ̶s̶l̶i̶c̶i̶n̶g̶ ̶t̶h̶o̶u̶g̶h̶.̶ ̶ ̶I̶ ̶t̶h̶i̶n̶k̶ ̶i̶t̶ ̶i̶s̶ ̶O̶(̶1̶)̶,̶ ̶b̶u̶t̶ ̶c̶o̶u̶l̶d̶ ̶n̶o̶t̶ ̶f̶i̶n̶d̶ ̶a̶n̶y̶ ̶s̶o̶l̶i̶d̶ ̶l̶i̶t̶e̶r̶a̶t̶u̶r̶e̶ ̶a̶b̶o̶u̶t̶ ̶i̶t̶.̶ O(n) 
# (thanks to ChuntaoLu). But as slicing is optimized by the interpreter's C code, it should run pretty fast. 
# I'm pretty new to Python. Would appreciate you would give more insights or further optimization.

# Thus, here is the O(n) method:
class Solution:
    def longestPalindrome(self, s: str) -> str:
                abbc
        if len(s)==0:
            return 0
        maxLen=1
        start=0
        for i in range(len(s)):
            if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
                start=i-maxLen-1
                maxLen+=2
                continue

            if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
                start=i-maxLen
                maxLen+=1
        return s[start:start+maxLen]




                

