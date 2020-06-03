# Given a 32-bit signed integer, reverse digits of an integer.
# Input: 123
# Output: 321
#########################################################
# str to int finally int to str, it should notice that after reverse it might
# exceed the scope

class Solution:
    def reverse(self, x: int) -> int:
          if x>2**31-1 or x<-2**31:
            return 0

          elif x>0 and x<2**31-1 :
            
                str_To_Int=str(x)
                str_To_Int_Inv=str_To_Int[::-1]
                
                if int(str_To_Int_Inv) > 2**31-1:
                    return 0
                else:
                    return int(str_To_Int_Inv)
          elif x<0 and x>-2**31 :
                x=-x
                str_To_Int=str(x)
                str_To_Int_Inv=str_To_Int[::-1]
                if int(str_To_Int_Inv)>2**31-1:
                    return 0
                else:
                    return -int(str_To_Int_Inv)
          else:
                return 0