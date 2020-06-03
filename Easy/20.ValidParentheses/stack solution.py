# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
########################################################################################
# stack method: if char in leftP list then pile in the stack, else then char must in rightP list["}","]",")"], 
#               once in rightP then compare to the top element in the stack and make the match, it matches then 
#               pop out the top element. We repeat the process and finally get the length of the stack if 0 then 
#               return true else return false which means it still exists elements in the stack. 



class Solution:
    def isValid(self, s: str) -> bool:
        
        leftP=['(','{','[']
        
        stack=[]
        
        for character in s:
            
            if character in leftP:
                stack.append(character)
            
            elif not stack:
                return False
            
            elif stack[-1]=='{' and character =='}':
                stack.pop()
            elif stack[-1]=='[' and character ==']':
                stack.pop()
            elif stack[-1]=='(' and character ==')':
                stack.pop()

            else:
                return False
                
        return len(stack)==0
