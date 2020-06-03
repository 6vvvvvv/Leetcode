# Share
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
###################################################################################################################
# replace the parentheses with blank and return the new length, if new length equals 0 then valid otherwise invalid
class Solution:
    def isValid(self, s: str) -> bool:
        length = len(s)

        if s == "":
            return True

        if length == 0:
            return False

        if length % 2 != 0:
            return False

        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace("{}", '').replace("[]", '').replace("()", '')

        newLength = len(s)

        if newLength == 0:
            return True
        else:
            return False
