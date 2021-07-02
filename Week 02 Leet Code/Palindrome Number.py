class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0 :
            return False
        
        sum , temp = 0 , x
        
        while x != 0 :
            sum = sum*10 + x%10
            x = x // 10
        if sum == temp :
            return True
        else :
            return False
