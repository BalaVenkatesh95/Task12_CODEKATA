N, M = map(int, input().split())
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
print(gcd(N, M))

'''
while b != 0::

This line starts a while loop that continues as long as b is not equal to 0.
a, b = b, a % b:

In each iteration of the loop, this line updates the values of a and b.
a is assigned the value of b.
b is assigned the remainder of a divided by b, calculated using the modulus operator %.
return a:

After the loop finishes (when b becomes 0), this line returns the final value of a, which is the HCF of the original values of a and b.
'''

