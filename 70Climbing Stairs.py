##Climbing Stairs
##You are climbing a stair case.
##It takes n steps to reach to the top.
##Each time you can either climb 1 or 2 steps.
##In how many distinct ways can you climb to the top?
##
##2015年7月10日
##zss

##TLE
##class Solution:
##    # @param {integer} n
##    # @return {integer}
##    def climbStairs(self, n):
##        if n==0:return 0
##        elif n==1:return 1
##        elif n==2:return 2
##        else:return self.climbStairs(n-1)+self.climbStairs(n-2)

##AC
class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if not n:return 0
        elif n==1:return 1
        elif n==2:return 2
        a,b = 1,2
        for i in range(3,n+1):
            a,b = b,a+b
        return b
