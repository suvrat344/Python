# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# Example 1:
# Input: x = 2.00000, n = 10
# Output: 1024.00000

# Example 2:
# Input: x = 2.10000, n = 3
# Output: 9.26100

# Example 3:
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25


class Solution:
  def pow(self,x,n):
    res = 1
    if(n == 0):
      return 1
    if(n < 0):
      x = 1 / x
      n = -n
    while(n > 0):
      if(n % 2 == 1):
        res = res * x
      x *=  x
      n //= 2
    return res


exponent = float(input("Enter exponent : "))
power = int(input("Enter power : "))

res = Solution()
print(f"{exponent}^{power} = {res.pow(exponent,power)}")